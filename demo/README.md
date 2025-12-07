<div align="center">

# 🌐 StreetSignSense Web Demo

[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![TensorFlow.js](https://img.shields.io/badge/TensorFlow.js-Client_Side_ML-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/js)

[![HTML5](https://img.shields.io/badge/HTML5-Web_Demo-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
[![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![ONNX](https://img.shields.io/badge/ONNX-Model_Exchange-005CED?logo=onnx&logoColor=white)](https://onnx.ai/)

[![GitHub Pages](https://img.shields.io/github/deployments/AlessandroFerrante/StreetSignSense/github-pages?label=GitHub%20Pages&logo=github&style=flat)](https://github.com/AlessandroFerrante/StreetSignSense/deployments)
[![License](https://img.shields.io/badge/License-MIT-green.svg?)](LICENSE)

[![Project-StreetSignSense](https://img.shields.io/badge/Project-StreetSignSense-007bff.svg)](https://github.com/AlessandroFerrante/StreetSignSense/)
[![visitors](https://visitor-badge.laobi.icu/badge?page_id=AlessandroFerrante.StreetSignSense)](https://github.com/AlessandroFerrante/StreetSignSense)
### Real-Time Client-Side Inference with TensorFlow.js

### 🚀 Live Demo Available

#### [👉 Click here to try StreetSignSense directly in your browser](https://www.google.com/search?q=https://alessandroferrante.github.io/StreetSignSense "null")

*(No installation required)*


![alt text](../../demo_interface.png)

</div>



## 📖 Overview
This directory contains the core assets and logic for the StreetSignSense Web Demo.

The application runs entirely in the browser using TensorFlow.js, leveraging the client's GPU (via WebGL) to perform real-time object detection without sending data to a backend server.

### ✨ Key Features

* **Real-Time Detection:** Inference on webcam video streams.
* **Image Analysis:** Drag-and-drop static image detection.
* **Privacy First:** No data leaves the user's device.
* **Adjustable Thresholds:** Dynamic control over Confidence and IoU (NMS) thresholds.

## 📂 Directory Structure

```
demo/
└── assets/
    ├── css/           # Stylesheets for the UI
    ├── js/            # Core application logic
    │   └── index.js   # Main script (Model loading, Pre/Post-processing, NMS)
    ├── models/        # Converted YOLO12 models (TF.js format)
    └── images/        # Sample images for testing

```

## 🧠 Model Conversion (PyTorch → TF.js)

The models located in `assets/models/` are **not** the original PyTorch weights (`.pt`). They have been exported to ONNX and then converted to the **TensorFlow.js Graph Model** format (`model.json` + binary shards).

This conversion ensures the models are optimized for browser execution.

| **Variant** | **Path**                        | **Description**                    |
| ----------------- | ------------------------------------- | ---------------------------------------- |
| **Nano**    | `assets/models/yolov12n_web_model/` | Fastest, lowest latency.                 |
| **Small**   | `assets/models/yolov12s_web_model/` | Balanced performance.                    |
| **Medium**  | `assets/models/yolov12m_web_model/` | Higher accuracy, requires more GPU resources. |

> **Note:** For original `.pt` models see [here](https://github.com/AlessandroFerrante/StreetSignSense//tree/main/models)
## 🚀 How to Run Locally

Due to browser security restrictions (CORS - Cross-Origin Resource Sharing), **you cannot simply double-click `index.html`** to run this demo. It must be served via a local HTTP server.


## ⚙️ Technical Details

* **Input Resolution:** Models are typically exported at `640x640`. The JS logic handles aspect-ratio preserving resizing (letterboxing).
* **Post-Processing:** The raw output from the model is decoded in `main.js`, applying Non-Maximum Suppression (NMS) to remove duplicate bounding boxes.

## 👨‍💻 Author

[Alessandro Ferrante](https://alessandroferrante.net)

Email: [github@alessandroferrante.net](mailto:github@alessandroferrante.net)