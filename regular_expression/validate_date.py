


from re import fullmatch

user_input=input("enter date: ")

pattern="([1-31]|0[1-9]|1[0-9]|2[0-9]|3[0-1])"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")