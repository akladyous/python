def lr(n): 
    return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
x=lr(10)
def mySum(list):
    if len(list) > 0:
        res = 0
        for i in list:
            res += i
        return res
    else:
        return 0
xx=mySum(x)
print(xx)

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
# class Student:
#     def __init__(self, name, year_UM, knowledge):
#         self.name = name
#         self.year_UM = year_UM
#         self.knowledge = knowledge

#     def study(self):
#         self.knowledge += 1
#         return None

#     def getKnowledge(self):
#         return self.knowledge

#     def year_at_umich(self):
#         return self.year_UM