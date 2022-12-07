def parse_ranges(ranges_string):
    lst = ranges_string.split(",")
    get_range = (r.split("-") for r in lst)
    get_numbers = (num for start, stop in get_range for num in range(int(start), int(stop)+1))

    return get_numbers
print(list(parse_ranges("1-2,4-4,8-10")))