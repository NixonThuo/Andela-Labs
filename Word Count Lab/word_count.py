def words(words):
    words = words.replace("\n", " ")
    words = words.replace("   ", " ")
    words = words.replace("\t", " ")
    words = words.split()
    int_list = [int(x) for x in words if x.isdigit()]
    str_list = [str(x) for x in words if not x.isdigit()]
    word_count = {}  # Map each word to its count
    for word in str_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1
    for word in int_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] = word_count[word] + 1
    return word_count


# print words('testing 1 2 testing')
