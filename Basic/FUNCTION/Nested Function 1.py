# def outer(x,y):
#     def somma(a,b):
#         return a+b
#     return somma(a,b)
# print('the value is : ', outer(2,5))
# print('-----------------------------------------------------')
# def print_msg(message):
#     def inner():
#         return message
#     return inner() + ' belli e brutti'
# x=print_msg('ciao a tutti')
# print(x)
# del x
# print('-----------------------------------------------------')
# def esterna1(valore1):
#     def interna(valore2):
#         valore_interna=valore1+valore2
#         return valore_interna
#     return interna
# x=esterna1(10)
# y=x(10)
# print(y)
# del x
# del y
# print('-----------------------------------------------------')
# def esterna2(valore1): #valore string
#     def interna(valore2): #valore string
#         return valore2.upper()
#     return interna(valore1)
# x=esterna2('funzione esterna2')
# print(x)
# del x
# print('-----------------------------------------------------')
# def multiplicator1():
#     def multiplicator2(num1,num2):
#         return num1*num2
#     return multiplicator2
# multiply=multiplicator1()
# print(multiply(2,2))
# print('-----------------------------------------------------')
# def percent1(basic_value):
#     def percentage_operation(percent_value):
#         return basic_value * (1+ (1 * percent_value/100) )
#     return percentage_operation
# prezzo1=percent1(1200)
# print(prezzo1(15))
# print('-----------------------------------------------------')
# def percent2(basic_value, percent_value):
#     def percentage_operation():
#         return round(basic_value * (1+ (1 * percent_value/100) ), 2)
#     return percentage_operation()
# print(percent2(100,20))
# print('-----------------------------------------------------')
# def percent3():
#     def percentage_operation(basic_value, percent_value):
#         return round(basic_value * (1+ (1 * percent_value/100) ), 2)
#     return percentage_operation
# prezzo2=percent3()
# print(prezzo2(1230,19))
# print('-----------------------------------------------------')
def Fun3Parameters(val1,val2):

    def inner(val3):
        return (val1**val2)/val3
    return inner

xy=Fun3Parameters(2,2)
xyz=xy(2)
print(xyz)
# print('-----------------------------------------------------')
# def DictIteration():
#     d1={"uno": 100, "due": 200, "tre": 300, "quattro": 400, "cinque": 500}
#     for chiave, valore in zip(d1.keys(), d1.values()):
#         d1[chiave]=percent2(valore, 15)
#     print(d1)
# DictIteration()
# print('-----------------------------------------------------')



