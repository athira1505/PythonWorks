

text="ABBACB"

# print character count

for ch in text:
    print(ch)

# ch_count={}
# for ch in text:
#     if ch in ch_count:
#         ch_count[ch]+=1
#     else:
#         # add w as key in word_count and value as 1
#         ch_count[ch]=1
ch_count={ch:text.count(ch) for ch in text}
print(ch_count)




# first recursive character

