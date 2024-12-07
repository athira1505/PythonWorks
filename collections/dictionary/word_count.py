

words=["hai","hello","hai","hello"]

word_count={}

# iterate words

for w in words:

    # check w exist in word_count
    if w in word_count:
        word_count[w]+=1


    else:
        # add w as key in word_count and value as 1
        word_count[w]=1

print(word_count)

