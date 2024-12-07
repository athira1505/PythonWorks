

num1=int(input("enter num1:"))

num2=int(input("enter num2:"))


max_num=max(num1,num2)   

for i in range(max_num,(num1*num2)+1,max_num):   # range start from max number and upto num*num2 and as step we use max_num
    if i%num1==0 and i%num2==0:
        print(i)
        break