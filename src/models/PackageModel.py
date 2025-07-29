
from pydantic import Field, validator
from typing import List, Optional, Union, Literal
from sdks.novavision.src.base.model import Package,Detection, Image, Inputs, Configs, Outputs, Response, Request, Output, Input, Config


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class InputDetections(Input):
    name: Literal["inputDetections"] = "inputDetections"
    value: List[Detection]
    type: str = "list"

    class Config:
        title = "Detections"

class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image],Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get('value')
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"

class XCenterAbsolute(Config):
    """
         The starting point of the crop as the horizontal distance from the left side of the image (in pixels).
    """
    name: Literal["xCenterAbsolute"] = "xCenterAbsolute"
    value: float = Field(ge=1, le=10000 ,default=50)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[1, 10000]"] = "[1, 10000]"

    class Config:
        title = "Crop Pixel Size (X - Center)"


class YCenterAbsolute(Config):
    """
         The starting point of the crop as the vertical distance from the top of the image (in pixels).
    """
    name: Literal["yCenterAbsolute"] = "yCenterAbsolute"
    value: float = Field(ge=1, le=10000 ,default=50)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[1, 10000]"] = "[1, 10000]"

    class Config:
        title = "Crop Pixel Size (Y - Center)"


class WidthAbsolute(Config):
    """
         The width of the region to be cropped (in pixels).
    """
    name: Literal["widthAbsolute"] = "widthAbsolute"
    value: float = Field(ge=1, le=10000 ,default=50)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[1, 10000]"] = "[1, 10000]"

    class Config:
        title = "Crop Pixel Size (Width)"


class HeightAbsolute(Config):
    """
         The height of the region to be cropped (in pixels).
    """
    name: Literal["heightAbsolute"] = "heightAbsolute"
    value: float = Field(ge=1, le=10000 ,default=50)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[1, 10000]"] = "[1, 10000]"

    class Config:
        title = "Crop Pixel Size  (Height)"

class MaskValue(Config):
    """
            Determines how much of the area outside the mask will be removed. 1.0 means fully removed, 0.0 means no removal. Use a value between 0.0 < mask value < 1.0 for partial transparency.
    """
    name: Literal["maskValue"] = "maskValue"
    value: float = Field(ge=0.0, le=1.0 ,default=0.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Mask Value"

class MaskOpacityFalse(Config):
    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class MaskOpacityTrue(Config):
    name: Literal["True"] = "True"
    maskValue: MaskValue
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class MaskOpacity(Config):
    """
        Mask opacity configuration with enable/disable options.
    """
    name: Literal["maskOpacity"] = "maskOpacity"
    value: Union[MaskOpacityTrue, MaskOpacityFalse]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Mask Opacity"


class XCenterRelative(Config):
    """
         Center X of the static crop (relative coordinate 0.0–1.0).
    """
    name: Literal["xCenterRelative"] = "xCenterRelative"
    value: float = Field(ge=0.0, le=1.0 ,default=0.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[0.0,1.0]"] = "[0.0, 1.0]"

    class Config:
        title = "Crop Ratio (X - Center)"


class YCenterRelative(Config):
    """
         Center Y of the static crop (relative coordinate 0.0–1.0).
    """
    name: Literal["yCenterRelative"] = "yCenterRelative"
    value: float = Field(ge=0.0, le=1.0 ,default=0.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[0.0,1.0]"] = "[0.0, 1.0]"

    class Config:
        title = "Crop Ratio (Y - Center)"


class WidthRelative(Config):
    """
         Width of the static crop (relative value 0.0–1.0).
    """
    name: Literal["widthRelative"] = "widthRelative"
    value: float = Field(ge=0.0, le=1.0 ,default=0.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[0.0,1.0]"] = "[0.0, 1.0]"

    class Config:
        title = "Crop Ratio (Width)"


class HeightRelative(Config):
    """
         Height of the static crop (relative value 0.0–1.0).
    """
    name: Literal["heightRelative"] = "heightRelative"
    value: float = Field(ge=0.0, le=1.0 ,default=0.5)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[0.0,1.0]"] = "[0.0, 1.0]"

    class Config:
        title = "Crop Ratio (Height)"



class AbsoluteCropInputs(Inputs):
    inputImage: InputImage


class AbsoluteCropConfigs(Configs):
    xCenterAbsolute: XCenterAbsolute
    yCenterAbsolute: YCenterAbsolute
    widthAbsolute: WidthAbsolute
    heightAbsolute: HeightAbsolute


class AbsoluteCropOutputs(Outputs):
    outputImage: OutputImage


class AbsoluteCropRequest(Request):
    inputs: Optional[AbsoluteCropInputs]
    configs: AbsoluteCropConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class AbsoluteCropResponse(Response):
    outputs: AbsoluteCropOutputs


class AbsoluteCropExecutor(Config):
    name: Literal["AbsoluteCrop"] = "AbsoluteCrop"
    value: Union[AbsoluteCropRequest, AbsoluteCropResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "AbsoluteCrop"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }



class DynamicCropInputs(Inputs):
    inputImage: InputImage
    inputDetections: InputDetections


class DynamicCropConfigs(Configs):
    maskOpacity: MaskOpacity


class DynamicCropOutputs(Outputs):
    outputImage: OutputImage


class DynamicCropRequest(Request):
    inputs: Optional[DynamicCropInputs]
    configs: DynamicCropConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class DynamicCropResponse(Response):
    outputs: DynamicCropOutputs


class DynamicCropExecutor(Config):
    name: Literal["DynamicCrop"] = "DynamicCrop"
    value: Union[DynamicCropRequest, DynamicCropResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "DynamicCrop"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }




class RelativeCropInputs(Inputs):
    inputImage: InputImage


class RelativeCropConfigs(Configs):
    xCenterRelative: XCenterRelative
    yCenterRelative: YCenterRelative
    widthRelative: WidthRelative
    heightRelative: HeightRelative


class RelativeCropOutputs(Outputs):
    outputImage: OutputImage


class RelativeCropRequest(Request):
    inputs: Optional[RelativeCropInputs]
    configs: RelativeCropConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class RelativeCropResponse(Response):
    outputs: RelativeCropOutputs


class RelativeCropExecutor(Config):
    name: Literal["RelativeCrop"] = "RelativeCrop"
    value: Union[RelativeCropRequest, RelativeCropResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "RelativeCrop"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[AbsoluteCropExecutor, DynamicCropExecutor, RelativeCropExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Task"


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["Crop"] = "Crop"
