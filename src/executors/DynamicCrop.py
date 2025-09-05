import os
import cv2
import sys
import copy

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
        self.image = self.request.get_param("inputImage")
        self.detections = self.request.get_param("inputDetections")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def crop_detections(self, image):
        images = []
        frame = image.value

        for det in self.detections:
            bbox = det.get('boundingBox', {})
            top = int(bbox.get('top', 0))
            left = int(bbox.get('left', 0))
            height = int(bbox.get('height', 0))
            width = int(bbox.get('width', 0))

            y1 = max(0, top)
            y2 = min(frame.shape[0], top + height)
            x1 = max(0, left)
            x2 = min(frame.shape[1], left + width)

            cropped_frame = frame[y1:y2, x1:x2]

            cropped_image = copy.deepcopy(image)
            cropped_image.value = cropped_frame

            saved_image = Image.set_frame(img=cropped_image, package_uID=self.request.model.uID, redis_db=self.redis_db)
            images.append(saved_image)

        return images

    def run(self):
        img = Image.get_frame(img=self.image, redis_db=self.redis_db)
        cropped_images = self.crop_detections(img)

        # Eğer hiç detection yoksa, orijinal görüntüyü döndür
        if not cropped_images:
            cropped_images = [img]

        # liste olarak döndür
        if len(cropped_images) == 1:
            self.image = cropped_images[0]
        else:
            self.image = cropped_images

        self.request.model.inputImage = self.image
        packageModel = build_response_DynamicCrop(context=self)
        return packageModel

if "__main__" == __name__:
    Executor(sys.argv[1]).run()
