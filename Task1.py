
import pandas as pd


df1 = pd.read_excel(r'C:\Users\Medisys\Downloads\Python&Excel_Assesment.xlsx', 'DataSet')
df2 = pd.read_excel(r'C:\Users\Medisys\Downloads\Python&Excel_Assesment.xlsx', 'DataSet2')
print(df1)
print(df2)

#f1 = pandas.read_excel("registration details.xlsx")
#f2 = pandas.read_excel("exam results.xlsx")

# merging the files
df3 = df1[["name","Id_a","Id_b","startDay","startTime","endDay","endTime","ablePri2AxlesAuto"]]\
    .merge(df2[["name","Id_a","Id_b","startDay","startTime","endDay","endTime","ablePri2AxlesAuto"]],on="name",how="left")

df3.to_excel("C:\\Users\\Medisys\\Documents\\output.xlsx", index=False)
print(df3)

