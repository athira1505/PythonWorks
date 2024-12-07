# read 3 numbers num1, num2, num3 print largest among three numbers


num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
num3=int(input("enter 3rd number:"))

if num1>=num2 and num1>=num3:
    print(f"{num1} is the largest number")

elif num2>=num1 and num2>=num3:
    print(f"{num2} is the largest number")

elif num3>=num1 and num3>=num2:
    print(f"{num3} is the largest number")

else:
    print(f"{num1} = {num2} = {num3} ")