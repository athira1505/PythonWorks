

class SuperHero:
    name:str
    suit:str

    def __init__(self,name,suit):
        self.name=name
        self.suit=suit

    def __str__(self):
        return self.name
    
class SpiderMan(SuperHero):

    def __init__(self, name, suit):
        super().__init__(name, suit)

    def super_power(self):
        print("spider sense","web shooting","sticky hands")

spiderman_instance=SpiderMan("spiderman","spidersuit")

class MinnalMurali(SuperHero):
    def __init__(self, name, suit):
        super().__init__(name, suit)

    def super_power(self):
        print("running","jumping","reflex")

minnalmurali_instance=MinnalMurali("minnalmurali","minnalmurali suit")
print(minnalmurali_instance)
minnalmurali_instance.super_power()

