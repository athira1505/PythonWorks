

movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]


# count movies

print(len(movies))

# print all movies

movie_tiltle=[m.get("title") for m in movies]
print(movie_tiltle)

# movie in 2024
movie_yr=[m.get("title") for m in movies if m.get("year")==2024]
print(movie_yr)

# malayalam movie

mal_movie=[m.get("title") for m in movies if m.get("language")=="malayalam"]
print(mal_movie)


# high run time

print(max(movies,key=lambda d:d.get("run_time")))