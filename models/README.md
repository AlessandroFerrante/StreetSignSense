<div  align="center">

# StreetSignSense: YOLO12 Models & Metrics

[![Ultralytics  8.3.229 ](https://img.shields.io/badge/Ultralytics-8.3.229-lightblue?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Ultralytics Github](https://img.shields.io/badge/Ultralytics-Github-darkgreen?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Ultralytics YOLO12](https://img.shields.io/badge/Ultralytics-YOLO12-8A2BE2?logo=ultralytics&logoColor=white)](https://github.com/sunsmarterjie/yolov12)

[![Python 3.11.13 ](https://img.shields.io/badge/Python-3.11.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch 2.6.0](https://img.shields.io/badge/PyTorch-2.6.0-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?)](LICENSE)
[![License](https://img.shields.io/badge/License-CC_BY_4.0-orange.svg?)](LICENSE)

[![Project-StreetSignSense](https://img.shields.io/badge/Project-StreetSignSense-007bff.svg)](https://github.com/AlessandroFerrante/StreetSignSense/)

[![GitHub Release](https://img.shields.io/badge/GitHub-StreetSignSenseY12n-181717?logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/releases)
[![GitHub Release](https://img.shields.io/badge/GitHub-StreetSignSenseY12s-181717?logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/releases)
[![GitHub Release](https://img.shields.io/badge/GitHub-StreetSignSenseY12m-181717?logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/releases)

[![Model-StreetSignSense](https://img.shields.io/badge/KaggleModel-StreetSignSenseY12n-20BEFF.svg?logo=kaggle&logoColor=white)](https://www.kaggle.com/models/ferrantealessandro/streetsignsensey12n/)
[![Model-StreetSignSense](https://img.shields.io/badge/KaggleModel-StreetSignSenseY12n-20BEFF.svg?logo=kaggle&logoColor=white)](https://www.kaggle.com/models/ferrantealessandro/streetsignsensey12s/)
[![Model-StreetSignSense](https://img.shields.io/badge/KaggleModel-StreetSignSenseY12n-20BEFF.svg?logo=kaggle&logoColor=white)](https://www.kaggle.com/models/ferrantealessandro/streetsignsensey12m/)

[![Model-StreetSignSense](https://img.shields.io/badge/HuggingFace-StreetSignSenseY12n-FFD21E.svg?logo=huggingface)](https://huggingface.co/AlessandroFerrante/StreetSignSenseY12s)
[![Model-StreetSignSense](https://img.shields.io/badge/KaggleModel-StreetSignSenseY12n-FFD21E.svg?logo=huggingface)](https://HuggingFace.co/AlessandroFerrante/StreetSignSenseY12s)
[![Model-StreetSignSense](https://img.shields.io/badge/HuggingFace-StreetSignSenseY12m-FFD21E.svg?logo=huggingface)](https://huggingface.co/AlessandroFerrante/StreetSignSenseY12m)

</div>

---

## 1. 📊 Comparative Analysis

Direct comparison between Nano (n), Small (s) and Medium (m) variants.

### 1.1 Aggregate Metrics

Overall performance on the validation set.

|                     Confronto mAP                     |                        Confronto P, R, F1 Score                        |
| :----------------------------------------------------: | :---------------------------------------------------------------------: |
| ![mAP Comparison](metrics/comparison_mAP_all_models.png) | ![Avg P-R-F1 Comparison](metrics/comparation_avgP_avgR_F1_all_models.png) |

### 1.2 Loss Curves during Training

Trend of training vs validation losses.

|                          Box Loss                          |                          Cls Loss                          |                          Dfl Loss                          |
| :---------------------------------------------------------: | :---------------------------------------------------------: | :---------------------------------------------------------: |
| ![Box Loss](metrics/ComparisonTrainValidBoxLossAllModels.png) | ![Cls Loss](metrics/ComparisonTrainValidClsLossAllModels.png) | ![Dfl Loss](metrics/ComparisonTrainValidDflLossAllModels.png) |

---

## 2. 🔬 Performance Detail by Model

### 2.1 🏎️ YOLO12 Nano (n)

*Optimized for Edge Computing and speed.*

* **Overview Results:**
  ![Results Nano](metrics/results_y12n.png)
* **Confusion Matrix:**
  ![Confusion Matrix Nano](metrics/confusion_matrix_normalized_n.png)

#### Detailed Curves (Nano)

|             Precision-Recall             |                 F1 Score                 |
| :---------------------------------------: | :---------------------------------------: |
| ![PR Curve Nano](metrics/BoxPR_curve_n.png) | ![F1 Curve Nano](metrics/BoxF1_curve_n.png) |
|            **Precision**            |             **Recall**             |
|  ![P Curve Nano](metrics/BoxP_curve_n.png)  |  ![R Curve Nano](metrics/BoxR_curve_n.png)  |

---

### 2.2 ⚖️ YOLO12 Small (s)

*Ideal balance between accuracy and performance.*

* **Overview Risultati:**
  ![Results Small](metrics/results_y12s.png)
* **Confusion Matrix:**
  ![Confusion Matrix Small](metrics/confusion_matrix_normalized_s.png)

#### Detailed Curves (Small)

|              Precision-Recall              |                  F1 Score                  |
| :----------------------------------------: | :----------------------------------------: |
| ![PR Curve Small](metrics/BoxPR_curve_s.png) | ![F1 Curve Small](metrics/BoxF1_curve_s.png) |
|            **Precision**            |              **Recall**              |
|  ![P Curve Small](metrics/BoxP_curve_s.png)  |  ![R Curve Small](metrics/BoxR_curve_s.png)  |

---

### 2.3 🎯 YOLO12 Medium (m)

*Maximum accuracy for in-depth analysis.*

* **Overview Results:**
  ![Results Medium](metrics/results_y12m.png)
* **Confusion Matrix:**
  ![Confusion Matrix Medium](metrics/confusion_matrix_normalized_m.png)

#### Detailed Curves (Medium)

|              Precision-Recall              |                  F1 Score                  |
| :-----------------------------------------: | :-----------------------------------------: |
| ![PR Curve Medium](metrics/BoxPR_curve_m.png) | ![F1 Curve Medium](metrics/BoxF1_curve_m.png) |
|             **Precision**             |              **Recall**              |
|  ![P Curve Medium](metrics/BoxP_curve_m.png)  |  ![R Curve Medium](metrics/BoxR_curve_m.png)  |

---

## 3. 📥 Download Templates (PyTorch Originals)

Templates can be downloaded via GitHub Release (.zip file) or via the Kaggle and Hugging Face platforms.

### YOLO12 Nano (n)

> Fast, lightweight, for Edge Computing.

[![GitHub Release](https://img.shields.io/badge/GitHub-Download_Nano_ZIP-181717?style=for-the-badge&logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/releases/download/1.0.0/streetsignsense_yolo12_nano_v1.0.0.zip)
[![Kaggle](https://img.shields.io/badge/Kaggle-Model_Nano-20BEFF?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/models/ferrantealessandro/streetsignsensey12n/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model_Nano-FFD21E?style=for-the-badge&logo=huggingface)](https://huggingface.co/AlessandroFerrante/StreetSignSenseY12n)

### YOLO12 Small (s)

> Balanced between speed and precision.

[![GitHub Release](https://img.shields.io/badge/GitHub-Download_Small_ZIP-181717?style=for-the-badge&logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/releases/download/1.0.0/streetsignsense_yolo12_small_v1.0.0.zip)
[![Kaggle](https://img.shields.io/badge/Kaggle-Model_Small-20BEFF?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/models/ferrantealessandro/streetsignsensey12s/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model_Small-FFD21E?style=for-the-badge&logo=huggingface)](https://huggingface.co/AlessandroFerrante/StreetSignSenseY12s)

### YOLO12 Medium (m)

> Maximum precision.

[![GitHub Release](https://img.shields.io/badge/GitHub-Download_Medium_ZIP-181717?style=for-the-badge&logo=github)](https://github.com/AlessandroFerrante/StreetSignSense/releases/download/1.0.0/streetsignsense_yolo12_medium_v1.0.0.zip)
[![Kaggle](https://img.shields.io/badge/Kaggle-Model_Medium-20BEFF?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/models/ferrantealessandro/streetsignsensey12m/)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Model_Medium-FFD21E?style=for-the-badge&logo=huggingface)](https://huggingface.co/AlessandroFerrante/StreetSignSenseY12m)

## 👨‍💻 Author

[Alessandro Ferrante](https://alessandroferrante.net)

Email: [github@alessandroferrante.net](mailto:github@alessandroferrante.net)
