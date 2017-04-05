def find_max_min(numbers):
    max_min = []
    numbers.sort()
    max_min.append(numbers[0])
    if max_min[0] != numbers[-1]:
        max_min.append(numbers[-1])
    return max_min


# print find_max_min([4, 4, 4, 4])
