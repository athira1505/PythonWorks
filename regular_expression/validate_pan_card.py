
# 3 alphabet
# 4th place alphabet [PCAFHT]
# 1alphabet
# 4 digit
# 1 alphabet



from re import fullmatch

user_input=input("enter pan no: ")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")