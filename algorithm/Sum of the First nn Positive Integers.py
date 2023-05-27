# Sum of the First nn Positive Integers
#   Sn = n(n+1)
#   ------------
#       2

nums = list(range(1,101))

def sum_first_positive_intiger(NumSeries):
    # formula n (n+1) / 2
    max_num = max(nums)
    return max(nums)*(max(nums)+1)/2

print(sum_first_positive_intiger(nums))

