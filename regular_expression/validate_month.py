

# validate month 01-12
# dat 1 2 3 4 5 6 7 8 9
#     01 02 03 04 05 06 07 08 09
#     10 11 12


from re import fullmatch

user_input=input("enter month: ")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")