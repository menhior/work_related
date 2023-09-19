import pandas as pd 
import numpy as np

df = pd.read_excel("file_name.xlsx")
#df['Length'] = df["Length"].str.split(":", expand=True)
df[['Hours', "Minutes", "Seconds"]] = df["Length"].str.split(":", expand=True)
df["Hours"] = df["Hours"].astype(int)
df["Minutes"] = df["Minutes"].astype(int)
df["Seconds"] = df["Seconds"].astype(int)
df = df.drop("Length", axis=1)
#print(df.head())
#print(df.info())
#print(df.head())
#df_grouped = df.groupby(by=["Household", 'Date'])['Hours', "Minutes", "Seconds"].sum()

df_grouped = df.groupby(by=["Household"])['Hours', "Minutes", "Seconds"].sum()
#print(len(np.where(df['Minutes'].ge(60), 1, 0)))
#df_grouped['Hours'] = df_grouped['Hours'] + np.where(df_grouped['Minutes'].ge(60), 1, 0)
#df_grouped['Minutes'] = df_grouped['Minutes'] - np.where(df_grouped['Minutes'].ge(60), 60, 0)
df_grouped['Hours'] = df_grouped['Hours'] + np.where(df_grouped['Minutes'].ge(60), 1, 0)
df_grouped['Minutes'] = df_grouped['Minutes'] - np.where(df_grouped['Minutes'].ge(60), 60, 0)
#df['Hours'] = df['Hours'] + 1
#df_grouped = df.groupby(by=["Household", 'Date'])["Length"].sum()
print(df_grouped)
#print(df_grouped.describe())

df_grouped.to_excel(r'file_1.xlsx')