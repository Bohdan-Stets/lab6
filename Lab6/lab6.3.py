import random

numbers = [random.randint(-50, 50) for _ in range(25)]

A1 = [num for num in numbers if num > 0]

A2 = [num for num in numbers if num < 0]

print("Початковий список:", numbers)
print("Список додатніх елементів (A1):", A1)
print("Список від'ємних елементів (A2):", A2)
