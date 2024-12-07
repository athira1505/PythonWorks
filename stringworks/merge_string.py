# sample input1
#  txxt1="PQRS"
#  txxt2="ABCD"
# q)merge 2 strings
# output  PAQBRCSD

# sample input2
#  txxt1="PQRST"
#  txxt2="ABC"
# output: PAQBRCST


txxt1="PQR"
#      012

txxt2="ABC"
#      012

result=""
for i in range(0,len(txxt1)):  #len used, so this loop works only if both the txts have equal length             # OR for i in range(0,3):  
    result+=txxt1[i]+txxt2[i]

print(result)



# for text with uneven length : merging :
txxt3="PQRST"
#      01234

txxt4="ABC"
#      012

smallest_txt=txxt3 if len(txxt3)<len(txxt4) else txxt4
largest_txt=txxt3 if len(txxt3)>len(txxt4) else txxt4

result=""
for i in range(0,len(smallest_txt)):     #uses length of smallest txt only
    result+=txxt3[i]+txxt4[i]

bal_txt=largest_txt[len(smallest_txt):]
result+=bal_txt
print(result)


# text="ABCABC"
# print 1st recursive character A
