

# lowercase
# starts with an alphabet
# numbers optional
# @gmail.com
# 64 character


from re import fullmatch

user_input=input("enter email: ")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")