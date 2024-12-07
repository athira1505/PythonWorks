# create afn last_digit_max with 2 param num1,num2
# num1=123
# num2=872
# num1

def last_digit_max(num1,num2):
    digit1=num1%10
    digit2=num2%10

    print(num1 if digit1>digit2 else num2)
last_digit_max(123,872)