users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

count_tom = users.count("Tom")
count_mark = users.count("Mark")
count_alice = users.count("Alice")
count_john = users.count("John")

print(f"Tom зустрічається {count_tom} рази")
print(f"Mark зустрічається {count_mark} рази")
print(f"Alice зустрічається {count_alice} рази")
print(f"John зустрічається {count_john} рази")

users.pop(2)
users = [user for user in users if user != "Tom"]

print("Оновлений список:", users)
