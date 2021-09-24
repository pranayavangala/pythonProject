import pandas as pd
import csv
df =open(r"C:\Users\Medisys\PycharmProjects\pythonProject\data1.csv")
#file = csv.reader(file)
df = pd.read_csv(df)

df[['datee','mnth']] = df.Date.str.split("-" , expand=True)

pajan = 0
pafeb = 0
pamar = 0

wdljan=0
wdlfeb=0
wdlmar=0
#this change for git hub
ha=0
ha1jan =0
ha1feb = 0
ha1mar =0
for i in range(0, len(df)):
    if (df.iloc[i]['LOB']=='PA' and df.iloc[i]['mnth']=="Jan" ):
        #print(df.iloc[i]["GWP"])
        pajan = pajan + df.iloc[i]["GWP"]
    if (df.iloc[i]['LOB']=='PA' and df.iloc[i]['mnth']=="Feb" ):
        pafeb += df.iloc[i]["GWP"]
    if (df.iloc[i]['LOB']=='PA' and df.iloc[i]['mnth']=="Mar" ):
        pamar += df.iloc[i]["GWP"]
        #WDL
    if (df.iloc[i]['LOB']=='WDL' and df.iloc[i]['mnth']=="Jan" ):
        #print(df.iloc[i]["GWP"])
        wdljan += df.iloc[i]["GWP"]
    if (df.iloc[i]['LOB']=='WDL' and df.iloc[i]['mnth']=="Feb" ):
        wdlfeb += df.iloc[i]["GWP"]
    if (df.iloc[i]['LOB']=='WDL' and df.iloc[i]['mnth']=="Mar" ):
        wdlmar += df.iloc[i]["GWP"]
        #HD1
    if (df.iloc[i]['LOB']=='HA1' and df.iloc[i]['mnth']=="Jan" ):
        #print(df.iloc[i]["GWP"])
        ha1jan += df.iloc[i]["GWP"]
    if (df.iloc[i]['LOB']=='HA1' and df.iloc[i]['mnth']=="Feb" ):
        ha1feb += df.iloc[i]["GWP"]
    if (df.iloc[i]['LOB']=='HA1' and df.iloc[i]['mnth']=="Mar" ):
        ha1mar += df.iloc[i]["GWP"]



data = {'Jan':[pajan,wdljan,ha1jan],
        'Feb':[pafeb,wdlfeb,ha1feb],
        'Mar':[pamar,wdlmar,ha1mar]}

ans = pd.DataFrame(data,index = ["Personal Accident","Travel Insurance","Home Insurance"])
ans = ans.rename_axis("GWP", axis="columns")
print(ans)