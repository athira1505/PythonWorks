
arr=[10,20,30,40,2,3,7,8,9,10,30]

#(10:100,20:400,......)

result={}
for num in arr:
    square=num**2
    result[num]=square
print(result)



# SYNTAX   result={key:value   iteration   condition}

result={num:num**3 for num in arr }
print(result)


# even no square
even_sq={num:num**2 for num in arr if num%2==0}
print(even_sq)

odd_cube={num:num**3 for num in arr if num%2!=0}
print(odd_cube)

frequency_count={num:arr.count(num) for num in arr}
print(frequency_count)