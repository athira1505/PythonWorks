
arr=[100,200,300,400,500]

k=1
# rotate array k times   :  [500,100,200,300,400]
# rotate array k=2 times :  [400,500,100,200,300]

for i in range(1,k+1):
     
    pop_el=arr.pop()
    arr.insert(0,pop_el)

print(arr)