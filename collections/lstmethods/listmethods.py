# class list:
#       def append(self)                     #insert new element at the end
#       def pop(self)                        #remove last obj from list
#       def insert(self,index,object)
#       def index(self,object)
#       def copy(self)
#       def sort()

col=["red","green","yellow","violet","purple"]
#      0      1      2        3        4

col.append("blue")
print(col)

poppedelents=col.pop()
print(poppedelents)
print(col)

col.pop(2)
print(col)

col.insert(0,"grey")
print(col)

red_index=col.index("red")       #return index of 1st occurence of red
print(red_index)



athira_fav_col=["blue","yellow","black","white"]
avani_fav_col=athira_fav_col.copy()
avani_fav_col.pop()
print("avani_fav_col",avani_fav_col)
print("athira_fav_col",athira_fav_col)



lst=[2,6,3,4,5,6]
lst.sort()
print(lst)