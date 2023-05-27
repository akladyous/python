

# Sum of the Squares of the First nn Positive Integers
#   n(n+1)(2n+1)
#   ------------
#       6

def sum_square_first_positive_intiger(nums):
    return (max(nums) * (max(nums)+1) * (2*max(nums)+1))/6

l1=list(range(1,101))

print(sum_square_first_positive_intiger(l1))