import pandas as pd
from tabulate import tabulate
import csv
file =open(r"C:\Users\Medisys\PycharmProjects\pythonProject\Summarize.csv",)
#file = csv.reader(file)
file = pd.read_csv(file)
#print(file)

print("--------------")

"""
d = [ ["Personal Accident","","",""],
     ["Travel Insurance","","",""],
     ["Home Insurance", "","",""]]

print(tabulate(d, headers=["GWP", "Jan","feb", "march"]))
"""

PA = file[(file['LOB'] == 'PA')]
WDL = file[(file['LOB'] == 'WDL')]
HA1 = file[(file['LOB'] == 'HA1')]
sum=file["GROSS"].sum()
print("sum of the gross:-",sum)
print("----------------")
print("Personal Accident\n",PA["GROSS"])
sumofPA=PA["GROSS"].sum()
print("sum of PA:-",sumofPA)
print("Travel Insurance\n",WDL["GROSS"])
sumofWDL=WDL["GROSS"].sum()
print("sum of WDL:-",sumofWDL)
print("Home Insurance\n",HA1["GROSS"])
sumofHA1=HA1["GROSS"].sum()
print("sum of HA1:-",sumofHA1)
