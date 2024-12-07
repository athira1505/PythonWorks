
def closest_no_to_zero(nums):
    nums.sort(key=lambda x:(abs(x),-x))
    return nums[0]
# nums=[-2,1,1]
nums=[-4,-2,1,4,8]
number=closest_no_to_zero(nums)
print("the closest no to 0 is: ",number)

