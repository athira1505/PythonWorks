
#   c1  c2  c3  c4  c5  c6 
#1  $
#2  $   $
#3  $   $   $
#4  $   $   $   $
#5  $   $   $   $   $
#6  $   $   $   $   $   $




for row in range(1,7):
    for col in range(1,row+1):
        print("$",end="\t")
    print()