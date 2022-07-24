def selection_sort(array: list) -> list:
    length = len(array)

    # Traverse through all array elements
    for i in range(length):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, length):
            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(selection_sort(numbers))
