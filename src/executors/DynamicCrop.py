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
        self.mask_Opacity = self.request.get_param("MaskOpacity")
        self.image = self.request.get_param("inputImage")
        self.detections = self.request.get_param("outputDetections")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def dynamic_crop(self, img, detections):
        cropped_images = []

        for det in detections:
            x_min = int(det["left"])
            y_min = int(det["top"])
            x_max = int(x_min + det["width"])
            y_max = int(y_min + det["height"])

            cropped = img[y_min:y_max, x_min:x_max]
            if cropped.size:
                cropped_images.append(cropped)

        return cropped_images



    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.dynamic_crop(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.uID, redis_db=self.redis_db)
        packageModel = build_response_DynamicCrop(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()