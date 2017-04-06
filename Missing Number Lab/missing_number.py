def find_missing(a, b):
    """the comments are for a scenario 
    where we are comparing lists with more than one 
    missing number
    """
    # missing = []

    if len(a) is 0 and len(b) is 0:
        return 0
    elif a == b:
        return 0
    else:
        for number in a:
            if number not in b:
                # missing.append(number)
                return number
        for number in b:
            if number not in a:
                # missing.append(number)
                return number
    # return missing


# print find_missing([5, 4, 7, 6, 11, 66], [4])
