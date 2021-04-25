from core.io.loader.loader import Loader
from sensor.point_cloud import PointCloud
from sensor.lidar.point import LidarPoint
from struct import unpack

class KittiLoader(Loader):
    
    def __init__(self, path = ""):
        super(KittiLoader, self).__init__()

        self._record_path = path

    @property
    def record_path(self):
        return self._record_path

    @record_path.setter
    def record_path(self, path):
        self._record_path = path

    def load(self):
        try:
            point_cloud = PointCloud()

            with open(self._record_path, "rb") as file:
                while True: 
                    # Raw data are a block of 4 float (x, y, z, intensity) representing a single point
                    b = file.read(16)

                    if not b:
                        break

                    point = LidarPoint()
                    point.x, point.y, point.z = unpack('fff', b[:12])[:]
                    point.intensity = unpack('f', b[12:])[0]

                    point_cloud.points.append(point)

                self._record.add_frame(point_cloud)

                return self._record
        except Exception as e:
            print(e)