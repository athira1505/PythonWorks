


#  set operations


st1={10,20,30,40,50}
st2={10,20,60,70,80}
print(type(st1))

itersection_set=st1.intersection(st2)
print(itersection_set)

union_set=st1.union(st2)
print(union_set)

difference_set=st1.difference(st2)
print(difference_set)

st1.remove(50)
print(st1)





st3={1,2,3}
st4={1,2,3,4,5}
print(st3.issubset(st4))
print(st3.issuperset(st4))





st5={1,2,3,10,20}
st6={1,2,3,4,5}
symmetric_diff=st5.symmetric_difference(st6)
print(symmetric_diff)

st5.update(st6)
print(st5)





# remove duplicate words
text="this is a text to remove duplicate words this text is simple"
text2="this simple text remove duplicate words"

words=text.split(" ")  #split txt wrt space
print(set(words))

print(set(text).issubset(set(text2)))