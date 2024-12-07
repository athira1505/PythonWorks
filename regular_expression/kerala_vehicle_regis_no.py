

# starting with KL
# 2digit
# alphabet min1 max2
# 4 digit

from re import fullmatch

user_input=input("enter registration no: ")

pattern="(KL)+[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")