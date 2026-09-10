import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("iris.csv")

X = data[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
y = data["Species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1
)

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Correct Predictions:")

for actual, predicted in zip(y_test, y_pred):
    if actual == predicted:
        print("Actual:", actual, "Predicted:", predicted)

print("\nWrong Predictions:")

for actual, predicted in zip(y_test, y_pred):
    if actual != predicted:
        print("Actual:", actual, "Predicted:", predicted)