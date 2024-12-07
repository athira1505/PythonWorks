

from re import finditer

text="abbbababbabaaaab"
#     0123456789012345

# pattern="a{2}"
# pattern="a{1,3}"
pattern="a*"               # * any num including 0




matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),obj.group())