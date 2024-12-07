
class Faculty():
    id:int
    name:str
    age:int
    course:str
    experience:int
    salary:int

    def set_faculty(self,id,name,age,course,experience,salary):
        self.id=id
        self.name=name
        self.age=age
        self.course=course
        self.experience=experience
        self.salary=salary

    def display(self):
        print(self.id,self.name,self.age,self.course,self.experience,self.salary)

faculty_instance1=Faculty()
faculty_instance2=Faculty()
faculty_instance2.set_faculty(100,"athira",23,"django",1,30000)
faculty_instance2.display()
