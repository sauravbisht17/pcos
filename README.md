# PCOS Prediction and Lifestyle Management

## Overview

This project aims to predict the likelihood of Polycystic Ovary Syndrome (PCOS) based on patient data and provide tailored lifestyle management advice. The project includes data ingestion, preprocessing, model training, prediction, and lifestyle advice generation. It leverages various technologies and services to ensure a robust and scalable solution.


## Technologies Used

- **Git**: For version control and collaboration.
- **GitHub Actions**: For CI/CD pipeline automation.
- **MLflow with Dagshub**: For experiment tracking and model management.
- **FastAPI**: For creating the prediction API.
- **Streamlit**: For creating the interactive web app.
- **Docker**: For containerizing the application.
- **AWS S3**: For storing artifacts and models.
- **AWS ECR**: For uploading Docker images.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Docker
- AWS CLI configured with appropriate permissions
- GitHub account
- Dagshub account

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/pcos-prediction.git
   cd pcos-prediction
