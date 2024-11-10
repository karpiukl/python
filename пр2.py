values = [42, "Hello", 3.14, True, 100, "World", 15, False, 0.5, 150]
types = [type(value) for value in values]
most_common_type = max(set(types), key=types.count)
print(f"Найбільш поширений тип даних: {most_common_type}")
