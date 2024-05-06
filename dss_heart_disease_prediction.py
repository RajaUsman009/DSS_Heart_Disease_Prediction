# -*- coding: utf-8 -*-
"""DSS Heart Disease Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hfjLyzb1Ou96kpJLXZR12PXaHvOvv6Dc
"""
pip install scikit-learn
import pandas as pd

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Function to print a header with a title
def print_header(title):
    print("=" * 50)
    print(title)
    print("=" * 50)

# Function to get user input with a formatted prompt
def get_user_input(label):
    return input(f"{label}: ")

# Function to format and print prediction result in red or green color
def print_prediction(result):
    if "healthy" in result:
        print("\033[92m" + result + "\033[0m")  # Print in green color
    else:
        print("\033[91m" + result + "\033[0m")  # Print in red color



# Step 1: Load and Explore the Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
print_header("Step 1: Load and Explore the Dataset")
df = pd.read_csv('https://github.com/RajaUsman009/DSS_Heart_Disease_Prediction/blob/main/Heart_disease_cleveland_new.csv')
# Step 2: Reshape the DataFrame for multiple columns
# Example: Reshape multiple columns into a 2D DataFrame
column_names = ['chol', 'fbs', 'restecg','thalach','exang','oldpeak','slope','ca','thal']  # Specify the names of the columns to reshape
reshaped_df = df[column_names].values.reshape(-1, len(column_names))

# Step 3: Split the data into features and target
X = reshaped_df  # Features
y = df['target']  # Target variable
print(df.head())  # Display the first few rows
print(df.info())  # Display dataset information
df.head()

import pandas as pd

# Assuming 'df' is your DataFrame
# Change data type of columns from int64 to int32
int64_columns = df.select_dtypes(include='int64').columns
df[int64_columns] = df[int64_columns].astype('int32')

# Change data type of columns from float64 to int32
float64_columns = df.select_dtypes(include='float64').columns
df[float64_columns] = df[float64_columns].astype('int32')

print(df.info())  # Display dataset information

# Step 2: Preprocess the Data
print_header("Step 2: Preprocess the Data")
X = df.drop(columns=['target'])  # Features
y = df['target']  # Target variable

# Step 3: Train and Evaluate Different Models
print_header("Step 3: Train and Evaluate Different Models")
models = {
    "Random Forest": RandomForestClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "Support Vector Machine": SVC(random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Logistic Regression": LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

accuracies = []
model_names = []

for name, model in models.items():
    print_header(f"Training and Evaluating {name}")
    model_names.append(name)
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model performance
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f"Accuracy: {accuracy:.2f}")

# Step 4: Create Bar Graph of Model Accuracies
print_header("Step 4: Create Bar Graph of Model Accuracies")
plt.figure(figsize=(10, 6))
plt.bar(model_names, accuracies, color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Model Accuracies')
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.show()

# Step 5: Accept User Input and Make Predictions
print_header("Step 5: Accept User Input and Make Predictions")
user_input = {}
user_input['age'] = int(get_user_input("Enter age"))
user_input['sex'] = int(get_user_input("Enter sex (0 for female, 1 for male)"))
user_input['cp'] = int(get_user_input("Enter chest pain type (0, 1, 2, or 3)"))
user_input['trestbps'] = int(get_user_input("Enter resting blood pressure"))
user_input['chol'] = int(get_user_input("Enter serum cholesterol"))
user_input['fbs'] = int(get_user_input("Enter fasting blood sugar (0 or 1)"))
user_input['restecg'] = int(get_user_input("Enter resting electrocardiographic results (0, 1, or 2)"))
user_input['thalach'] = int(get_user_input("Enter maximum heart rate achieved"))
user_input['exang'] = int(get_user_input("Enter exercise induced angina (0 or 1)"))
user_input['oldpeak'] = float(get_user_input("Enter ST depression induced by exercise relative to rest"))
user_input['slope'] = int(get_user_input("Enter slope of the peak exercise ST segment (0, 1, or 2)"))
user_input['ca'] = int(get_user_input("Enter number of major vessels colored by fluoroscopy (0-3)"))
user_input['thal'] = int(get_user_input("Enter thalium stress result (1, 2, or 3)"))

print_header("Predicting Heart Disease")
best_model = models["Random Forest"]  # Choose the best model based on evaluation
prediction = best_model.predict([list(user_input.values())])
result = "The person is predicted to have heart disease." if prediction[0] == 1 else "The person is predicted to be healthy."
print_prediction(result)

import pickle

pickle.dump(models,open('/content/drive/MyDrive/RAJA@24/DSS_Model1', 'wb'))

model_loaded = pickle.load(open('/content/drive/MyDrive/RAJA@24/DSS_Model1','rb'))

import numpy as np

with open('/content/drive/MyDrive/RAJA@24/DSS_Model1', 'rb') as f:
    array = np.load(f, allow_pickle=True, dtype='float32')
