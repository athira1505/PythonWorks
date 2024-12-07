

text="this is a simple question return word with maximun number of characters"

words=text.split(" ")

def get_lrngth(w):
    return len(w)


print(max(words,key=get_lrngth))
