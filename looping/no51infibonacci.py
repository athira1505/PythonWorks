# num=51
# is 51 in fibonacci series?

num=int(input("enter the number:"))

prev=0

current=1

is_fibo=False

for i in range(1,num+1):
    next=prev+current
    

    prev=current
    current=next
    
    if next==num:
        is_fibo=True
        break

print(is_fibo)