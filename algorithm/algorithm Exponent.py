

# def expponent(num, exp):
#     temp = num
#     for x in range(1,exp):
#         num = num * temp
#     return num
# print(expponent(25,3))



def exp(n,p):
    return n*exp(n,p-1) if p else 1

print(exp(2,7))