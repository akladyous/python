def combine_lists(list1, list2):
    studentlist=list()
    list1.reverse()
    studentlist= list2 + list1
    return studentlist



# Generate a new list containing the elements of list2
# Followed by the elements of list1 in reverse order


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
