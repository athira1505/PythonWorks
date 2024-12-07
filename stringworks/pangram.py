# chck whether the text contain all alphabets in english

text="The quick brown fox jumps over the lazy dog"

text=text.casefold()

is_pangram=True

alphabets="abcdefghijklmnopqrstuvwxyz"

for ch in alphabets:
    if ch not in text:
        is_pangram=False
        break

print(is_pangram)
