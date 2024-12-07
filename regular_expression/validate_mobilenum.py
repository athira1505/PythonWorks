

# rule 10 digits
# validate mobile num

from re import fullmatch

user_input=input("enter mobile no:")

pattern="(91)?[0-9]{10}"            #(91)?  :  country code 91 optional              (91)+  : country code 91 is mandatory

matcher=fullmatch(pattern,user_input)   #None

if matcher==None:
    print("invalid")

else:
    print("valid")