

def review(rating):

    if rating<0:
        raise Exception("too low")
    elif rating>10:
        raise Exception("too high")
    else:
        print("done")


try:
    review(12)
except Exception as e:
    print(e)

print("hello")
print("hai")