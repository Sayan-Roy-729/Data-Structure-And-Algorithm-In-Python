strings = ["a", "b", "c", "d"]
# 4 * 4 = 16 bytes of storage (For 32 bit System)
print(strings[2])  # O(1) time complexity

# push in js/append in py --> O(1) Time Complexity
strings.append("e")
print(strings)

# pop (in both language, it is same name) --> O(1) Time Complexity
strings.pop()
print(strings)

# unshift, splice in js/insert in py --> O(n) time complexity
strings.insert(0, "x")
print(strings)
strings.insert(2, "alien")  # O(n/2) = O(n) time complexity

# remove in py  --> O(n) time complexity
strings.remove()

"""
Summary:
1. Accessing, Insert element as last item or delete the last item in Python are O(1) time complexity.
2. But insertion at index 0 or middle of an array or remove an element in Python list are O(n) time complexity.

There are 2 types of array - static & dynamic. C++ has static array. But JS/Python have dynamic array.

Pros:
1. Fast lookups
2. Fast append/pop
3. Ordered

Cons:
1. Slow inserts
2. Slow deletes
3. Flxed size (if using static array)
"""