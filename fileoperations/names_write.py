
f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\names.txt","w")

language=["pyton","java","c#","javascript"]

for l in language:
    f.write(l+"\n")


f.close()