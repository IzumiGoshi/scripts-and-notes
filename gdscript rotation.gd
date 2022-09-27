extends Spatial


onready var X := Spatial.new()
onready var Y := Spatial.new()
onready var Z := Spatial.new()
onready var zup := Vector3()
onready var zright := Vector3()
onready var zforward := Vector3()

onready var model := $Model

func _ready() -> void:
	"""
		SPATIAL (with this script)
			MODEL (object that gets rotated)
			
		to rotate the starting rotation rotate this node
	"""
	add_child(X)
	X.add_child(Y)
	Y.add_child(Z)
	remove_child(model) # dont forget this part!
	Z.add_child(model)  # !important

func controls(delta):
	zup = Z.global_transform.basis.y
	zright = Z.global_transform.basis.x
	zforward = Z.global_transform.basis.z
	
	if Input.is_key_pressed(KEY_A):
		X.global_rotate(zup, delta)
	if Input.is_key_pressed(KEY_D):
		X.global_rotate(zup, -delta)
		
	if Input.is_key_pressed(KEY_W):
		Y.global_rotate(zright, delta)
	if Input.is_key_pressed(KEY_S):
		Y.global_rotate(zright, -delta)
		
	if Input.is_key_pressed(KEY_Z):
		Y.global_rotate(zforward, delta)
	if Input.is_key_pressed(KEY_C):
		Y.global_rotate(zforward, -delta)
	

func _process(delta: float) -> void:
	controls(delta)
