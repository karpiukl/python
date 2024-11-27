def remove_duplicates(lst):
    return list(set(lst))

def sort_list(lst):
    numbers = sorted([item for item in lst if isinstance(item, (int, float))])
    strings = sorted([item for item in lst if isinstance(item, str)])
    return numbers + strings

initial_list = [3, 1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']
unique_list = remove_duplicates(initial_list)
sorted_list = sort_list(unique_list)

print("Список без повторень:", unique_list)
print("Відсортований список:", sorted_list)
