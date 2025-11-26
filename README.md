### End-to-End Student Performance Prediction
[![Live Demo](https://img.shields.io/badge/demo-online-green.svg)](https://student-performance-predictor-m829.onrender.com/predictdata)

#### Project Overview
This project is a complete End-to-End Machine Learning application designed to predict student test scores based on various demographic and academic factors. It demonstrates a full lifecycle of a data science project, from data ingestion and exploratory data analysis (EDA) to model training, pipeline construction, and deployment via a Flask web application.


#### Tech Stack
*   **Language**: Python 3.8+
*   **Web Framework**: Flask
*   **Data Manipulation**: Pandas, NumPy
*   **Machine Learning**: Scikit-Learn, CatBoost, XGBoost
*   **Visualization**: Matplotlib, Seaborn
*   **Deployment**: GitHub Actions for CI/CD 

#### Project structure
```text
├── artifacts/          # Stores generated models and preprocessors (model.pkl, preprocessor.pkl)
├── notebook/           # Jupyter notebooks for EDA and model experimentation
├── src/
│   ├── components/     # Core modules for Ingestion, Transformation, and Training
│   ├── pipeline/       # Pipelines for Training and Prediction
│   ├── utils.py        # Utility functions (save/load objects, evaluate models)
│   ├── logger.py       # Logging configuration
│   └── exception.py    # Custom exception handling
├── templates/          # HTML templates for the Flask app
├── app.py              # Main Flask application entry point
├── requirements.txt    # Project dependencies
└── setup.py            # Package setup configuration
```

#### Setup

##### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mlproject.git
cd mlproject
```

##### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```bash
conda create -p venv python==3.8 -y
conda activate venv/
```

##### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

##### 4. Run the Application
Start the Flask server:
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.
