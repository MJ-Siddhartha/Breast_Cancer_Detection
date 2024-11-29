# Breast Cancer Detection using AdaBoost Classifier

## Overview
This project implements a machine learning model to detect breast cancer using the AdaBoost classifier. The model classifies tumors as malignant or benign based on their features.  

## Features
- **AdaBoost Classifier**: Combines multiple weak learners to enhance prediction accuracy.  
- **Dataset**: Uses the Wisconsin Breast Cancer Dataset.  

## Technologies Used
- **Programming Language**: Python  
- **Libraries**:  
  - Scikit-learn  
  - Pandas  
  - NumPy  
  - Matplotlib/Seaborn (for visualization)
  - Streamlit (for deployment)
  - Joblib (for saving model)

## Dataset
- **Source**: [Wisconsin Breast Cancer Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)  
- **Features**: 30 numeric attributes including mean, standard error, and worst values for cell nucleus properties.  
- **Target**: Binary classification — `Malignant` (M) and `Benign` (B).  

## Workflow
1. **Data Collection**:
   - Taking data from the Wiscosin Dataset.
3. **Data Preprocessing**: 
   - Handling missing values, normalization, and encoding categorical labels, balancing classes.  
4. **Model Training**:  
   - AdaBoost trained on a split dataset with hyperparameter tuning.  
5. **Evaluation**:  
   - Metrics like accuracy, precision, recall, and F1-score.  
6. **Hyperparameter Tuning**:
   - Applying grid search for finding best parameters.
8. **Visualization**:
   - Confusion matrix, feature importance analysis and ROC curve.  

## Results
The AdaBoost classifier was evaluated using the Wisconsin Breast Cancer Dataset. Below are the performance metrics:
### Without Hyperparameter Tuning
- Accuracy: 97%
- Classification Report:
  
                  precision    recall  f1-score   support
  
            0         0.97      0.98      0.98       107
            1         0.97      0.95      0.96        64
  
      accuracy                            0.97       171
      macro avg       0.97      0.97      0.97       171
      weighted avg    0.97      0.97      0.97       171

### With Hyperparameter Tuning
- **Best Hyperparameters**:  
- `learning_rate`: 1.0  
- `n_estimators`: 200  
- **Best Score**: 97.8%  
- **Accuracy**: 98%  
- **Classification Report**:

                  precision    recall  f1-score   support
  
            0         0.96      1.00      0.98       107
            1         1.00      0.94      0.97        64
  
      accuracy                            0.98       171
      macro avg       0.98      0.98      0.97       171
      weighted avg    0.98      0.98      0.98       171

The model performed slightly better with hyperparameter tuning, achieving higher precision and recall for both classes.  

## Predictions
### UI
![image](https://github.com/user-attachments/assets/5db8d0d3-a0ad-4001-b6dc-498dc658dd28)
### Benign
![image](https://github.com/user-attachments/assets/cfade937-3984-4589-af7c-d947ba609729)
### Malignant
![image](https://github.com/user-attachments/assets/06339154-a0e6-41bd-a208-2278f6a6d02c)


