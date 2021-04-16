extends Area2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"

export var laps=3
export var checkpoints=0
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_finish_line_body_entered(body):
	if body.is_in_group('tile'):
		return
	if checkpoints >= self.get_parent().passed:
		print('lap')
		self.get_parent().passed = 0
		self.get_parent().laps += 1
		self.get_parent().get_child(4).get_child(1).text = 'laps : '+String(self.get_parent().laps)+' / '+String(laps)
	else:
		print('not full lap ',self.get_parent().passed,' / ',checkpoints)
	if laps == self.get_parent().laps:
		self.get_parent().get_child(4).get_child(0).visible = true
		self.get_tree().paused=true
		print('you finished')
