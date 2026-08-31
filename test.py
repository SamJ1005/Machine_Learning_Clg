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

# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# import matplotlib.pyplot as plt

# # Load data
# data = pd.read_csv("playtennis.csv")

# # Input and output
# X = data[["Outlook", "Temperature", "Humidity", "Wind"]].copy()
# Y = data["Play"]

# # Convert text into numbers
# for col in X.columns:
#     X[col] = LabelEncoder().fit_transform(X[col])

# Y = LabelEncoder().fit_transform(Y)

# # Create and train ID3 modela
# model = DecisionTreeClassifier(criterion="entropy")
# model.fit(X, Y)

# # Predictions
# print("Predictions:", model.predict(X))

# # Plot decision tree
# plot_tree(model, feature_names=X.columns)
# plt.show()

# import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# import matplotlib.pyplot as plt

# data = pd.read_csv("playtennis.csv")

# X = data[["Outlook", "Temperature", "Humidity", "Wind"]].copy()
# Y = data["Play"]
# encoders = {}

# for col in X.columns:
#     encoders[col] = LabelEncoder()
#     X[col] = encoders[col].fit_transform(X[col])

# output_encoder = LabelEncoder()
# Y = output_encoder.fit_transform(Y)

# model = DecisionTreeClassifier(criterion="entropy")
# model.fit(X, Y)
# print("Predictions:", model.predict(X))

# #Sample Data
# new_sample = pd.DataFrame({
#     "Outlook": ["Sunny"],
#     "Temperature": ["Cool"],
#     "Humidity": ["High"],
#     "Wind": ["Strong"]
# })

# for col in new_sample.columns:
#     new_sample[col] = encoders[col].transform(new_sample[col])

# prediction = model.predict(new_sample)
# result = output_encoder.inverse_transform(prediction)

# print("\nNew Sample:")
# print("Outlook     : Sunny")
# print("Temperature : Cool")
# print("Humidity    : High")
# print("Wind        : Strong")
# print("\n\nPredicted Class:", result[0])

# plt.figure(figsize=(12, 7))

# plot_tree(
#     model,
#     feature_names=X.columns,
#     class_names=output_encoder.classes_,
#     filled=True
# )

# plt.title("Decision Tree using ID3 Algorithm")
# plt.show()