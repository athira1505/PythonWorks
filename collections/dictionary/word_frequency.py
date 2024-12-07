text="ABABBCCDDE"

character_freq={ch:text.count(ch) for ch in text}
print(character_freq)


for k,v in character_freq.items():
    if v==1:
        print(k)
# or
# non_recursive_ch=[k for k,v in character_freq.items() if v==1]
# print(non_recursive_ch)



