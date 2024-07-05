import random

nikku_counter = 0
papa_counter = 0

while True:
    nikku_num = int(random.randrange(1,50))
    papa_num = int(random.randrange(1, 50))
    if nikku_num > papa_num:
        nikku_counter = nikku_counter + 1
    elif papa_num > nikku_num:
        papa_counter = papa_counter + 1
    else:
        break

print(f'Papa won {papa_counter} times')
print(f'Nikku won {nikku_counter} times')

