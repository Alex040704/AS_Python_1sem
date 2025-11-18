def filter_combined_lists(list1, list2, filter_function=None):
    combined = list1 + list2
    if filter_function is None:
        return combined
    else:
        return [x for x in combined if filter_function(x)]

def unique_sorted_numbers(numbers):
    return sorted(set(numbers))

def strings_starting_with_upper(*args):
    return [s for s in args if s and s[0].isupper()]

print("а) change_case:")
print(change_case(['Hello', 'World']))
print(change_case(['Hello', 'World'], to_upper=True))

print("\nб) filter_combined_lists:")
print(filter_combined_lists([2, 4], [6, 8]))
print(filter_combined_lists([2, 4], [6, 8], filter_function=lambda x: x > 5))

print("\nв) unique_sorted_numbers:")
print(unique_sorted_numbers([3, 1, 2, 3, 4, 2]))
print(unique_sorted_numbers([5, 5, 5, 5]))

print("\nг) strings_starting_with_upper:")
print(strings_starting_with_upper('Apple', 'banana', 'Cherry'))
print(strings_starting_with_upper('dog', 'Elephant', 'fox'))
