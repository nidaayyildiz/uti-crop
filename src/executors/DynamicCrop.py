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
        self.mask_Opacity = self.request.get_param("KeepSide")
        self.image = self.request.get_param("inputImage")
        self.detections = self.request.get_param("inputDetections")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def crop_detections(self, image):
        if isinstance(image, list):
            image = image[0]

        last_crop = None

        for det in self.detections:
            bbox = det.get('boundingBox', {})
            top = int(bbox.get('top', 0))
            left = int(bbox.get('left', 0))
            height = int(bbox.get('height', 0))
            width = int(bbox.get('width', 0))

            y1, y2 = max(0, top), min(image.shape[0], top + height)
            x1, x2 = max(0, left), min(image.shape[1], left + width)

            cropped = image[y1:y2, x1:x2]
            last_crop = cropped

        return last_crop



    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        img.value = self.crop_detections(img.value)
        self.image = Image.set_frame(img=img, package_uID=self.request.model.uID, redis_db=self.redis_db)
        packageModel = build_response_DynamicCrop(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
