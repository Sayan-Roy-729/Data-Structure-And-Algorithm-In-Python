# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a
# for loop
def find_factorial_recursive(number: int) -> int:  # O(n)
    if number == 2:
        return 2
    return number * find_factorial_iterative(number - 1)


def find_factorial_iterative(number: int) -> int:  # O(n) time complexity
    answer = 1

    if number == 2:
        answer = 2

    for i in range(2, number + 1):
        answer = answer * i

    return answer


if __name__ == "__main__":
    print(find_factorial_iterative(5))
    print(find_factorial_recursive(5))
