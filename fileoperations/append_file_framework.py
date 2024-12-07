
f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\framework.txt","a")

framework=["wordpress","springboot","oodo",'fastapi']

for fw in framework:
    f.write(fw+"\n")

f.close()