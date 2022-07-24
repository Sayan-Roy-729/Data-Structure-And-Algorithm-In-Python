def memoized_add_to_80() -> int:
    cache = {}

    def memoized(n: int) -> int:
        if n in cache:
            return cache[n]
        else:
            print("Long time!")
            cache[n] = n + 80
            return cache[n]
    return memoized


if __name__ == "__main__":
    memoized = memoized_add_to_80()

    print(memoized(5))
    print(memoized(5))
    print(memoized(6))
