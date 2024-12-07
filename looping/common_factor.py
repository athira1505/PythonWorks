#common factor of 2 no


num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

# 16 and 24    :  [1,2,4,8]       => common factors{in case of 16 and 24 to find common factor we check only upto smaller no,ie,here upto 16}
# 12 and 24    :  [1,2,3,4,6,12]  => common factors
min_num=num1 if num1<num2 else num2

for i in range(1,min_num):
    if num1%i==0 and num2%i==0:
        print(i)