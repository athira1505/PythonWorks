

from re import finditer

f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\reg_exp_filework\\social_post.txt")

for line in f:
    line=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,line)

    for obj in matcher:
        print(obj.group())