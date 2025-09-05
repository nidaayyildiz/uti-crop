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
from components.Crop.src.utils.response import build_response_RelativeCrop
from components.Crop.src.models.PackageModel import PackageModel
from sdks.novavision.src.base.logger import LoggerManager

logger = LoggerManager()

class RelativeCrop(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.xCenterRelative = self.request.get_param("xCenterRelative")
        self.yCenterRelative = self.request.get_param("yCenterRelative")
        self.widthRelative = self.request.get_param("widthRelative")
        self.heightRelative = self.request.get_param("heightRelative")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def relative_static_crop(self, img):
        try:
            if None in [self.xCenterRelative, self.yCenterRelative, self.widthRelative, self.heightRelative]:
                logger.error(
                    "One or more crop parameters are None. xCenterRelative: {}, yCenterRelative: {}, widthRelative: {}, heightRelative: {}".format(
                        self.xCenterRelative, self.yCenterRelative, self.widthRelative, self.heightRelative))
                return img
            x_center = float(img.shape[1] * self.xCenterRelative)
            y_center = float(img.shape[0] * self.yCenterRelative)
            width = float(img.shape[1] * self.widthRelative)
            height = float(img.shape[0] * self.heightRelative)

            x_min = int(x_center - (width / 2))
            y_min = int(y_center - (height / 2))
            x_max = int(x_min + width)
            y_max = int(y_min + height)

            cropped_image = img[int(y_min):int(y_max), int(x_min):int(x_max)]

            if not cropped_image.size:
                return None
        except TypeError as e:
            logger.info("x_center value > width / 2 value or y_center value >  height / 2 value")
            logger.error(f"Error in cropping: {e}")
            return img
        return cropped_image

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.relative_static_crop(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_RelativeCrop(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
