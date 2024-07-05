def nat(n):    
    sum = 0
    for i in range(n):
        sum = n * (n + 1) / 2
    return sum

print(nat(7))

