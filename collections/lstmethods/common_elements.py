# commom elents without using in

arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]
counter=0

for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
        if arr1[i]==arr2[j]:
            counter+=1
            print(arr1[i])

print("counter",counter)






