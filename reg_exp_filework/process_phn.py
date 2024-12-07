
from re import fullmatch

f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\reg_exp_filework\\ph_no.txt")

for line in f:
    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher!=None:
        print(phone)