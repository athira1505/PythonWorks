



from re import fullmatch

user_input=input("enter year: ")

pattern="((18|19)[0-9]{2}|20[01][0-9]|202[0-4])"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")