def is_prim(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def is_palin(num):
    return str(num)==str(num)[::-1]

def smallest(n):
    while True:
        if is_palin(n) and is_prim(n):
            return n
        n+=1

n=int(input("enter no:"))
print(smallest(n))