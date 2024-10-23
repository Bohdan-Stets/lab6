numbers = [10, 20, 30, 40, 50, 60]

numbers.insert(1, -5)

min_number = min(numbers)
max_number = max(numbers)

numbers[3:3] = [1, 2, 3]

numbers.append("Стець Богдан")

element_count = len(numbers)

print("Оновлений список:", numbers)
print("Мінімальний елемент:", min_number)
print("Максимальний елемент:", max_number)
print("Кількість елементів у списку:", element_count)
