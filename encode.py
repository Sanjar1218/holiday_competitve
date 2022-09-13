def encode(message, key):
    x = lambda x: ord(x)-96
    lst = list(map(x, message))
    lstkey = list(map(int, list(str(key))))
    for i in range(len(lst)):
        lst[i] += lstkey[i%len(lstkey)]
    return lst

encode("masterpiece", 1939)