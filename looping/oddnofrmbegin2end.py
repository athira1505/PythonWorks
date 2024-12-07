begin=int(input("enter the starting limit:"))

end=int(input("enter the limit:"))


if begin>end:
    begin,end=end,begin


i=begin

while(i<=end):
    if i%2!=0:
        print(i)
    i=i+1