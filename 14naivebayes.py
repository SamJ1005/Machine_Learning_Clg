import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("student.csv")

# Input and output
X = data[["Age", "StudyHours"]]
Y = data["Result"]

# Split data into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=0
)

# Create and train Naive Bayes model
model = GaussianNB()
model.fit(X_train, Y_train)

# Predict test data
Y_pred = model.predict(X_test)

# Display results
print("Actual:", list(Y_test))
print("Predicted:", list(Y_pred))
print("Accuracy:", accuracy_score(Y_test, Y_pred))

# Test a new sample
new = pd.DataFrame({"Age": [20], "StudyHours": [5]})
print("New Sample Result:", model.predict(new)[0])