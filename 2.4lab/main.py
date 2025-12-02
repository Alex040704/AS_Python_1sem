def change_case(strings, to_upper=False):
    if to_upper:
        return ' '.join(s.upper() for s in strings)
    return ' '.join(s.lower() for s in strings)

def filter_combined_lists(list1, list2, filter_function=None):
    combined = list1 + list2
    if filter_function:
        return [x for x in combined if filter_function(x)]
    return combined

def unique_sorted_numbers(numbers):
    return sorted(set(numbers))

def strings_starting_with_upper(*strings):
    return [s for s in strings if s and s[0].isupper()]
