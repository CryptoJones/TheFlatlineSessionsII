extends RefCounted
## DialogEngine — data-driven branching conversation runner.
##
## Loads a node graph from JSON ({ "start": id, "nodes": { id: {text, options[]} } })
## and walks it option by option. Extended for the sequels with story hooks:
##   node:   "grant": "<item id>"      give the player an item (once per flag)
##           "set_flag": "<flag>"      set a story flag on arrival
##           "credits": <int>          credit delta on arrival (once per node+npc)
##   option: "require_flag": "<flag>"  only shown once the flag is set
##           "hide_flag": "<flag>"     hidden once the flag is set
## Top-level "start_gates": [{require_flag|unless_flag, start}] override the start
##   node based on story flags (first match wins) — e.g. gate a whole tree behind
##   an item being slotted. Node "random_text": [..] shows one random line per
##   visit; node "repeatable": true tells the UI not to burn the Talk button.
## Pure logic, no display — the UI reads current_* and calls choose().

var npc_name: String = ""
var _nodes: Dictionary = {}
var _current: String = ""

func load_file(path: String, state = null) -> bool:
	if not FileAccess.file_exists(path):
		push_warning("DialogEngine: missing dialog file '%s'" % path)
		return false
	var parsed = JSON.parse_string(FileAccess.get_file_as_string(path))
	if typeof(parsed) != TYPE_DICTIONARY or not parsed.has("nodes"):
		push_warning("DialogEngine: bad dialog file '%s'" % path)
		return false
	npc_name = parsed.get("name", "")
	_nodes = parsed["nodes"]
	_current = parsed.get("start", "")
	# Flag-gated start: the first gate whose condition holds redirects the opening
	# node (e.g. speak-only-Spanish until the language chip is slotted).
	if state != null:
		for g in parsed.get("start_gates", []):
			var req := str(g.get("require_flag", ""))
			if req != "" and not state.has_flag(req):
				continue
			var unless := str(g.get("unless_flag", ""))
			if unless != "" and state.has_flag(unless):
				continue
			var s := str(g.get("start", ""))
			if _nodes.has(s):
				_current = s
				break
	return _nodes.has(_current)

func current_id() -> String:
	return _current

func current_text() -> String:
	if not _nodes.has(_current):
		return ""
	var node: Dictionary = _nodes[_current]
	var rt: Array = node.get("random_text", [])
	if not rt.is_empty():
		return str(rt[randi() % rt.size()])
	return node.get("text", "")

## True when the current node is flagged repeatable — the UI uses this to keep the
## NPC talkable (never marks them "spoken") so a random-line loop can continue.
func current_repeatable() -> bool:
	if _nodes.has(_current):
		return bool(_nodes[_current].get("repeatable", false))
	return false

## Options visible at the current node given the story flags in `state`.
## Each is the raw option Dictionary plus its original index in "_idx".
func current_options(state = null) -> Array:
	if not _nodes.has(_current):
		return []
	var raw: Array = _nodes[_current].get("options", [])
	var out: Array = []
	for i in raw.size():
		var o: Dictionary = raw[i]
		if state != null:
			var req := str(o.get("require_flag", ""))
			if req != "" and not state.has_flag(req):
				continue
			var hide := str(o.get("hide_flag", ""))
			if hide != "" and state.has_flag(hide):
				continue
		var oo := o.duplicate()
		oo["_idx"] = i
		out.append(oo)
	return out

## Item id this node grants the player, or "".
func current_grant() -> String:
	if _nodes.has(_current):
		return _nodes[_current].get("grant", "")
	return ""

## Story flag this node sets on arrival, or "".
func current_set_flag() -> String:
	if _nodes.has(_current):
		return _nodes[_current].get("set_flag", "")
	return ""

## Credit delta this node applies on arrival (0 for none).
func current_credits() -> int:
	if _nodes.has(_current):
		return int(_nodes[_current].get("credits", 0))
	return 0

## True when the current node has no options (conversation can end here).
func is_terminal(state = null) -> bool:
	return current_options(state).is_empty()

## Advance along the RAW option index (use the "_idx" from current_options).
func choose(raw_index: int) -> bool:
	if not _nodes.has(_current):
		return false
	var opts: Array = _nodes[_current].get("options", [])
	if raw_index < 0 or raw_index >= opts.size():
		return false
	var nxt: String = opts[raw_index].get("next", "")
	if not _nodes.has(nxt):
		return false
	_current = nxt
	return true
