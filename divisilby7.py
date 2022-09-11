def seven(m):
    step = 0
    while m>0:
        m = m//10-2*(m%10)
        step +=1
        if len(str(m))<=2:
            return m, step
        print(m)
    return m, step
print(seven(483595))
    