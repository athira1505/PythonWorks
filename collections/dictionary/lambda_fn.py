#lambda fn  used when only 1 statement is present inside def


def add_number(num1,num2):
    return num1+num2
print(add_number(100,200))

# solving the above using lambda fn
add=lambda num1,num2:num1+num2
print(add(100,200))



cube=lambda num:num**3
print(cube(3))


sub=lambda num1,num2:num1-num2
print(sub(10,2))

add=lambda num1,num2:num1+num2
print(add(10,2))


max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
print(max_two("hai","hello"))


smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(8,9))




words=["hello","hai","morning","test","apple"]

print(max(words))
# def get_length(word):
#     return len(word)
# print(max(words,key=get_length))
# print(min(words,key=get_length))

# OR

get_length=lambda word:len(word)
print(max(words,key=get_length))



# sort words

def get_length(words):
    return len(words)
sort_words=sorted(words,key=get_length)
print(sort_words)


