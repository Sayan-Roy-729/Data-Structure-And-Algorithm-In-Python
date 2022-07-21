"""
Structure of linked list:

10 --> 5 --> 16

my_linked_list = {
    "head": {
        "value": 10,
        "next": {
            "value": 5,
            "next": {
                "value": 16,
                "next": None,
            },
        },
    } 
}
"""


class LinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next": None
        }
        self.tail = self.head
        self.length = 1

    def _new_node(self, value):
        return {
            "value": value,
            "next": None
        }

    def append(self, value):
        # add element at the end of the lined list [O(1) time complexity]
        new_node = self._new_node(value)
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return self.head

    def prepend(self, value):
        # add element at the beginning of the linked list [O(1) time complexity]
        new_node = self._new_node(value)
        new_node["next"] = self.head
        self.head = new_node
        self.length += 1
        return self.head

    def print_list(self):
        array = []
        current_node = self.head

        while current_node is not None:
            array.append(current_node["value"])
            current_node = current_node["next"]

        return array

    def traverse_to_index(self, index):
        # check params
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node["next"]
            counter += 1
        return current_node

    def insert(self, index: int, value) -> list:
        # insert an element at a particular index [O(n) time complexity]

        # check inputs
        if index > self.length:
            raise Exception("index should be int and should be within the range.")

        if index == 0:
            self.prepend(value)
            return self.print_list()
        elif index == self.length:
            self.append(value)
            return self.print_list()

        new_node = self._new_node(value)
        leader_node = self.traverse_to_index(index - 1)
        holding_pointer = leader_node["next"]
        leader_node["next"] = new_node
        new_node["next"] = holding_pointer
        self.length += 1
        return self.print_list()
    
    def remove(self, index: int) -> list:
        # delete a particular index element [O(n) time complexity]

        # check params
        # ---

        leader_node = self.traverse_to_index(index - 1)
        unwanted_node = leader_node["next"]
        leader_node["next"] = unwanted_node["next"]
        self.length -= 1
        return self.print_list()

    def reverse(self):
        # if there is only one element
        if self.head["next"] is None:
            return self.print_list()

        first = self.head
        self.tail = self.head
        second = first["next"]
        while second is not None:
            temp = second["next"]
            second["next"] = first
            first = second
            second = temp

        self.head["next"] = None
        self.head = first
        return self.print_list()


if __name__ == "__main__":
    my_linked_list = LinkedList(10)
    my_linked_list.append(5)
    my_linked_list.append(16)
    my_linked_list.prepend(1)
    print(my_linked_list.print_list())  # [1, 10, 5, 16]
    my_linked_list.insert(2, 99)
    print(my_linked_list.print_list())  # [1, 10, 99, 5, 16]
    my_linked_list.insert(5, 7)
    print(my_linked_list.print_list())  # [1, 10, 99, 5, 16, 7]
    my_linked_list.remove(2)
    print(my_linked_list.print_list())  # [1, 10, 5, 16, 7]
    print(my_linked_list.head)
    print(my_linked_list.tail)
    print(my_linked_list.reverse())     # [7, 16, 5, 10, 1]
    print(my_linked_list.head)
    print(my_linked_list.tail)

