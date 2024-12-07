

def swap_dec(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper


def round_dec(fn):
    def wrapper(n1,n2):
        n1=round(n1)
        n2=round(n2)
        return fn(n1,n2)
    return wrapper


@round_dec
@swap_dec
def add_number(num1,num2):
    return num1+num2


@round_dec
@swap_dec
def sub(num1,num2):
    return num1-num2


@round_dec
@swap_dec
def div(num1,num2):
    return num1/num2


print(div(2,10))
print(add_number(2.5,3.6))
print(sub(2.8,12.2))