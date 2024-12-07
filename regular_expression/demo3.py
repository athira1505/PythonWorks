
from re import finditer

text="I have 3 cars, 2 bike and 1 cycle"

# pattern="[a-zA-Z]"                       :   FOR ALPHABETS
# pattern="[0-9]"                          :   for digits
# pattern="[a-zA-Z0-9]"                    #   alphabets,digits no spcl characters
# pattern="[^ak]"                          #   exclude a and k
# pattern="[^akA-Z0-9 ]"                   #   all lower case alphabets exclude a,k : here in pattern after 9 leave a space so that in ans it excludes space also
# pattern="[^a-zA-Z0-9 ]"                  #   for spcl characters
# pattern="\w"                             #   "[a-zA-Z0-9]"    :  alphanumericals         
# pattern="\d"                             #   "[0-9]"          :  digits
# pattern="\D"                             #   "[^0-9]"         :  exclude digits
# pattern="\W"                             #   special characters
# pattern="\s"                             #   for space
pattern="\S"                               #   exclude space


matcher=finditer(pattern,text)

for obj in matcher:
    
    print(obj.start(), obj.group())