def is_subseq(s,t):
    i,j=0,0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
        j+=1
    return i==len(s)

s="aec"
t="adbvch"
print(is_subseq(s,t))

