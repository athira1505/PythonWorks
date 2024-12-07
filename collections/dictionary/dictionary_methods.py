
# employee id, name,department,age,salary

employee={"id":123,"name":"athira","department":"hr","age":23,"salary":25000}

print(employee.get("department"))

employee.pop("salary")
print(employee)


# return all keys =>keys()
for k in employee.keys():
    print(k)


# fetch all values =>values()
for v in employee.values():
    print(v)


# fetch key and values
for k,v in employee.items():
    print(k,v)


# get(),pop(),keys(),values()
# to fetch both keys and values => items()

 