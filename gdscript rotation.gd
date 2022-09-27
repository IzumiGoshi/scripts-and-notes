extends Spatial


onready var X := Spatial.new()
onready var Y := Spatial.new()
onready var Z := Spatial.new()
onready var model := $Model

func _ready() -> void:
	"""
		SPATIAL (with this script)
			MODEL (object that gets rotated)
	"""
	add_child(X)
	X.add_child(Y)
	Y.add_child(Z)
	remove_child(model) # dont forget this part!
	Z.add_child(model)  # !important

func controls(delta):
	var u : Vector3 = Z.global_transform.basis.y
	var r : Vector3 = Z.global_transform.basis.x
	var f : Vector3 = Z.global_transform.basis.z
	
	if Input.is_key_pressed(KEY_A):
		X.global_rotate(u, delta)
	if Input.is_key_pressed(KEY_D):
		X.global_rotate(u, -delta)
		
	if Input.is_key_pressed(KEY_W):
		Y.global_rotate(r, delta)
	if Input.is_key_pressed(KEY_S):
		Y.global_rotate(r, -delta)
		
	if Input.is_key_pressed(KEY_Z):
		Y.global_rotate(f, delta)
	if Input.is_key_pressed(KEY_C):
		Y.global_rotate(f, -delta)
	

func _process(delta: float) -> void:
	controls(delta)
