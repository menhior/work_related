import pandas as pd
import numpy as np


xls = pd.ExcelFile('file_name.xlsx')
df1 = pd.read_excel(xls, 'Sheet_1')
df2 = pd.read_excel(xls, 'Sheet_2')

df1 = df1[["Household", "Length", 'Date']]
df2 = df2[["Household", "Length", 'Date']]

df1[['Hours', "Minutes", "Seconds"]] = df1["Length"].str.split(":", expand=True)
df1["Hours"] = df1["Hours"].astype(int)
df1["Minutes"] = df1["Minutes"].astype(int)
df1["Seconds"] = df1["Seconds"].astype(int)
df1 = df1.drop("Length", axis=1)

df1_grouped = df1.groupby(by=["Household", "Date"])['Hours', "Minutes", "Seconds"].sum()

df1_grouped['Hours'] = df1_grouped['Hours'] + np.where(df1_grouped['Minutes'].ge(60), df1_grouped['Minutes']//60, 0)
df1_grouped['Minutes'] = np.where(df1_grouped['Minutes'].ge(60), df1_grouped['Minutes']%60, df1_grouped['Minutes'])

print(df1_grouped)
print(df1_grouped.describe())

df2[['Hours', "Minutes", "Seconds"]] = df2["Length"].str.split(":", expand=True)
df2["Hours"] = df2["Hours"].astype(int)
df2["Minutes"] = df2["Minutes"].astype(int)
df2["Seconds"] = df2["Seconds"].astype(int)
df2 = df2.drop("Length", axis=1)

df2_grouped = df2.groupby(by=["Household", "Date"])['Hours', "Minutes", "Seconds"].sum()

df2_grouped['Hours'] = df2_grouped['Hours'] + np.where(df2_grouped['Minutes'].ge(60), df2_grouped['Minutes']//60, 0)
df2_grouped['Minutes'] = np.where(df2_grouped['Minutes'].ge(60), df2_grouped['Minutes']%60, df2_grouped['Minutes'])

print(df2_grouped)
print(df2_grouped.describe())

df1_grouped.to_excel(r'file_1.xlsx')
df2_grouped.to_excel(r'file_2.xlsx')