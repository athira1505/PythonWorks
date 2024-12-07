# class str:
#     def capitalise()
#     def casefold()
#     def isalpha()
#     def isdigit()
#     def isalnum()
#     startswith(str)
#     endswith(str)
#     split()
#     strip()    => remove from left and right side only
#     lstrip()   => from left
#     rstrip()   => from right
#     replace("old_para","new_param")           or       replace("old_para","new_param",count)       
#     slicing  =>  string[start:end:step]
#     index("needed_alphabet")  => to find index of an alphabet

text="helloPythonWoRLD"

result=text.capitalize()
print(result)

result=text.casefold()
print(result)

result=text.isalpha()
print(result)

result=text.isdigit()
print(result)

result=text.isalnum()
print(result)

print(text.startswith("he"))

print(text.endswith("on"))


for ch in text:
    print(ch)

texts="hello,world,python"
words=texts.split(",")
print(words)

txt="\nthis is a line\n"
new_txt=txt.strip("\n")
print(new_txt)


# o to a
tt="hello world program"
new_tt=tt.replace("o","a")
print(new_tt)


new_tts=tt.replace("o","a",2)
print(new_tts)

content="python programming"
       # 012345678901234567
# string_object[start:end:step]   => slicing

print(content[:6])  #print(content[0:6])  => from start so no need to give start val
print(content[7:])   #  => no end value
print(content[::2])
print(content[::-1])


string="hello"
rev_string=string[::-1]
print(rev_string)


txt1="helloworld"
#     0123456789
# index of 1st o
print(txt1.index("o"))


txt2="athirasanthosh@gmail.com"
# find index of @
# slice from 0 to index upto @
t=txt2.index("@")
print(txt2[:t])


txt3="hellopython"
# print llehopython
t=txt3.index("o")
new_txt3=txt3[0:t]
rev_sub_strng=new_txt3[::-1]

balance_sub_strng=txt3[t:]

result=rev_sub_strng+balance_sub_strng
print(result)




