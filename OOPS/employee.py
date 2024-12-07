

class Employee():
    id:int
    name:str
    age:int
    department:str
    salary:int

    def set_employee(self,id,name,age,department,salary):
        self.id=id
        self.name=name
        self.age=age
        self.department=department
        self.salary=salary

    def display(self):
        print(self.id,self.name,self.age,self.department,self.salary)

emp_instance=Employee()
emp_instance.set_employee(100,"vyshnav",23,"django",30000)
emp_instance.display()
