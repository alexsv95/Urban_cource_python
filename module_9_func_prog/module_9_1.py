
def apply_all_func(int_list, *function):
    result = {}
    for func in function:
        result[func.__name__] = func(int_list)
    return result

my_numbers = [7, 2, 9, 4, 1, 20, 6, 8]

print(apply_all_func(my_numbers, max, min))
print(apply_all_func(my_numbers, len, sum, sorted))
