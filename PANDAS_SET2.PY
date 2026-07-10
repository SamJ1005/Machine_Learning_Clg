#-----Program 1-----
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["species"] = iris.target_names[iris.target]

print(df.head())

#-----Program 2-----
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["species"] = iris.target_names[iris.target]

result = df[(df["sepal length (cm)"] > 5) &
            (df["species"] == "setosa")]

print(result)

#-----Program 3-----
import pandas as pd

df = pd.read_csv("missing.csv")

df = df.fillna(df.mean(numeric_only=True))

print(df)

#-----Program 4-----
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["species"] = iris.target_names[iris.target]

print(df.groupby("species").agg(["mean","median","std"]))

#-----Program 5-----
import pandas as pd

students = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Sam","John","Raj"]
})

courses = pd.DataFrame({
    "ID":[1,2,3],
    "Course":["Python","AI","ML"]
})

result = pd.merge(students, courses, on="ID")

print(result)

#-----Program 6-----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Daily Return"] = df["Close"].pct_change()

print(df)

plt.plot(df["Date"], df["Close"])
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Stock Price")
plt.show()

#-----Program 7-----
import pandas as pd

df = pd.read_csv("sales.csv")

pivot = df.pivot_table(values="Sales",
                       index="Category",
                       columns="Month",
                       aggfunc="sum")

print(pivot)

#-----Program 8-----
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df.hist()

plt.show()

#-----Program 9-----
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Number":[4,9,16,25]
})

df["Square Root"] = df["Number"].apply(np.sqrt)

print(df)

#-----Program 10-----
import pandas as pd

df = pd.read_csv("category.csv")

result = pd.get_dummies(df, columns=["Color"])

print(result)
