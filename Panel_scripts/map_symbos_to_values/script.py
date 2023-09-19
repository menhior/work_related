import pandas as pd

df = pd.read_excel('file_name.xlsx')
df = df.replace('UNC -','100 -', regex=True)
df = df.replace('INV -','100 -', regex=True)
df = df.replace(['***'], 100)
df = df.replace(['NIL'], 0)
df = df.replace(['NF'], 0)
df = df.replace(['^REJ'], 0, regex=True)
df = df.replace(['NP'], 0)
df = df.replace(['NC'], 0)
df = df.astype(str)
#for value in df['29/03/2023'].values:
#	print(type(value))
#df = np.where(df, eval, df2_grouped['Minutes'])
#df = df.replace('^100 -', eval(df) ,regex=True)
def calculate_difference(row):
    parts = row.split('-')
    if len(parts) == 1:
        return int(parts[0])
    else:
        return int(parts[0]) - int(parts[1])

# Apply the function to the 'A' column of the dataframe
for col in df.columns:
    if col != "Home Number":
        df[col] = df[col].apply(lambda x: calculate_difference(x))

print(df)
df.to_excel(r'file_1.xlsx', index=False)
#print(df.dtypes)
#df = df.astype('int64')
#print(df.dtypes)
'''NIL=0
UNC-(value) = 100-(value)
*** = 100
NF=0
REJ = 0
NP=0
NC=0
INV-(value) = 100-(value)'''