S = ["Сир", "Молоко", "Морозиво", "Шоколад", "Сметана", "Майонез", "Хліб", "Макарони",
     "Мука", "Цукор", "Сіль", "Вершки", "Яйця", "Круасани", "Сосиски",
     "Ковбаса", "Клубніка", "Хурма", "Яблука", "Чорниця"]

A = [32, 30, 63, 21, 46, 82, 17, 70, 90, 20, 50, 103, 35, 65, 45, 25, 55, 15, 85, 95]

B = [10, 15, 20, 21, 30, 12, 18, 22, 27, 35, 40, 50, 60, 32, 45, 28, 33, 17, 19, 29]

total_value = sum([A[i] * B[i] for i in range(20)])

average_price = sum(B) / len(B)

max_quantity_index = A.index(max(A))
most_stocked_item = S[max_quantity_index]

print(f"Загальна вартість товарів на складі: {total_value}")
print(f"Середня ціна товару: {average_price}")
print(f"Найбільше на складі товару: {most_stocked_item}, кількість: {A[max_quantity_index]}")
