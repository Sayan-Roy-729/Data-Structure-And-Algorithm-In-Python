from typing import Union


def node(value) -> Union[dict, None]:
    return {
        "value": value,
        "next": None
    }


class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        # extract the very top element
        return self.array[-1] if len(self.array) > 0 else None

    def push(self, value):
        # add node on top of the last node
        self.array.append(value)
        return self

    def pop(self):
        # remove the very top node
        self.array.pop()
        return self


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("google")
    my_stack.push("udemy")
    my_stack.push("discord")
    print("Peek:", my_stack.peek)
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print(my_stack.array)
    print(my_stack.peek)
