def bubble_sort(array: list) -> list:
    length = len(array)  # O(1) Time Complexity

    for i in range(length - 1):  # for both loops, O(n^2) time complexity
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                # swap numbers
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


if __name__ == "__main__":
    numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    print(bubble_sort(numbers))
