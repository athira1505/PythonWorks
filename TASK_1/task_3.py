def roman_int(roman):                                          
    roman_numbers={
        'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
    }
    total=0                                                     # total=0
    prev_val=0                                                  #prev_val=0

    for char in reversed(roman):                                #(ix)  
        current_val=roman_numbers[char]                         #i:1               #x:10

        if current_val<prev_val:                                #1<0  :false       #10<1  :false
            total-=current_val                                                     
        else:
            total+=current_val                                  #total=1           #total=10+1=11

        prev_val=current_val                                    #prev_val=1
    return total                                                                    # total=11


roman_no=input("Enter Roman value: ")                              #xi
print(roman_int(roman_no.upper()))                                 #XI

