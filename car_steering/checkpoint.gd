extends Area2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

var finished=false
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_checkpoint_body_entered(body):
	if body.is_in_group('tile'):
		return
	if finished:return
	var finished = true
	self.get_parent().get_parent().passed += 1
	print('checkpoint passed')
