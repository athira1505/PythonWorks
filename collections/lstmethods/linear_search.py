

arr=[2,4,6,3,8,7]
#    0 1 2 3 4 5

search_elements=int(input("enter no:"))

is_present=False

for i in range(0,len(arr)):
    if search_elements==arr[i]:
        is_present=True
        break

print(is_present)