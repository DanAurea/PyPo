from scene.camera.camera import Camera3D

from pyrr import Vector3

class FlyCamera(Camera3D):
    
    def __init__(self, pos = Vector3([0.0, 1.0, 0.0]), orientation = Vector3([0.0, 0.0, 0.0])):
        super(FlyCamera, self).__init__(pos = pos, orientation = orientation)