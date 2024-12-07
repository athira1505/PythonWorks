# collection is used when we have to manage a group of objects

#   define is duplictes-allowed  insertion_order_preserved mutable methods

#  list  []    or     list()

expenses=[10000,12000,13000,14000]
# index    0     1     2     3
print(expenses[1])

expenses[0]=15000
print(expenses)


colors=["red","green","blue"]
print(colors[2])



colors=list()
print(type(colors))



colors={"red","green","blue","green","blue"}    #duplicates not allowed curly braces used
print(colors)

colors=["red","green","blue","green","blue"]    #duplicates  allowed  list[] or list() used
print(colors)



colors=["red","green","blue","green","blue"]
#         0     1       2       3      4

colors[0]="pink"                  #mutable
print(colors)