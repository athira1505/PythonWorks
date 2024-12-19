

def sum_unique(nums):
    count={}

    for num in nums:
        count[num]=count.get(num,0)+1

    unique_sum=sum(key for key,value in count.items() if value==1)
    return unique_sum

# nums=[1,2,3,2]
# nums=[1,1,1,1,1]
nums=[1,2,3,4,5]
print(sum_unique(nums))