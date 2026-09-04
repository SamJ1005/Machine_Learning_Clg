import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("calories.csv")

X = data[["Time"]]
Y = data["Calories"]

model = LinearRegression()
model.fit(X, Y)
Y_pred = model.predict(X)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Calories for 6 hours:",
      model.predict(pd.DataFrame({"Time": [6]}))[0])

# Plot graph
plt.scatter(X, Y)
plt.plot(X, Y_pred)
plt.xlabel("Time (hours)")
plt.ylabel("Calories")
plt.title("Simple Linear Regression")
plt.show()