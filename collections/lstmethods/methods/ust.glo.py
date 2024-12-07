arr=[100,200,300,400,500,600,700,800]
#     0   1   2   3   4   5   6   7
#     i
# output
# result=[100,800,300,600,500,400,700,200]

odd_position_el=[arr[i] for i in range(0,len(arr)) if i%2!=0]     #odd_position_el=[num for index,num in enumerate(arr) if index%2!=0]

print(odd_position_el)
for i in range(1,len(arr),2):
    el=odd_position_el.pop()

    arr[i]=el

print(arr)


# enumerate(iterable)
# for index,num in enumerate(arr):
#     print(index,num)
    


# OR

left=1
right=len(arr)-1
if right%2==0:
   right-=1

while(left<right):
    arr[left],arr[right]=arr[right],arr[left]
    left+=2
    right-=2
print(arr)