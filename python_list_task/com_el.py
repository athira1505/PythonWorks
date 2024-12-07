

arr1=[2,3,6,9,86]

arr2=[86,3,7,1]

arr1.sort()
arr2.sort()

p1=0
p2=0

while(p1<=len(arr1)-1 and p2<=len(arr2)-1):
    if arr1[p1]==arr2[p2]:
        print(arr1[p1])
        p1+=1
        p2+=1

    elif arr1[p1]<arr2[p2]:
        p1+=1

    elif arr1[p1]>arr2[p2]:
        p2+=1 


