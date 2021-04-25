from sensor.point import Point

class LidarPoint(Point):
    
    def __init__(self, x = 0.0, y = 0.0, z = 0.0, intensity = 0.0):
        super(LidarPoint, self).__init__(x, y, z)
        self.intensity = intensity