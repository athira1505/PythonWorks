

class Student:
    name:str
    rollnum:int
    age:int
    course:str


    def __init__(self,name,rollnum,age,course):
        self.name=name
        self.rollnum=rollnum
        self.age=age
        self.course=course

    def display(self):
        print(self.name,self.rollnum,self.age,self.course)


stud_instance1=Student("vyshnav",100,23,"django")
stud_instance1.display()

