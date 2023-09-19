import pandas as pd

df_1 = pd.read_excel('file1.xls')
df_2 = pd.read_excel('file2.xls')

df_1_values = df_1['Home No.'].values
df_2_values = df_2['Home No.'].values


repeat_offenders_list = []

for value in df_1_values:
	if value in df_2_values:
		repeat_offenders_list.append(value)

print(repeat_offenders_list)