

from re import fullmatch

user_input=input("enter aadhar no: ")

pattern="[0-9]{4}[0-9]{4}[0-9]{4}"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")