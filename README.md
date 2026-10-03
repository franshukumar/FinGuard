# FinGuard

## Real-Time AI-Powered Financial Fraud Detection Platform

FinGuard is an AI-powered financial fraud detection platform that analyzes transaction data using machine learning and generates fraud probability, risk level, and automated decisions.

## Features

- Credit card fraud detection
- XGBoost-based classification
- Fraud probability prediction
- LOW / MEDIUM / HIGH risk classification
- APPROVE / REVIEW / BLOCK decisions
- FastAPI REST API
- PostgreSQL transaction storage
- Interactive Swagger API documentation
- Planned React monitoring dashboard
- Planned Kafka real-time transaction streaming

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- PostgreSQL
- SQLAlchemy
- React
- Apache Kafka
- Docker

## Machine Learning

Dataset:
Credit Card Fraud Detection Dataset

Transactions: 284,807

Fraud transactions: 492

The model was evaluated using:

- Precision
- Recall
- F1-score
- ROC-AUC
- PR-AUC

## API

### POST /predict

Example request:

```json
{
  "features": [
    0,
    -1.3598,
    -0.0727
  ]
}
The API returns:

```json
{
  "fraud_probability": 0.0001,
  "risk_level": "LOW",
  "decision": "APPROVE"
}
```

## Project Structure

```text
FinGuard/
├── backend/
│   ├── main.py
│   └── routes/
├── ml/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── risk_engine.py
├── data/
│   └── raw/
│       └── creditcard.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   └── 02_model.ipynb
├── venv/
├── requirements.txt
├── README.md
└── .gitignore
```

## Model Performance

The XGBoost model achieved the following results on the test set:

| Metric | Score |
|---|---:|
| ROC-AUC | 0.9816 |
| PR-AUC | 0.8800 |
| Fraud Precision | 91.9% |
| Fraud Recall | 80.6% |
| Fraud F1-Score | 85.9% |

These results are based on the project's current train-test split.

## Risk Engine

FinGuard converts the predicted fraud probability into a risk level and decision:

| Fraud Probability | Risk Level | Decision |
|---|---|---|
| < 0.30 | LOW | APPROVE |
| 0.30 – 0.69 | MEDIUM | REVIEW |
| ≥ 0.70 | HIGH | BLOCK |

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/FinGuard.git
cd FinGuard
```

### 2. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Start PostgreSQL

```bash
brew services start postgresql
```

### 5. Start FastAPI

```bash
uvicorn backend.main:app --reload
```

### 6. Open Swagger API documentation

Open:

```text
http://127.0.0.1:8000/docs
```

## Example Results

### Normal Transaction

```json
{
  "fraud_probability": 0.0001,
  "risk_level": "LOW",
  "decision": "APPROVE"
}
```

### Fraud Transaction

```json
{
  "fraud_probability": 0.9942,
  "risk_level": "HIGH",
  "decision": "BLOCK"
}
```

## Future Enhancements

- React-based fraud monitoring dashboard
- Real-time transaction processing using Apache Kafka
- SHAP-based fraud prediction explanations
- Transaction network and graph analysis
- Docker containerization
- Cloud deployment
- Advanced fraud alert and monitoring system

## Disclaimer

This project is developed for educational and demonstration purposes. The machine learning model is trained and evaluated on a public credit card fraud dataset and should not be considered a production financial fraud detection system without additional validation, security, monitoring, and regulatory considerations.