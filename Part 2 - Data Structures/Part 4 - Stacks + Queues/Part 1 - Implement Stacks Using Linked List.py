from typing import Union


def node(value) -> Union[dict, None]:
    return {
        "value": value,
        "next": None
    }


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        # extract the very top element
        return self.top

    def push(self, value):
        # add node on top of the last node
        new_node = node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top["next"] = holding_pointer
        self.length += 1
        return self

    def pop(self):
        # remove the very top node
        if self.top is None:
            return None
        else:
            if self.top == self.bottom:
                self.bottom = None
                
            # holding_pointer = self.top
            self.top = self.top["next"]
            self.length -= 1
            return self


if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push("google")
    my_stack.push("udemy")
    my_stack.push("discord")
    print("Peek:", my_stack.peek())
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print("Top:", my_stack.top)
    print("Bottom:", my_stack.bottom)
