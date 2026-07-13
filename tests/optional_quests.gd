extends SceneTree
## Regression coverage for optional objectives: they are visible quest steps but
## do not become the current objective or block chapter completion.

const Quests = preload("res://src/story/Quests.gd")

class TestState:
	extends RefCounted
	var flags := {}
	func has_flag(flag: String) -> bool:
		return bool(flags.get(flag, false))

func _initialize() -> void:
	var quests = Quests.new()
	if not quests.load_data():
		printerr("optional_quests: could not load quests")
		quit(1)
		return
	var state = TestState.new()
	var steps := quests.steps("q01_the_job")
	if quests.current_step(state, "q01_the_job") != 4:
		printerr("optional_quests: optional opening steps blocked the required path")
		quit(1)
		return
	for step in steps:
		if not bool(step.get("optional", false)):
			state.flags[str(step.get("flag", ""))] = true
	if not quests.is_complete(state, "q01_the_job"):
		printerr("optional_quests: unfinished optional steps blocked completion")
		quit(1)
		return
	if bool(steps[steps.size() - 1].get("optional", false)) or str(steps[steps.size() - 1].get("flag", "")) != "ch01_boarded_charter":
		printerr("optional_quests: boarding is not the final required objective")
		quit(1)
		return
	print("optional_quests: OK")
	quit(0)
