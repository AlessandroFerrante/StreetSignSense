<div  align="center">

# StreetSignSense

### Real-Time Traffic Sign Detection

[![Python 3.11.13 ](https://img.shields.io/badge/Python-3.11.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch 2.6.0](https://img.shields.io/badge/PyTorch-2.6.0-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
![Linguaggio Principale](https://img.shields.io/github/languages/top/AlessandroFerrante/StreetSignSense)
![Dimensione Repository](https://img.shields.io/github/repo-size/AlessandroFerrante/StreetSignSense)

[![Dataset DOI](https://img.shields.io/badge/Dataset_DOI-10.34740%2FKAGGLE%2FDS%2F8410752-blue)](https://doi.org/10.34740/KAGGLE/DS/8410752)
[![Images](https://img.shields.io/badge/Images-%3E7.3k-success?style=flat&logo=image)](https://www.kaggle.com/datasets/ferrantealessandro/street-sign-set)
[![Annotations](https://img.shields.io/badge/Annotations-%3E12k-success?style=flat&logo=image&logoColor=blue)](https://www.kaggle.com/datasets/ferrantealessandro/street-sign-set)

[![Ultralytics  8.3.229 ](https://img.shields.io/badge/Ultralytics-8.3.229-lightblue?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Ultralytics Github](https://img.shields.io/badge/Ultralytics-Github-darkgreen?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Ultralytics YOLO12](https://img.shields.io/badge/Ultralytics-YOLO12-8A2BE2?logo=ultralytics&logoColor=white)](https://github.com/sunsmarterjie/yolov12)

[![TensorFlow.js](https://img.shields.io/badge/TensorFlow.js-Client_Side_ML-FF6F00?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/js)
[![ONNX](https://img.shields.io/badge/ONNX-Model_Exchange-005CED?logo=onnx&logoColor=white)](https://onnx.ai/)

[![HTML5](https://img.shields.io/badge/HTML5-Web_Demo-E34F26?logo=html5&logoColor=white)](https://alessandroferrante.github.io/StreetSignSense)
[![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?logo=javascript&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

[![GitHub Pages](https://img.shields.io/github/deployments/AlessandroFerrante/StreetSignSense/github-pages?label=GitHub%20Pages&logo=github&style=flat)](https://github.com/AlessandroFerrante/StreetSignSense/deployments)
[![Licenza](https://img.shields.io/badge/License-MIT-darkblue.svg?)](https://github.com/AlessandroFerrante/StreetSignSense/blob/main/LICENSE)
[![License](https://img.shields.io/badge/License-CC_BY_4.0-darkgreen.svg?)](LICENSE)

[![Kaggle](https://img.shields.io/badge/Kaggle-Visit_Profile-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/)
[![Model-StreetSignSense](https://img.shields.io/badge/HuggingFace-Visit_Profile-FFD21E.svg?logo=huggingface)](https://huggingface.co/AlessandroFerrante/)

[![Project-StreetSignSense](https://img.shields.io/badge/Project-StreetSignSense-007bff.svg)](https://github.com/AlessandroFerrante/StreetSignSense/)
[![Badge Report PDF](https://img.shields.io/badge/Report-Technical_Documentation-white?logo=pdf&logoColor=white)](https://alessandroferrante.github.io/StreetSignSense/docs/Report.pdf)

[![visitors](https://visitor-badge.laobi.icu/badge?page_id=AlessandroFerrante.StreetSignSense.readme&right_color=black)](https://github.com/AlessandroFerrante/StreetSignSense)
![Stelle](https://img.shields.io/github/stars/AlessandroFerrante/StreetSignSense?style=social)


**StreetSignSense** is a Machine Learning and Object Detection project focused on **real-time identification and classification of traffic signs**. The project explores the potential of executing Artificial Intelligence models directly in the browser (*client-side*) to ensure low latency, privacy, and high performance on edge devices.

## 🚀 Try Demo

The web application is entirely hosted on GitHub Pages and demonstrates the model's capabilities in a real and accessible environment.

### [**ACCESS**](https://alessandroferrante.github.io/StreetSignSense/demo/)

[![](https://alessandroferrante.github.io/StreetSignSense/demo/demo_interface.png)](https://alessandroferrante.github.io/StreetSignSense)

</div>

---

## 🔬 Project Architecture

The repository covers the entire Machine Learning lifecycle, structured into three critical phases:

### Training & Validation (Python/PyTorch)

Use of **Ultralytics YOLO** (12) for supervised training on a large-scale traffic sign dataset.

* **Engine:** PyTorch + Ultralytics
* **Dataset:** Kaggle (Identified via DOI)
* **Output:** High-precision `.pt` models (optimized mAP).

### Edge Inference (JavaScript/TF.js)

The heart of the innovation: running the model directly in the user's browser.

* **Framework:** TensorFlow.js with WebGL/WASM backend.
* **Logic:** Image pre-processing (resize, normalization) and Post-processing (Non-Maximum Suppression) implemented in pure ES6+ JavaScript.
* **Frontend:** Reactive interface for real-time video stream management (`getUserMedia`).

---

## ⚡️ Key Features

* **Zero-Latency Network:** Inference happens on-device (`Edge Computing`), eliminating network delays.
* **Privacy-First:** No video data ever leaves the user's device.
* **Cross-Platform:** Compatible with any device equipped with a modern browser (Chrome, Firefox, Safari, Edge).
* **Robustness:** Trained to handle variations in lighting, angles, and partial sign occlusions.

---

## 👨‍💻 Author

[Alessandro Ferrante](https://alessandroferrante.net)

Email: [github@alessandroferrante.net](mailto:github@alessandroferrante.net)
