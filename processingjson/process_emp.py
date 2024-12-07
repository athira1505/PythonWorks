
from json import load

f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\emp.json")

data=load(f)

for emp in data:
    print(emp)
