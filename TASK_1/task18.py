
def max(s):
    count=0
    bal_count=0

    for char in s:
        if char=='L':
            count+=1
        elif char=='R':
            count-=1

        if count==0:
            bal_count+=1

    return bal_count

s=input("enter string:")
print(max(s))
            
