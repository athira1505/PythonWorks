
def lexicograhical(n):
    numbers=[str(i) for i in range(1,n+1)]
    numbers.sort()
    return [int(num) for num in numbers]

n=int(input("enter the number:"))
print("no in lexicographical order:",lexicograhical(n))