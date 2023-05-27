def format_address(address_string):

    address = address_string.split()
    housenum = address[0]
    street =  " ".join(address[1:])


    return "house number {} on street named {}".format(housenum, street)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
