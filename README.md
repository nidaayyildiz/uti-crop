# NOVAVISION Crop Package

A cropping package developed for **NOVAVISION**. This package provides static and dynamic cropping methods to be used in image processing pipelines.

## Executors

### 🔹 Absolute Crop Executor

- Crops the image using pixel-based coordinates.
- X and Y center points, along with width and height values, are provided in pixels.
- Designed for fixed-size cropping.

**Configs:**
- X Center Crop Pixel Size (`textInput`)
- Y Center Crop Pixel Size (`textInput`)
- Width Crop Pixel Size (`textInput`)
- Height Crop Pixel Size (`textInput`)

> Valid pixel value range: `1 < pixel size < 10000`

---

### 🔹 Dynamic Crop Executor

- Performs dynamic cropping based on detection results using bounding box coordinates.
- If there are multiple detections, the outputs are listed in JSON format.
- <img width="2053" height="1310" alt="image" src="https://github.com/user-attachments/assets/a6c95aa5-0e89-4733-b708-43849e80884b" />


---

### 🔹 Relative Crop Executor

- Performs ratio-based cropping depending on the size of the image.
- Suitable for cropping images of different sizes.

**Configs:**
- X Center Crop Ratio (`textInput`)
- Y Center Crop Ratio (`textInput`)
- Width Crop Ratio (`textInput`)
- Height Crop Ratio (`textInput`)

> Valid ratio value range: `0.0 < crop ratio < 1.0`

---

## 🛠️ Built With

- OpenCV  
- WSL  
- Redis
