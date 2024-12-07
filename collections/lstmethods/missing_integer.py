arr=[1,2,5,4]
# find least +ve missing integer  :    2

# arr2=[1,2,3,5]
# least +ve missig integer

arr.sort()

for i in range (0,len(arr)-1):
    j=i+1

    result=arr[j]-arr[i]

    if result!=1:
        print(arr[i]+1,"missing")
        break


