# print 1st 5 numbers in fibonacci series
# input:none
# output:0 1 1 2 3


prev=0

current=1

print(prev)
print(current)

for i in range(1,4):
    next=prev+current
    print(next)

    prev=current
    current=next
    