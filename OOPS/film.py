# movie
# title,rating,run_time,director,genre

# arm
# kgf

class Film():
    id:int
    title:str
    rating:int
    run_time:int
    director:str
    genre:str

    def set_film(self,id,title,rating,run_time,director,genre):
        self.id=id
        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre


    def display(self):
        print(self.id,self.title,self.rating,self.run_time,self.director,self.genre)


film_instance1=Film()
film_instance1.set_film(100,"arm",4.5,"jithin lal",120,"action")
film_instance1.display()