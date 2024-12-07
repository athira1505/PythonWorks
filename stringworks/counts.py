# print vowels count
# print consonents count




text="pneumonoultramicroscopicsilicovolcanoconiosis"
count=0
total=0

text=text.casefold()
for ch in text:

    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
       count=count+1
    else:
        total=total+1

print("vowelcount:",count)
print("consonentcount:",total)

