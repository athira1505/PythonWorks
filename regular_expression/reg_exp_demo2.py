
from re import finditer

text="fatcatrunveryfasttocaththerat"

matcher=finditer("at",text)

for obj in matcher:
    
    print(obj.start(),obj.group())