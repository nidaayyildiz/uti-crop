"""
    It is one of the preprocessing components in which the image is rotated.
"""

import os
import cv2
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Crop.src.utils.response import build_response_AbsoluteCrop
from components.Crop.src.models.PackageModel import PackageModel


class AbsoluteCrop(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.xCenterAbsolute = self.request.get_param("XCenterAbsolute")
        self.yCenterAbsolute = self.request.get_param("YCenterAbsolute")
        self.widthAbsolute = self.request.get_param("WidthAbsolute")
        self.heightAbsolute = self.request.get_param("HeightAbsolute")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def absolute_static_crop( self, img):
        x_min = round(self.xCenterAbsolute - self.widthAbsolute / 2)
        y_min = round(self.yCenterAbsolute - self.heightAbsolute / 2)
        x_max = round(x_min + self.widthAbsolute)
        y_max = round(y_min + self.heightAbsolute)
        cropped_image = img[y_min:y_max, x_min:x_max]
        if not cropped_image.size:
            return None
        return cropped_image

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.absolute_static_crop(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_AbsoluteCrop(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()
