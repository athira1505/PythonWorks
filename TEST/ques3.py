
text="this is a simple python program that print most recursive word . this program is simple"

words=text.split(" ")
print(words)

def get_count(w):
    return words.count(w)
freq_word=max(words,key=get_count)
print(freq_word)
