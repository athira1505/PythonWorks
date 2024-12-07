

lst1=["apple","mango","onion","potato"]
#       0       1        2        3

lst2=[100,200]
#      0   1

# {"apple":100,"mango":200,"onion":1,"potato":2}

result={}
for i in range(0,len(lst2)):

    lst1_index_element=lst1[i]
    lst2_index_element=lst2[i]

    result[lst1_index_element]=lst2_index_element


balance_element=lst1[len(lst2):]
for index,element in enumerate(balance_element):
    result[element]=index+1
print(result)

