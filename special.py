import pandas as pd
df=pd.read_csv("line1.csv")
print(df)
df.reset_index()
print(df)