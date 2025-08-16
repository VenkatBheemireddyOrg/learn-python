my_list = [10,70,40, 30, 60, 90, 80]
print("my_list", my_list)

new_list = my_list + [20,50]
print("new_list", new_list)

new_list_sorted = new_list.sort()
print("new_list_sorted", new_list_sorted)

slice_list = new_list_sorted[0:3]
print("slice_list", slice_list)