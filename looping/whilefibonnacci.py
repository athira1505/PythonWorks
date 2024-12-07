
num=int(input("enter the no: limit:"))
prev=0

current=1

print(prev)
print(current)
i=0

while(i<=num):
    next=prev+current
    print(next)

    prev=current
    current=next
    i=i+1