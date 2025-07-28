
from sdks.novavision.src.helper.package import PackageHelper
from components.Crop.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor,AbsoluteCropOutputs, DynamicCropOutputs, RelativeCropOutputs, AbsoluteCropResponse, DynamicCropResponse, RelativeCropResponse, AbsoluteCrop, DynamicCrop, RelativeCrop, OutputImage


def build_response_AbsoluteCrop(context):
    outputImage = OutputImage(value=context.image)
    absoluteCropOutputs = AbsoluteCropOutputs(outputImage=outputImage)
    absoluteCropResponse = AbsoluteCropResponse(outputs=absoluteCropOutputs)
    absoluteCrop = AbsoluteCrop(value=absoluteCropResponse)
    executor = ConfigExecutor(value=absoluteCrop)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_DynamicCrop(context):
    outputImage = OutputImage(value=context.image)
    dynamicCropOutputs = DynamicCropOutputs(outputImage=outputImage)
    dynamicCropResponse = DynamicCropResponse(outputs=dynamicCropOutputs)
    dynamicCrop = DynamicCrop(value=dynamicCropResponse)
    executor = ConfigExecutor(value=dynamicCrop)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel


def build_response_RelativeCrop(context):
    outputImage = OutputImage(value=context.image)
    relativeCropOutputs = RelativeCropOutputs(outputImage=outputImage)
    relativeCropResponse = RelativeCropResponse(outputs=relativeCropOutputs)
    relativeCrop = RelativeCrop(value=relativeCropResponse)
    executor = ConfigExecutor(value=relativeCrop)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

