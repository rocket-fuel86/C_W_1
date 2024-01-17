# from random import randint
#
# comp = randint(1, 100)
# user = 0
# count = 0
#
# while user != comp:
#     count += 1
#     user = int(input("Угадай число: "))
#     if comp > user:
#         print("Твоё число меньше. Введите число побольше!")
#     elif comp < user:
#         print("Твоё число слишком большое. Нужно поменьше!")
# else:
#     print(f"Ты угадал с {count} попытки!")

a = int(input("Введите начало диапозона: "))
b = int(input("Введите конец диапозона: "))


while a < b:
    users_value = int(input("Введите еще любое число: "))
    if users_value >= a and users_value <= b:
        break
for i in range(a, b+1):
    if i == users_value:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")
