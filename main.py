# print('kjhiuhiu')

# age1 =  int(input("возраст 1"))
# age2 = int(input("возраст 2"))
# age3= int(input("возраст 3"))

# if age3>age1 and age3>age2:
#     print("возраст 3 больше всех")
# elif age2>age1 and age2>age3:
#     print("возраст 2 больше всех")
# else:
#     print("возраст 1 больше всех")


import random

hp = 100
speed = 0
dist = 400

yetti = 1
tree = 2
rock = 3

while True:

    сhanceEnemy = random.randit(0,10)
    if chanceEnemy == rock:
        print("вы столкнулись с камнем")
        hp -= 5
        print(f"у вас осталось {hp} жизней")
    elif chanceEnemy == yetti:
        print("вы столкнулись с йети")
        hp = -= 10
        print(f"у вас осталось {hp} жизней")
    elif chanceEnemy == tree:
        print("вы влетели в дерево")
        hp -= 8
        print(f"у вас осталось {hp} жизней")
    
    speed += 1
    dist -= speed
    print(f"\nвы летите со скоростью {speed} км/с")
    print(f"осталось проехать {dist} километров")
    print(f"у вас осталось {hp} жизней")
    if(dist <= 0):
        print("УРА! победа!")
        break
    if(hp <= 0):
        print("вас сожрали")
        break

