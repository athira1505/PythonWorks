arr1=[9,7,8,4]

arr2=[89.4,2,7]


def merge_lst(arr1,arr2):

    new_arr=arr1+arr2
    new_arr.sort()
    return new_arr

print(merge_lst(arr1,arr2))