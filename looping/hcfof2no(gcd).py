# GCD/HCF of 2 no


num1=int(input("enter num1:"))

num2=int(input("enter num2:"))

gcd=1  #1 is always a factor so we initializee gcd=1 and not as gcd=0

min_num=num1 if num1<num2 else num2    # OR to find min num use   min_num=min(num1,num2)

for i in range(1,min_num+1):
    if num1%i==0 and num2%i==0:
        gcd=i #we need only the highest value so we store that value in gcd

print(gcd)