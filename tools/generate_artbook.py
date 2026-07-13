#!/usr/bin/env python3
"""Generate the production artbook from the game assets and story data."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image, LongTable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, TableStyle
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "The_Art_of_The_Flatline_Sessions_II.pdf"
MARKDOWN_OUTPUT = ROOT / "docs" / "The_Art_of_The_Flatline_Sessions_II.md"
THUMBS = Path("/tmp/flatline-artbook-thumbs")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def para(text: str) -> str:
    return escape(str(text)).replace("\n", "<br/>")


def npc_context(npc_id: str) -> str:
    path = ROOT / "data" / "npcs" / f"{npc_id}.json"
    if not path.exists():
        return f"Missing dialogue data for {npc_id}."
    data = load(path)
    lines = [f"DIALOGUE — {data.get('name', npc_id)}"]
    for node_id, node in data.get("nodes", {}).items():
        texts = []
        if node.get("text"):
            texts.append(node["text"])
        texts.extend(node.get("random_text", []))
        for text in texts:
            lines.append(f"[{node_id}] {text}")
        for option in node.get("options", []):
            lines.append(f"PLAYER OPTION: {option.get('text', '')}")
    return "\n\n".join(lines)


def add_usage(usages, asset, title, description, dialogue=""):
    if not asset:
        return
    asset = str(asset).removeprefix("res://")
    usages[asset].append({"title": title, "description": description, "dialogue": dialogue})


def collect_usages():
    usages = defaultdict(list)
    chapters = load(ROOT / "data" / "chapters.json")["chapters"]
    chapter_by_id = {c["id"]: c for c in chapters}
    for ch in chapters:
        rooms_data = load(ROOT / ch["rooms"].removeprefix("res://"))
        for room_id, room in rooms_data["rooms"].items():
            bg = f"assets/backgrounds_hd/{room.get('bg')}.png" if room.get("bg") else ""
            dialogue = "\n\n".join(npc_context(n) for n in room.get("npcs", []))
            interactions = []
            for action in room.get("interactions", []):
                interactions.append(
                    f"INTERACTION — {action.get('label', action.get('id', ''))}\n" +
                    "\n".join(action.get("pages", []))
                )
                art = action.get("art", "")
                art_list = art if isinstance(art, list) else ([art] if art else [])
                for idx, page in enumerate(action.get("pages", [])):
                    if art_list:
                        chosen = art_list[min(idx, len(art_list) - 1)]
                        add_usage(usages, chosen, f"Interaction art — {action.get('label', '')}", page)
            context = room.get("desc", "")
            if interactions:
                context += "\n\n" + "\n\n".join(interactions)
            add_usage(
                usages, bg,
                f"Room — {ch['id'].upper()} {ch['title']} / {room.get('name', room_id)}",
                context, dialogue,
            )

        for kind in ("intro", "outro"):
            pages = ch.get(kind, [])
            art = ch.get(f"{kind}_art", ch.get("art", ""))
            art_list = art if isinstance(art, list) else [art]
            for idx, text in enumerate(pages):
                if art_list:
                    add_usage(
                        usages, art_list[min(idx, len(art_list) - 1)],
                        f"{kind.title()} page {idx + 1} — {ch['id'].upper()} {ch['title']}", text,
                    )

    matrix = load(ROOT / "data" / "cyberspace" / "databases.json")
    for db in matrix.get("databases", []):
        if db.get("bg"):
            add_usage(
                usages, f"assets/cyberspace/{db['bg']}.png",
                f"Cyberspace — {db.get('name', db.get('id'))}", db.get("content", ""),
            )

    add_usage(usages, "assets/ui/cover.png", "Title and chapter-select background",
              "Full-screen title image and subdued chapter-select background behind the nine-chapter campaign.")
    add_usage(usages, "assets/ui/logo_with_text.png", "Studio ident",
              "Opening Ronin 48 Games Studio splash shown before the dedication and title.")
    add_usage(usages, "assets/album_art/the_flatline_sessions_ii_count_binary.png", "Soundtrack album artwork",
              "Album-cover asset retained with the game project; not displayed during normal play.")
    add_usage(usages, "icon.svg", "Application icon", "Godot application and exported-build icon.")
    return usages


def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#667085"))
    canvas.drawRightString(letter[0] - 0.55 * inch, 0.35 * inch, f"Page {doc.page}")
    canvas.restoreState()


def preview(path: Path, asset_id: str) -> Path:
    """Create a compact PDF-only JPEG preview without modifying source art."""
    THUMBS.mkdir(parents=True, exist_ok=True)
    target = THUMBS / f"{asset_id}.jpg"
    if target.exists() and target.stat().st_mtime >= path.stat().st_mtime:
        return target
    with PILImage.open(path) as source:
        source.thumbnail((1400, 800), PILImage.Resampling.LANCZOS)
        if source.mode in ("RGBA", "LA"):
            background = PILImage.new("RGB", source.size, (12, 17, 24))
            background.paste(source, mask=source.getchannel("A"))
            source = background
        else:
            source = source.convert("RGB")
        source.save(target, "JPEG", quality=72, optimize=True, progressive=True)
    return target


def build():
    usages = collect_usages()
    all_assets = sorted(
        [p for p in (ROOT / "assets").rglob("*") if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".svg"}]
        + [ROOT / "icon.svg"],
        key=lambda p: str(p.relative_to(ROOT)).lower(),
    )
    # Assign IDs before filtering so the public catalog IDs never shift. Content
    # intentionally absent from the artbook remains an unexplained gap.
    ids = {str(path.relative_to(ROOT)): f"IMG-{idx:03d}" for idx, path in enumerate(all_assets, 1)}
    assets = [path for path in all_assets if path.relative_to(ROOT).as_posix() != "assets/ui/void.png"]

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="AssetTitle", parent=styles["Heading1"], fontSize=18,
                              leading=22, textColor=colors.HexColor("#00A6A6"), spaceAfter=8))
    styles.add(ParagraphStyle(name="UseTitle", parent=styles["Heading2"], fontSize=12,
                              leading=15, textColor=colors.HexColor("#344054"), spaceBefore=10, spaceAfter=4))
    styles.add(ParagraphStyle(name="BodySmall", parent=styles["BodyText"], fontSize=8.5,
                              leading=11, spaceAfter=6))
    styles.add(ParagraphStyle(name="Cover", parent=styles["Title"], alignment=TA_CENTER,
                              textColor=colors.HexColor("#00A6A6")))

    doc = SimpleDocTemplate(str(OUTPUT), pagesize=letter, rightMargin=.55*inch, leftMargin=.55*inch,
                            topMargin=.5*inch, bottomMargin=.5*inch,
                            title="The Art of The Flatline Sessions II")
    story = [Spacer(1, 1.4*inch), Paragraph("THE FLATLINE SESSIONS II", styles["Cover"]),
             Paragraph("THE ART OF THE FLATLINE SESSIONS II", styles["Cover"]), Spacer(1, .3*inch),
             Paragraph("A visual catalog of the production artwork, with the story context and dialogue attached to each image's appearances in the game.", styles["BodyText"]),
             PageBreak(), Paragraph("Asset Index", styles["Heading1"])]

    rows = [[Paragraph("ID", styles["BodySmall"]), Paragraph("Asset", styles["BodySmall"]),
             Paragraph("Primary use", styles["BodySmall"])]]
    for path in assets:
        rel = str(path.relative_to(ROOT))
        primary = usages.get(rel, [{}])[0].get("title", "Not referenced at runtime")
        rows.append([ids[rel], Paragraph(para(rel), styles["BodySmall"]),
                     Paragraph(para(primary), styles["BodySmall"])])
    table = LongTable(rows, colWidths=[.65*inch, 2.8*inch, 3.55*inch], repeatRows=1)
    table.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#D0F0EF")),
                               ("GRID", (0,0), (-1,-1), .25, colors.HexColor("#98A2B3")),
                               ("VALIGN", (0,0), (-1,-1), "TOP"),
                               ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
                               ("FONTSIZE", (0,0), (-1,-1), 7)]))
    story += [table]

    for path in assets:
        rel = str(path.relative_to(ROOT))
        aid = ids[rel]
        story += [PageBreak(), Paragraph(f"{aid} — {para(path.name)}", styles["AssetTitle"]),
                  Paragraph(f"<b>File:</b> {para(rel)}", styles["BodySmall"])]
        if path.suffix.lower() != ".svg":
            img = Image(str(preview(path, aid)))
            img._restrictSize(7.0*inch, 3.9*inch)
            story += [img, Spacer(1, 6)]
        entries = usages.get(rel, [])
        if not entries:
            story.append(Paragraph("No live runtime reference was found. Verify whether this asset should be retained.", styles["BodySmall"]))
        for entry in entries:
            story.append(Paragraph(para(entry["title"]), styles["UseTitle"]))
            story.append(Paragraph(para(entry["description"]), styles["BodySmall"]))
            if entry.get("dialogue"):
                story.append(Paragraph(para(entry["dialogue"]), styles["BodySmall"]))

    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
    markdown = [
        "# The Art of The Flatline Sessions II",
        "",
        "A visual catalog of the production artwork and its story context.",
        "",
    ]
    for path in assets:
        rel = str(path.relative_to(ROOT))
        markdown.extend([f"## {ids[rel]} — `{path.name}`", "", f"![{path.name}](../{rel})", ""])
        entries = usages.get(rel, [])
        if not entries:
            markdown.extend(["Not referenced at runtime.", ""])
        for entry in entries:
            markdown.extend([f"### {entry['title']}", "", entry["description"], ""])
    MARKDOWN_OUTPUT.write_text("\n".join(markdown), encoding="utf-8")
    print(f"Wrote {OUTPUT} and {MARKDOWN_OUTPUT} ({len(assets)} indexed assets, {sum(len(v) for v in usages.values())} usage records)")


if __name__ == "__main__":
    build()
