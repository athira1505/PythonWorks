


#   c1  c2  c3  c4  c5  
#1  *   *   *   *   *
#2  *   *   *   *
#3  *   *   *
#4  *   *
#5  *





for row in range(5,0,-1):
    for col in range(1,row+1):
        print("*",end="\t")
    print()