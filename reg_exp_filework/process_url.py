

from re import fullmatch,finditer,findall

f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\reg_exp_filework\\url.txt")

content=f.read()

pattern="http?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:
    print(url)