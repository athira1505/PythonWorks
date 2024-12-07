

text="this is a simple programming question to find word with maximum number of  characters"

# step1
words=text.split(" ")
print(words)


# step2
def get_lrngth(w):
    return len(w)


print(max(words,key=get_lrngth))


srt_words=sorted(words,key=get_lrngth)                   #sort in ascending order
print(srt_words)


srt_words=sorted(words,key=get_lrngth,reverse=True)      #sort in adescending order
print(srt_words)



# most recursive wors

# step1 split words by       words=text.split(" ")

# step2 count

def get_count(w):
    return words.count(w)
freq_word=max(words,key=get_count)
print(freq_word)



