

cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]


# count of vehicles
print(f"total cars=>{len(cars)}")


# print available colors of baleno
baleno_col=[c.get("colors") for c in cars if c.get("name")=="baleno" ]
print(baleno_col[0])  #[0] is given to get 1st element(list) inside  that particular list cars


# print all brands
#  no duplicates that is print nexa only 1 time        ans:use set
brand=[c.get("brand") for c in cars ]
print(set(brand))


# print car names available in amt transmission
car_names=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(car_names)


# cars in blue clr
car_col=[c.get("name") for c in cars if "blue" in c.get("colors")]
print(car_col)


# print all transmissions
transmissions=[t for c in cars for t in c.get("transmissions")  ]
print(set(transmissions))


# print all colors
col={color for c in cars for color in c.get("colors")}
print(col)


# most popular col



# costly car
costly_car=max(cars,key=lambda p:p.get("price"))
print(costly_car.get("name"))


# car with min cost
min_costly_car=min(cars,key=lambda p:p.get("price"))
print(min_costly_car)



# sort cars wrt price
sort_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)
#sort_car_name=[c.get("name") for c in sort_car]    
sort_car_name={c.get("name"):[c.get("price"),c.get("brand")] for c in sort_car}
print(sort_car_name)
