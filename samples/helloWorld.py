print("hello world")

# Loop
for i in range(10):
    print(i)

print(type( () ) ) # tuple
print(type( {} ) ) # dict
print(type( [] ) ) # list

# tuple
a = (1,2,4,5,9,0,2)
for i in a:
    if i % 2 == 0:
        print(i)

# dict
b = {2,4,5,7,8,8,9}
for i in b:
    print(i)

# list
c = [23,3,6,7,8,9]
for i in c:
    print(i)

def myFun():
    print("my function")
myFun()