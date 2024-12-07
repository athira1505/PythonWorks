# name and age of 5 peoplle
# access and print age of one person using their name

name_dictionary={"ammu":21,"arya":25,"athul":21,"athira":23,"advay":1}

def get_age(gname):
    if gname in  name_dictionary:
        return name_dictionary[gname]
    else:
        return "not found"
    
print(get_age("advay"))