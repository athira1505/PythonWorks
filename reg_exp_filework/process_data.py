
from re import findall

f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\reg_exp_filework\\data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

all_dares=findall(pattern,content)

for data in all_dares:
    print(data)