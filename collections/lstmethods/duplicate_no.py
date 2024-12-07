

arr=[1,2,2,3,2,1,4,5,3]

arr.sort()
duplicate_no=[]

for i in range (0,len(arr)-1):
    j=i+1

    result=arr[j]-arr[i]

    if result==0:
       if arr[i] not in duplicate_no:
           
          duplicate_no.append(arr[i])

print(duplicate_no)
        
