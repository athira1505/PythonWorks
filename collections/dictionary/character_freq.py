
text="ABAABBC"

def get_count(ch):
    return text.count(ch)


# most recursive character
most_recursive_ch=max(text,key=get_count)
print(most_recursive_ch)


# non recursive character
least_recursive_ch=min(text,key=get_count)
print(least_recursive_ch)
