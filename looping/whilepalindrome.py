


num=int(input("enter the number:"))
original=num
rev=0

while(num!=0):
    digit=num%10
    rev=rev*10+digit
    num=num//10

print("palindrome no" if rev==original else "not palindrome no")