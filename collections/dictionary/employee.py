# dictionary employee with keys eid,name,salary,department,experience

employee={"eid":45,"name":"athira","salary":25000,"department":"technical","experience":6}
print(employee)


# add contact
employee["contact"]=87765543
print(employee)


# if experience>5 update employee salary as current_salary+10000 else current_salary+5000
if employee["experience"]>5:
    employee["salary"]+=10000
else:
    employee["salary"]+=5000
print(employee)


# add role as SDE if exp>5 else add role as JDE
if employee["experience"]>5:
    employee["role"]="SDE"
else:
    employee["role"]="jde"
print(employee)


