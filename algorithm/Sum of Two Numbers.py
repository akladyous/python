

# Given a list of numbers nums and a number k, return whether any two elements from the list add up to k.
# You may not use the same element twice.
#
# Note: Numbers can be negative or 0.


nums = [35, 8, 18, 3, 22,1,9,4,22,19,90,101,23,93,55]


print(np.median(nums))

def sum2nums(nums,var):
    for x in range(len(nums)):
        for y in range(x+1,len(nums)):
            if int(nums[x])+int(nums[y]) == var:
                # print(nums[x],' + ', nums[y], '== ', int(nums[x])+int(nums[y]))
                return True
    return False


print(sum2nums(nums, k))


# for item in nums:
#     for x in range(len(nums)):
#         print('comparison of ', str(item),str(nums[x]))

# nums = [35, 8, 18, 3, 22]
# k = 11
# counter = 1
# while 0 <= counter <= len(nums)-1:
#     print(nums[counter-1], nums[counter])
#     counter += 1
