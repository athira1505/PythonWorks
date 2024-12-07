
#  key:value pairs
# dictionary

student=[1000,"ram","django","mca"]
print(student[1])


student={"rol":1000,"name":"ram","course":"django","qualification":"mca"}


# employee id=100 name=vipin department=hr salary=25000
employee={"id":100,"name":"vipin","department":"hr","salary":25000}
print(employee["name"])



# create a dictionary product with keys id,title,price,brand
product={"id":345,"title":"goodday","price":40,"brand":"britania"}
print(product["brand"])
# update product price as 50
product["price"]=50
print(product)

product["brand"]="parlie"
print(product)

# addind/insertion of a key
product["use_by_date"]="12-08-2024"
print(product)


if "offer" in product:
    product["offer"]=10
else:
     product["offer"]=20
print(product)