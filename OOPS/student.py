

# student


class Student:
    name:str
    rollnum:int
    age:int
    course:str

    # initializing attributes  of student class

    def set_student(self,name,rollnum,age,course):
        self.name=name
        self.rollnum=rollnum
        self.age=age
        self.course=course

    def display(self):
        print(self.name,self.rollnum,self.age,self.course)


# reference_name=ClassName()

stud_instance1=Student()

stud_instance1.set_student("vyshnav",100,23,"django")
stud_instance1.display()

