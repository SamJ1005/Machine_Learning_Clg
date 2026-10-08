import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

data = pd.read_csv("playtennis.csv")
X = data[["Outlook", "Temperature", "Humidity", "Wind"]].copy()
Y = data["Play"]

encoders = {}
for col in X.columns:
    encoders[col] = LabelEncoder()
    X[col] = encoders[col].fit_transform(X[col])

Y = LabelEncoder().fit_transform(Y)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, Y)
print("Predictions:", model.predict(X))

new_sample = pd.DataFrame({
    "Outlook": ["Sunny"],
    "Temperature": ["Cool"],
    "Humidity": ["High"],
    "Wind": ["Strong"]
})

for col in X.columns:
    new_sample[col] = encoders[col].transform(new_sample[col])

prediction = model.predict(new_sample)

print("\nNew Sample:")
print("Sunny, Cool, High, Strong")
print("Predicted Class:", "Yes" if prediction[0] == 1 else "No")

plt.figure(figsize=(12, 7))
plot_tree(model, feature_names=X.columns,
          class_names=["No", "Yes"], filled=True)
plt.title("ID3 Decision Tree")
plt.show()