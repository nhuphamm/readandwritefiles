import csv
import pandas as pd

df = pd.read_csv("sales.csv")

dflist = ["SubTotal", "TaxAmt", "Freight"]

df["Total"] = df[dflist].sum(axis=1)
df1 = df.drop(["OrderDate", "ShipDate", "SubTotal", "TaxAmt", "Freight"], axis=1)
df2 = df1.groupby("CustomerID").sum()
print(df2)


df2.to_csv("salesreport.csv", index=True)
