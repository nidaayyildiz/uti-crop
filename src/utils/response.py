
from sdks.novavision.src.helper.package import PackageHelper
from components.Crop.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor,AbsoluteCropOutputs, DynamicCropOutputs, RelativeCropOutputs, AbsoluteCropResponse, DynamicCropResponse, RelativeCropResponse, AbsoluteCrop, DynamicCrop, RelativeCrop, OutputImage


def build_response_AbsoluteCrop(context):
    outputImage = OutputImage(value=context.image)
    absoluteCropOutputs = AbsoluteCropOutputs(outputImage=outputImage)
    absoluteCropResponse = AbsoluteCropResponse(outputs=absoluteCropOutputs)
    absoluteCropExecutor = AbsoluteCrop(value=absoluteCropResponse)
    executor = ConfigExecutor(value=absoluteCropExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

def build_response_DynamicCrop(context):
    outputImage = OutputImage(value=context.image)
    dynamicCropOutputs = DynamicCropOutputs(outputImage=outputImage)
    dynamicCropResponse = DynamicCropResponse(outputs=dynamicCropOutputs)
    dynamicCropExecutor = DynamicCrop(value=dynamicCropResponse)
    executor = ConfigExecutor(value=dynamicCropExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel


def build_response_RelativeCrop(context):
    outputImage = OutputImage(value=context.image)
    relativeCropOutputs = RelativeCropOutputs(outputImage=outputImage)
    relativeCropResponse = RelativeCropResponse(outputs=relativeCropOutputs)
    relativeCropExecutor = RelativeCrop(value=relativeCropResponse)
    executor = ConfigExecutor(value=relativeCropExecutor)
    packageConfigs = PackageConfigs(executor=executor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel

