


# starting with an alphabet from p-t
# in second place must be a number that is \ by 3
# followed by any no alphabets,num,@


# s6abc


from re import fullmatch

user_input=input("enter the variable name:")

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")


