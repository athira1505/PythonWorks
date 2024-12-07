

source_word="CHIKENN"

target_word="HEN"

# kangaroo word



ch_count={ch:source_word.count(ch) for ch in source_word}

is_kangaroo_word=True

for ch in target_word:

    if ch in ch_count and ch_count.get(ch)>0:

        ch_count[ch]-=1

    else:

        is_kangaroo_word=False
        break

print(is_kangaroo_word)
