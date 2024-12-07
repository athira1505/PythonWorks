


num=int(input("enter the number:"))

total=0

while(num!=0):
    digit=num%10
    digit_sq=digit**2  #**2 => exponential 2
    total=total+digit_sq
    num=num//10

print(total)