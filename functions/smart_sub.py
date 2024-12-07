# create a fn smart_sub with 3 parameters num1,num2,reverse
# reverse takes boolean value
# if reverse==true then return num2-num1 else return num1-num2

def smart_sub(num1,num2,reverse):

    return num2-num1 if reverse==True else num1-num2

print(smart_sub(2,10,True))

print(smart_sub(2,10,False))