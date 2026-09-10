import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
data = pd.read_csv("iris.csv")

# Input and output
X = data[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
Y = data["Species"]

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=5
)

# KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)

# Prediction
Y_pred = model.predict(X_test)

# Print predictions
print("Correct Predictions:")
for actual, predicted in zip(Y_test, Y_pred):
    if actual == predicted:
        print("Actual:", actual, "Predicted:", predicted)

print("\nWrong Predictions:")
for actual, predicted in zip(Y_test, Y_pred):
    if actual != predicted:
        print("Actual:", actual, "Predicted:", predicted)