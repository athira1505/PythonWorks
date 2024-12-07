num=int(input("enter the num:"))

if num%15==0:
    print("FizzBuzz")

elif num%5==0:
    print("Buzz")

elif num%3==0:
    print("Fizz")

else:
    print("invalid number")