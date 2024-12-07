

arr=[10,8,7,12,13,20,25]

search_el=int(input("enter the no:"))

is_present=False

arr.sort()

low=0
upp=len(arr)-1

while(low<=upp):

    mid=(low+upp)//2

    if search_el==arr[mid]:
        is_present=True
        break

    elif search_el<arr[mid]:
        upp=mid-1

    elif search_el>arr[mid]:
        low=mid+1

print(is_present)