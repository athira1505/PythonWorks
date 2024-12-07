# create a functin is_prime(num)

def is_prime(num):
    is_prime=True

    for i in range(2,num):
        if num%i==0:
            is_prime=False
    print(is_prime)
is_prime(6)