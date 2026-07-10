#1
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

#2
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

#3
import pandas as pd

df = pd.read_csv("data.csv")

print("Rows and Columns:", df.shape)

#4
import pandas as pd

df = pd.read_csv("data.csv")

df_filtered = df[df["column_name"] > 10]

print(df_filtered)

#5
import pandas as pd

df = pd.read_csv("data.csv")

print(df.isnull().sum())

df = df.dropna()

print(df)

#6
import pandas as pd

df = pd.read_csv("data.csv")

print(df.groupby("category").mean(numeric_only=True))

#7
import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Sam","John","Raj"]
})

df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Marks":[90,85,95]
})

result = pd.merge(df1, df2, on="ID")

print(result)

#8
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

df["category"].value_counts().plot(kind="bar")

plt.show()

#9
import pandas as pd

df = pd.read_csv("data.csv")

df["date"] = pd.to_datetime(df["date"])

df["Month"] = df["date"].dt.month

print(df)

# 10
import pandas as pd

df = pd.read_csv("data.csv")

df.to_csv("output_data.csv", index=False)

print("File Saved")