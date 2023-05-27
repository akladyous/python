
def sum2items(funzione_da_decorare):
    def sum1item(basic_value,percent_value):
        funzione_da_decorare(basic_value,percent_value)
        return basic_value * (1+ (1 * percent_value/100) )
    return sum1item


@sum2items
def percentage(basic_value,percent_value):
    return percentage

result=percentage(1000,20)
print(result)