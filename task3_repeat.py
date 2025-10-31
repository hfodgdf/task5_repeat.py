a = int(input("Перше число: "))
b = int(input("Друге число: "))

total = sum(range(min(a, b), max(a, b) + 1))

print(f"Сума всіх чисел від {a} до {b} включно: {total}")
