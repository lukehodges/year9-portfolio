extends Area2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var time = 0
var started=false
onready var timer = self.get_parent().get_child(4).get_child(2)
# Called when the node enters the scene tree for the first time.
func _ready():
	print('running')
	connect("body_enter",self,"_on_start_entered")
	print('connected')
func _on_start_entered(area):
	if started:return
	if area.is_in_group('tile'):return
	
	started = true
	print(time)
	print('started')
func _process(delta):
	if started:
		time += delta
		timer.text = String(time).substr(0,5)
