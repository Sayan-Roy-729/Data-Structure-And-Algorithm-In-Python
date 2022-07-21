# Google Question
# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given as array = [2, 3, 4, 5]
# It should return undefined

from typing import Union

def first_recurring_character(input_array: list) -> Union[int, bool]:
    "method 1 --> O(n^2) time complexity but space complexity with O(1)"
    for i in range(len(input_array)):
       for j in range(i + 1, len(input_array)):
        if input_array[i] == input_array[j]:
            return input_array[i]
    return None

    "method 2 --> O(n) time complexity but Space complexity with O(n)"
    # hash_table = {}
    # for i in range(len(input_array)):
    #     if input_array[i] in hash_table:
    #         return input_array[i]
    #     else:
    #         hash_table[input_array[i]] = 1
    # return None


if __name__ == "__main__":
    print(first_recurring_character([2, 5, 5, 2, 3, 5, 1, 2, 4])) # will get 2 different ans from the 2 methods. WHy?

