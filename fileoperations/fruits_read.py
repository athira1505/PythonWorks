

f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\fruits.txt","r")

fruits=[]

for line in f:
    fruits.append(line.rstrip("\n"))     #rstrip("\n")  removes \n

print(fruits)