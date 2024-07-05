
# 1, 2, 3, 5, 8
def printFab(len):
    firstnum = 0
    secondnum = 1
    temp = 0
    for i in range(0, len):
        temp = firstnum + secondnum
        firstnum = secondnum
        secondnum = temp
        print(temp)







printFab(5)