from core.io.loader.kitti_loader import KittiLoader
from core.io.loader.las_loader import LASLoader
from core.io.loader.ply_loader import PLYLoader
from core.io.loader.xyz_loader import XYZLoader

import os

class LoaderFactory(object):
    
    def __init__(self):
        pass

    def load(self, path = ""):
        record = None

        if path.lower().endswith(".bin"):
            loader = KittiLoader(path)
            record = loader.load()
            return record