"""
Time Complexity:
1. insert --> O(1)
2. lookup --> O(1) (depends on collision)
3. delete --> O(1)
4. search --> O(1)

But not good to access the keys of a Hash table because it depends on the size of the hash table.

Playground: https://www.cs.usfca.edu/~galles/visualization/OpenHash.html
When there is a collision, it slows down the reading and writing with a hash table with O(n/k) where k is the size
of your hash table. So, O(n/k) => O(n). To avoid this collision, can refer this wikipedia page:
https://en.wikipedia.org/wiki/Hash_table#Collision_resolution

Pros:
1. Fast lookups (Good collision resolution needed)
2. Fast inserts
3. Flexible Keys

Cons:
1. Unordered
2. Slow key iteration

"""

def log_print():
    print("ahhhhhh!")

user = {
    "age": 54,
    "name": "Sayan",
    "magic": True,
    "scream": log_print,
}

print(user["age"])              # O(1)
user["spell"] = "abra kadabra"  # O(1)
print(user)
print(user["scream"]())         # O(1)
