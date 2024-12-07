
# create afn multiplication_table(number,n)
# print multiplication table of number till n

# multiplication_table(3,50)


def multiplication_table(number,n):

    for i in range(1,n+1):
      
      print(f"{i}*{number}={i*number}")

multiplication_table(3,50)