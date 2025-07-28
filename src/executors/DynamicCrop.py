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
from components.Crop.src.utils.response import build_response_DynamicCrop
from components.Crop.src.models.PackageModel import PackageModel


class DynamicCrop(Component):
    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.rotation_degree = self.request.get_param("Degree")
        self.keep_side = self.request.get_param("KeepSide")
        self.image = self.request.get_param("inputImage")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def dynamic_crop(img, detections):
        crops = []
        for det in detections:
            x1, y1, x2, y2 = map(int, det['bbox'])
            cropped = img[y1:y2, x1:x2]
            if cropped.size > 0:
                crops.append(cropped)
        return crops



    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.dynamic_crop(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_DynamicCrop(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()