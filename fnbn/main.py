from itertools import permutations


def find_next_bigger_number(n: int) -> int:
    value = str(n)
    all_combinations = (([int(''.join(number)) for number in list(set(permutations(value, len(value))))]))
    sorted_combinations= sorted(all_combinations)
    max_num_index = sorted_combinations.index(n)
    if max_num_index == len(sorted_combinations) - 1:
        return -1
    return sorted_combinations[max_num_index + 1]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(find_next_bigger_number)