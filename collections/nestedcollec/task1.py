
arr=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
]

# print(isinstance("hello",str))     : to check strng
# print(isinstance(1,int))           :to check int

lst_obj=[item for item in arr if isinstance(item,list)]
print(lst_obj)

print(max(lst_obj,key=len))