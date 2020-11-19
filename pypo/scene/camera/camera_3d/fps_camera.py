from scene.camera.camera import Camera3D

from pyrr import Vector3

class FPSCamera(Camera3D):
    
    def __init__(self, pos = Vector3([0.0, 1.0, 0.0]), orientation = Vector3([0.0, 0.0, 0.0])):
        super(FPSCamera, self).__init__(pos = pos, orientation = orientation)