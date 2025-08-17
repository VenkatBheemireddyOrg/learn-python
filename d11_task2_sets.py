my_set = {1,5,4,3,2}
print("my_set :", my_set)

my_set.add(6)
print("After addition :", my_set)

my_set.remove(1)
print("After removal :", my_set)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1.union(set2)
print("union_set :", union_set)

intersection_set = set1.intersection(set2)
print("intersection_set :", intersection_set)

difference_set = set1.difference(set2)
print("difference_set :", difference_set)

is_subset = set1.issubset(set2)
print("is_subset :", is_subset)

is_superset = set1.issuperset(set2)
print("is_superset :", is_superset)
