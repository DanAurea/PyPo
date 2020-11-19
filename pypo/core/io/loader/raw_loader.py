from core.io.loader.loader import Loader

class RawLoader(Loader):
    
    def __init__(self, point_cloud = point_cloud):
        super(RawLoader, self).__init__()

        self._point_cloud = point_cloud 

    def load(self):
        return self._point_cloud