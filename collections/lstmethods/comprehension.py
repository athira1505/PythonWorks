

# list comprehension

# mapping   
# reduce   : max()  ,  min()   ,sum()
# filter


arr=[2,3,4,5,6,7]


# cubes=[]
# for num in arr:
#     cubes.append(num**3)
# print(cubes)


# OR


# syntax
#  reference=[return loop condition]


cube=[num**3 for num in arr]
print(cube)


square=[num**2 for num in arr]
print(square)


add_five=[num+5 for num in arr]
print(add_five)

odd_no=[num for num in arr if num%2!=0]
print(odd_no)

even_no=[num for num in arr if num%2==0]
print(even_no)

no_greater_five=[num for num in arr if num>5]
print(no_greater_five)


map_num=[num+1 if num>5 else num-1 for num in arr]
print(map_num)



text=["apple","iphone","orange","potato","watermelon"]
# words starting with vowels
vowel_words=[w for w in text if w[0] in ['a','e','i','o','u']]       #filter
print(vowel_words)

consonent_word=[w for w in text if w[0] not in ['a','e','i','o','u']]
print(consonent_word)



# longest worrd
long=max([len(w) for w in text ])
longest_word=[w for w in text if len(w)==long]
print(longest_word)



