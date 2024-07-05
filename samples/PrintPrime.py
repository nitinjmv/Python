list = [0, 1]
def prime(n):
    for i in range (2, n):
        for j in range(2, n):
            if i % j == 0:
                break
            list.append(i)
            break
    return list


print(prime(10))

# 12357