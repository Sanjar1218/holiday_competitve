from math import ceil
def movie(card, ticket, perc):
    i = 1
    m = ticket*perc
    while ticket*i<ceil(card+m):
        i+=1
        m = m+ ticket*perc**i
    return i

print(movie(500,15,0.9))