import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("weather.csv")

X = data[["Temperature", "Humidity", "Wind"]]
Y = data["Play"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=1
)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

print("Actual:", list(Y_test))
print("Predicted:", list(Y_pred))
print("Accuracy:", model.score(X_test, Y_test))