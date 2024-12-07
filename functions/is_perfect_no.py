def is_perfect_number(num):


    total=0

    for i in range(1,num):
     if num%i==0:
        total=total+i
        return total==num
print(is_perfect_number(6))

