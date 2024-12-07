#begin
#end
#read frm user
#print all even no frm begin 2 end



begin=int(input("enter the starting limit:"))
end=int(input("enter the limit:"))

#10,.................,50
#begin,.............,end

if begin>end:
   begin,end=end,begin

i=begin

while(i<=end):
    if i%2==0:
     print(i)
    i=i+1