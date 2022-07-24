# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# the pattern of the sequence is that each value is the sum of the 2 previous values,
# that means for N=5 -> 2+3

def fibonacci_iterative(n):  # O(n) time complexity
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 2] + arr[i - 1])
    return arr[n]


def fibonacci_recursive(n):  # O(2^n) time complexity
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive((n - 2))


if __name__ == "__main__":
    print(fibonacci_iterative(3))
    print(fibonacci_recursive(3))
