
from re import finditer

text="abababbaab"
#     0123456789

pattern="ab"

matcher=finditer(pattern,text)  #[object(start,group),object(start,group),....]

for obj in matcher:
    print(obj.start(),obj.group())