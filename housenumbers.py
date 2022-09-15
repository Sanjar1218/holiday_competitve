def house_numbers_sum(inp):
    return ','.join(map(str,inp)).find('0,')//2

print(house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]))