# End-to-End Student Performance Prediction

## 📌 Project Overview
This project is a complete End-to-End Machine Learning application designed to predict student test scores based on various demographic and academic factors. It demonstrates a full lifecycle of a data science project, from data ingestion and exploratory data analysis (EDA) to model training, pipeline construction, and deployment via a Flask web application.

The goal is to provide a robust and modular codebase that allows for easy experimentation with different regression models and preprocessing techniques.

## 🚀 Features
*   **Modular Architecture**: Code is organized into distinct components (Data Ingestion, Transformation, Model Training) for maintainability and scalability.
*   **Automated Pipelines**: Implements `DataTransformation` and `ModelTrainer` pipelines to streamline the workflow.
*   **Multi-Model Comparison**: Automatically trains and evaluates multiple regression models (Random Forest, Decision Tree, XGBoost, CatBoost, AdaBoost, etc.) to select the best performer.
*   **Web Interface**: A user-friendly Flask web application that allows users to input data and receive real-time predictions.
*   **Robust Error Handling & Logging**: Custom exception handling and logging mechanisms to ensure smooth execution and easy debugging.

## 🛠️ Tech Stack
*   **Language**: Python 3.8+
*   **Web Framework**: Flask
*   **Data Manipulation**: Pandas, NumPy
*   **Machine Learning**: Scikit-Learn, CatBoost, XGBoost
*   **Visualization**: Matplotlib, Seaborn
*   **Deployment**: AWS Elastic Beanstalk (Ready) / Docker

## 📂 Project Structure
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

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mlproject.git
cd mlproject
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.
```bash
conda create -p venv python==3.8 -y
conda activate venv/
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask server:
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.

## 🧠 Model Training Pipeline
To retrain the model with new data:
1.  Ensure your dataset is in the correct format.
2.  Run the data ingestion script (which triggers transformation and training):
    ```bash
    python src/components/data_ingestion.py
    ```
    *This will process the data, train multiple models, select the best one based on R2 score, and save the artifacts (`model.pkl`, `preprocessor.pkl`).*

## 📊 Usage
1.  Navigate to the home page.
2.  Click on "Predict your Data".
3.  Fill in the form with student details (Gender, Ethnicity, Parental Education, etc.).
4.  Submit the form to see the predicted Math Score.

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## 📝 License
This project is licensed under the MIT License.
