

from re import fullmatch

user_input=input("enter driving license no: ")

pattern=""

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")