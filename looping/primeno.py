

num=int(input("enter number:"))

is_prime=True

for i in range(2,num):          # 1 and the num is always a fact so here we check if there is any other factor other than 1 and num
    if num%i==0:
        is_prime=False 
        break
print(is_prime)


