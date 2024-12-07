#print all numbers from start to end

#read=start,end

start=int(input("enter the start no:"))

end=int(input("enter the end num:"))

if start<end: 

    for num in range(start,end+1,1):
         print(num)

else:
     for num in range(start,end-1,-1):
         print(num)
