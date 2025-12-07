<div align="center">

# StreetSignSense Notebooks

[![Ultralytics  8.3.229 ](https://img.shields.io/badge/Ultralytics-8.3.229-lightblue?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Ultralytics Github](https://img.shields.io/badge/Ultralytics-Github-darkgreen?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Ultralytics YOLO12](https://img.shields.io/badge/Ultralytics-YOLO12-8A2BE2?logo=ultralytics&logoColor=white)](https://github.com/sunsmarterjie/yolov12)

[![Python 3.11.13 ](https://img.shields.io/badge/Python-3.11.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch 2.6.0](https://img.shields.io/badge/PyTorch-2.6.0-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?)](LICENSE)
[![License](https://img.shields.io/badge/License-CC_BY_4.0-orange.svg?)](LICENSE)

[![Project-StreetSignSense](https://img.shields.io/badge/Project-StreetSignSense-007bff.svg)](https://github.com/AlessandroFerrante/StreetSignSense/)
[![visitors](https://visitor-badge.laobi.icu/badge?page_id=AlessandroFerrante.StreetSignSense)](https://github.com/AlessandroFerrante/StreetSignSense)

[![GitHub Release](https://img.shields.io/badge/GitHub-View_StreetSignSenseYOLO12n-181717?logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/notebooks/)
[![GitHub Release](https://img.shields.io/badge/GitHub-View_StreetSignSenseYOLO12s-181717?logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/notebooks/)
[![GitHub Release](https://img.shields.io/badge/GitHub-View_StreetSignSenseYOLO12m-181717?logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/notebooks/)

[![Kaggle](https://img.shields.io/badge/Kaggle_Notebook-View_StreetSignSenseYOLO12n-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/streetsignsense-yolo12n)
[![Kaggle](https://img.shields.io/badge/Kaggle_Notebook-View_StreetSignSenseYOLO12s-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/streetsignsense-yolo12s)
[![Kaggle](https://img.shields.io/badge/Kaggle_Notebook-View_StreetSignSenseYOLO12m-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/streetsignsense-yolo12m)

### Training, Validation & Testing Pipelines

</div>

## 📖 Overview

This directory contains the Jupyter Notebooks used to train, validate, and test the **YOLO12** models (Nano, Small, Medium) on the  **Street Sign Set** .

Each notebook covers the end-to-end pipeline:

1. **Environment Setup:** Installation of Ultralytics and dependencies.
2. **Data Preparation:** Loading the dataset configuration.
3. **Training:** Training the YOLO12 architecture from pretrained weights.
4. **Validation:** Evaluating performance on the validation split.
5. **Inference:** Running predictions on test images.
6. **Analysis & Comparison:** In-depth model analysis and comparative metrics evaluation.

## 🧹 "Clean" vs "Executed" Versions

To ensure the GitHub repository remains lightweight and ensures clean diffs, the notebooks hosted here are **stripped of outputs** using `nbstripout`.

* **GitHub Version (Clean):** Contains only the code and markdown cells. Best for version control, code review, and cloning.
* **Kaggle Version (Full):** These are the executed kernels. They contain  **all outputs** , including training logs, loss curves, confusion matrices, and visualization of predictions.

## 🔗 Notebook Access

You can run the clean code locally or view the fully executed run on Kaggle.

| Model Variant                      | Source Code (GitHub)                                                      | Executed Kernel (Kaggle)                                                                                                                           |
| :--------------------------------- | :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **YOLO12 Nano**              | [`streetsignsense-yolo12n.ipynb`](./streetsignsense-yolo12n.ipynb)         | [![Kaggle](https://img.shields.io/badge/Kaggle-View_Kernel-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/streetsignsense-yolo12n) |
| **YOLO12 Small**             | [`streetsignsense-yolo12s.ipynb`](./streetsignsense-yolo12s.ipynb)         | [![Kaggle](https://img.shields.io/badge/Kaggle-View_Kernel-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/streetsignsense-yolo12s) |
| **YOLO12 Medium**            | [`streetsignsense-yolo12m.ipynb`](./streetsignsense-yolo12m.ipynb)         | [![Kaggle](https://img.shields.io/badge/Kaggle-View_Kernel-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/streetsignsense-yolo12m) |
| **Analysis & Metrics**       | [`yolo12modelanalysis.ipynb`](./yolo12modelanalysis.ipynb)                 | [![Kaggle](https://img.shields.io/badge/Kaggle-View_Kernel-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/yolo12modelanalysis)     |
| **Ground Truth Annotations** | [`sss-groundtruth-annotations.ipynb`](./sss-groundtruth-annotations.ipynb) | [![Kaggle](https://img.shields.io/badge/Kaggle-View_Kernel-20BEFF?logo=kaggle)](https://www.kaggle.com/code/ferrantealessandro/sss-groundtruth-annotations)                                                                                                                                |

## 🚀 How to Run

If you wish to run these notebooks:

* **Install Requirements:**
  In the requirements.txt file in this directory are all the necessary dependencies locked into the versions used during training.

```bash
pip install -r requirements.txt
```

## 👨‍💻 Author

[Alessandro Ferrante](https://alessandroferrante.net)

Email: [github@alessandroferrante.net](mailto:github@alessandroferrante.net)
