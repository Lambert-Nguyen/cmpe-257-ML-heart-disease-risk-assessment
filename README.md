# Heart Disease Risk Assessment: A Multi-Class Prediction Approach

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Project Overview

This project aims to predict heart disease severity levels (0-4) using machine learning algorithms. Rather than binary classification, we provide detailed risk assessment to help healthcare professionals make informed treatment decisions.

### Team Members
- **Lam Nguyen** - Data preprocessing and analysis lead
- **James Pham** - Model development and training lead
- **Le Duy Vu** - Web application development lead
- **Vi Thi Tuong Nguyen** - Evaluation and documentation lead

## 🎯 Problem Statement

Heart disease is the leading cause of death globally, responsible for ~32% of all deaths. This project addresses:
- Limited access to expensive diagnostic tests
- Need for severity-level prediction (not just binary yes/no)
- Resource constraints in smaller hospitals and developing regions

## 📊 Dataset

**Source:** [UCI Heart Disease Dataset (Kaggle)](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)

- **Size:** 920 patient records
- **Sources:** 4 medical centers (Cleveland, Hungary, Switzerland, Long Beach VA)
- **Features:** 14 clinical features
- **Target:** 5 classes (0-4 severity levels)

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
pip or conda
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/Lambert-Nguyen/cmpe-257-ML-heart-disease-risk-assessment.git
cd heart-disease-prediction
```

2. Create virtual environment
```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n heart-disease python=3.8
conda activate heart-disease
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

### Download Dataset
1. Go to [Kaggle Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)
2. Download the dataset
3. Place in `data/raw/` directory

## 📁 Project Structure
```
├── data/               # Data files (not tracked in git)
├── notebooks/          # Jupyter notebooks for exploration
├── src/               # Source code
├── models/            # Trained models
├── webapp/            # Web application
├── tests/             # Unit tests
└── results/           # Output results and figures
```

## 🔬 Methodology

### Models
- Random Forest
- XGBoost
- Support Vector Machines (SVM)
- Ensemble Methods

### Key Techniques
- Stratified K-Fold Cross-Validation (k=5)
- SMOTE for class imbalance
- Hyperparameter tuning via Grid Search
- Feature importance analysis

## 📈 Evaluation Metrics

**Primary Metric:** Weighted F1-Score
- Target: ≥75% overall
- Sensitivity: >90% for disease detection

**Additional Metrics:**
- Confusion matrices per severity level
- Precision and Recall per class
- ROC curves

## 🌐 Web Application

User-friendly interface for:
- Input clinical parameters
- Real-time risk assessment
- Severity level prediction
- Feature importance visualization

## 📝 Usage

### Training Models
```bash
python src/models/train.py --model random_forest --config config/config.yaml
```

### Running Web App
```bash
cd webapp
python app.py
```

## 🤝 Contributing

1. Create your feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 References

See `docs/project_proposal.pdf` for detailed references and methodology.

## 📧 Contact

For questions or suggestions, please open an issue or contact the team members.