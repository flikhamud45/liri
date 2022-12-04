def intersection(list_1, list_2):
    return [x for x in list_1 if x in list_1 and x in list_2]

print(intersection([1, 2, 3, 4], [8, 3, 9]))