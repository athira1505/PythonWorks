

class Animal:
    sound:str
    name:str

    def set_animal(self,name,sound):
        self.name=name
        self.sound=sound

    def animal_sound(self):
        print("sound of",self.name,"is",self.sound)

lion_instance=Animal()
cat_instance=Animal()

lion_instance.set_animal("lion","roar")
cat_instance.set_animal("cat","meow")

lion_instance.animal_sound()
cat_instance.animal_sound()
