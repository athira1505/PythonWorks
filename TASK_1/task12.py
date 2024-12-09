def is_ugly_no(n):
    if n<=0:
        return False
    
    for factor in [2,3,5]:
        while n%factor==0:
            n//=factor

    return n==1

print(is_ugly_no(6))
print(is_ugly_no(1))
print(is_ugly_no(14))