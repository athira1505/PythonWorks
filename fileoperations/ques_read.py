
f=open("C:\\Users\\Athira\\OneDrive\\Desktop\\pythonworks\\dataset\\ques.txt","r")

words=[]

for line in f:
    # line=this is a python program to print hello world
    line=line.rstrip("\n")
    all_words=line.split(" ")   #["this","is"...]

    for w in all_words:
        words.append(w)

print(words)

word_count={w:words.count(w) for w in words}
print(word_count)

value_key=[[v,k] for k,v in word_count.items()]
print(sorted(value_key,reverse=True))