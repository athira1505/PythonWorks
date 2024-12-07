#  list palindrome


test_list = [1, 4, 5,  1]

print("The original list is : " + str(test_list))

reverse = test_list[::-1]
print("The reverse list is : " + str(reverse))
res = test_list == reverse

print("Is list Palindrome : " + str(res))