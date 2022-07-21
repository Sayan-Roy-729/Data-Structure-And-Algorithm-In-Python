class HashTable:
    def __init__(self, size):
        self.data = [None for i in range(size)]

    def _charcodeat(self, string, index):
        """
        Return a unique hash code for a character.
        """
        if isinstance(string, str) and isinstance(index, int):
            return ord(string[index])
        else:
            raise Exception(f"Error: charcodeat takes a str and an int, received {type(string)} and {type(int)}.")

    def _hash(self, key):
        """
        Create a hash for a key
        """
        hash = 0
        for i in range(len(key)):
            hash = (hash + self._charcodeat(key, i)) % len(self.data)
        return hash

    def get(self, key):
        """
        Time complexity is O(1) if there is no collision. But it depends on the collision.
        """
        address = self._hash(key)
        current_bucket = self.data[address]
        if len(current_bucket):
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1] 
        else:
            return None

    def set(self, key, value):
        """
        Time complexity is O(1)
        """
        address = self._hash(key)
        if self.data[address] == None:
            self.data[address] = []
        
        self.data[address].append([key, value])
        return self.data

    def keys(self):  # this is a cons of hash tables
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i] != None:
                keys_array.append(self.data[i][0][0])
        return keys_array

if __name__ == "__main__":
    my_hash_table = HashTable(50)
    my_hash_table.set("grapes", 10000)
    my_hash_table.set("apples", 54)
    my_hash_table.set("apples", 14)
    my_hash_table.set("oranges", 2)
    print(my_hash_table.data)
    print(my_hash_table.get("grapes"))
    print(my_hash_table.keys())