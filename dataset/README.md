<div align="center">

# Street Sign Set
[![License](https://img.shields.io/badge/License-CCBY4.0-darkgreen.svg?)]([LICENSE](https://creativecommons.org/licenses/by/4.0/))
[![DOI](https://img.shields.io/badge/DOI-10.34740%2FKAGGLE%2FDS%2F8410752-blue)](https://doi.org/10.34740/KAGGLE/DS/8410752)

[![Kaggle](https://img.shields.io/badge/View_on-Kaggle-20BEFF?logo=kaggle)](https://www.kaggle.com/datasets/ferrantealessandro/street-sign-set)
[![Hugging Face](https://img.shields.io/badge/View_on-Hugging_Face-FFD21E?logo=huggingface)](https://huggingface.co/datasets/AlessandroFerrante/StreetSignSet)
[![Roboflow](https://img.shields.io/badge/View_on-Roboflow-purple?logo=Roboflow)](https://universe.roboflow.com/alessandros-workspace/street-sign-set-xzdde)

[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLO12-2596be?logo=ultralytics&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![Images](https://img.shields.io/badge/Images-%3E7.3k-success?style=flat&logo=image)](https://www.kaggle.com/datasets/ferrantealessandro/street-sign-set)
[![Annotations](https://img.shields.io/badge/Annotations-%3E12k-success?style=flat&logo=image&logoColor=blue)](https://www.kaggle.com/datasets/ferrantealessandro/street-sign-set)


[![Project-StreetSignSense](https://img.shields.io/badge/Project-StreetSignSense-007bff.svg)](https://github.com/AlessandroFerrante/StreetSignSense/)


### High-Quality Traffic Sign Detection Dataset

</div>

## 📂 Dataset Overview

**Street Sign Set** is a comprehensive dataset designed for road sign detection in realistic contexts. It serves as the foundation for the StreetSignSense project, enabling robust detection in diverse environmental conditions.

The dataset is not perfectly balanced, reflecting the real-world frequency where some signs appear much more often than others.

### 📊 Dataset Statistics

* **Total Images:** **> 7,300** images.
* **Classes:** **63** distinct classes.
* **Macro-Categories:** 5 (Priority, Prohibition, Information, Warning, Mandatory).
* **Format:** Standard YOLO annotations (`.txt`).

## 🏷️ Class Structure and Labels

The 63 classes are organized into **5 macro-categories** that define the label prefix:

1. **prio** (Priority) - e.g., `prio_give_way`, `stop`
2. **forb** (Prohibition) - e.g., `forb_speed_over_50`
3. **info** (Information) - e.g., `info_parking`
4. **warn** (Warning) - e.g., `warn_right_curve`
5. **mand** (Mandatory) - e.g., `mand_pass_left_right`

### Primary Targets (23 Main Classes)

The dataset focuses on 23 main classes identified as primary targets, including:

* **Speed limits:** 14 classes (e.g., 5–130 km/h).
* **Prohibition signs:** 4 classes (e.g., no stopping/parking, no overtaking).
* **Priority signs:** 2 classes (e.g., give way, stop).
* **Curves and crossings:** 3 classes (e.g., dangerous curves, pedestrian crossing).

## 🛠️ Hybrid Origin and Construction

This dataset is a result of a hybrid curation process:

* **Base:** ~4000 images sourced from existing Kaggle datasets.
* **Expansion:** ~3000 images manually integrated from external sources and street mapping services to cover underrepresented classes. These were manually labeled to ensure quality.

## ⚙️ Technical Specifications

* **Filename Scheme:** Rigorous logical scheme `class_name-n.jpg` (e.g., `prio_give_way-12.jpg`).
* **Selective Data Augmentation:** Applied **only** to rare classes to mitigate class imbalance. Techniques include:
  * Hue/Saturation/Brightness variations.
  * Grayscale (23% probability).
  * Blur and Noise simulation for adverse conditions.

## 📥 Download & Access

To keep the GitHub repository lightweight, the raw dataset is hosted on external platforms specialized for data versioning.



## 🖊️ Citation

If you use this dataset in your research, please cite it as follows:

```
@misc{alessandro_ferrante_2025,
    title={Street Sign Set},
    url={[https://www.kaggle.com/ds/8410752](https://www.kaggle.com/ds/8410752)},
    DOI={10.34740/KAGGLE/DS/8410752},
    publisher={Kaggle},
    author={Alessandro Ferrante},
    year={2025}
}
```

## 🗂️ Directory Structure

The dataset follows the standard YOLO directory structure required by Ultralytics:

```
StreetSignSense/
├── data.yaml          # Configuration file with class names and paths
├── train/
│   ├── images/        # Training images (.jpg/.png)
│   └── labels/        # Training labels (.txt)
├── valid/
│   ├── images/        # Validation images
│   └── labels/        # Validation labels
└── test/
    ├── images/        # Testing images
    └── labels/        # Testing labels
```


## 👨‍💻 Author

[Alessandro Ferrante](https://alessandroferrante.net)

Email: [github@alessandroferrante.net](mailto:github@alessandroferrante.net)