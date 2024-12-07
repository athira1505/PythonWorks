class Mobile():
    name:str
    price:int
    brand:str

    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand

    def display(self):
        print(self.name,self.price,self.brand)

mob_instance=Mobile("oneplusnord9r",45000,"oneplus")
mob_instance.display()