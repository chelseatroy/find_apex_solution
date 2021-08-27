from find_apex import find_apex_iterative, find_apex_recursive

list_with_apex = [1, 2, 3, 9, 7, 6, 5]

item, index = find_apex_recursive(list_with_apex, 0, len(list_with_apex))
assert item == 9
assert index == 3

item, index = find_apex_iterative(list_with_apex)
assert item == 9
assert index == 3


