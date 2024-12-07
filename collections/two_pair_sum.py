
#    i
#i   0 1 2 3
arr=[2,3,4,5]
#j   0 1 2 3
#      j


sum=int(input("enter sum:"))
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        cur_sum=arr[i]+arr[j]

        if sum==cur_sum:
            print(arr[i],arr[j])
            break




lst=[2,3,4,5]
# 12,11,10,9

left=0
right=len(lst)-1

sum=7

while(left<right):
    curr_sum=lst[left]+lst[right]   

    if curr_sum==sum:
        print(lst[left],lst[right]) 
        break
    
    elif curr_sum>sum:
        right-=1

    elif curr_sum<sum:
        left+=1

        







# sample input2
lsts=[3,6,7]
# 13,10,9





