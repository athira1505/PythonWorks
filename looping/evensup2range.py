#read 2 limits
#sample input (1)





begin=int(input("enter the start:"))
end=int(input("enter the end:"))

i=begin

reverse=True if begin>end else False
print(reverse)


while(i<=end if reverse==False else i>=end):
    if i%2==0:
        print(i)

    if reverse==True:
        i=i-1

    else:
        i=i+1




