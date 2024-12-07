

#   c1  c2  c3  c4  c5  
#1  1
#2  2   2
#3  3   3   3
#4  4   4   4   4
#5  5   5   5   5   5





for row in range(1,6):
    for col in range(1,row+1):
        print(row,end="\t")
    print()