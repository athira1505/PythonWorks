

student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[50,50,50]
}


# index=1 hari's avg mark
# index=5 anvin's avg mark


# for index,element in enumerate(student_data):
#     print(index,element)


index=5

for i,element in enumerate(student_data):

    if i+1==index:
        marks=student_data.get(element)
        avg=sum(marks)/len(marks)
        print(avg)


# avg mark of all

student_avg_mark={k:sum(v)/len(v) for k,v in student_data.items()}
print(student_avg_mark)


