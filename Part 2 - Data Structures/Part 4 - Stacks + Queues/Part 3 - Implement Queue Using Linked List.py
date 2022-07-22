from typing import Union


def node(value) -> Union[dict, None]:
    return {
        "value": value,
        "next": None
    }


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        # return very first item
        return self.first if self.length > 0 else None

    def enqueue(self, value):
        #
        new_node = node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last["next"] = new_node
            self.last = new_node

        self.length += 1
        return self

    def dequeue(self):
        if self.first is None:
            return None

        if self.first == self.last:
            self.last = None

        self.first = self.first["next"]
        self.length -= 1
        return self


if __name__ == "__main__":
    my_queue = Queue()
    print(my_queue.peek())
    my_queue.enqueue("Joy")
    my_queue.enqueue("Matt")
    my_queue.enqueue("Pavel")
    my_queue.enqueue("Samir")
    print("First Node:", my_queue.first)
    print("Last node: ", my_queue.last)
    print("Peek:      ", my_queue.peek(), "\n")
    my_queue.dequeue()
    my_queue.dequeue()
    print("First Node:", my_queue.first)
    print("Last node: ", my_queue.last)
    print("Peek:      ", my_queue.peek())
