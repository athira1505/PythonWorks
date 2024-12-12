def is_additive_no(num):
    def is_valid_seq(num1,num2,remaining):
        while remaining:
            sum=str(num1+num2)
            if not remaining.startswith(sum):
                return False
            num1,num2=num2,int(sum)
            remaining=remaining[len(sum):]
        return True
    
    n=len(num)
    for i in range(1,n):
        for j in range(i+1,n):
            num1,num2=num[:i],num[i:j]
            if(len(num1)>1 and num1[0]=='0') or (len(num2)>1 and num[0]=='0'):
                continue
            if is_valid_seq(int(num1),int(num2),num[j:]):
                return True
    return False

print(is_additive_no("112358"))
print(is_additive_no("199100199"))
print(is_additive_no("1239"))