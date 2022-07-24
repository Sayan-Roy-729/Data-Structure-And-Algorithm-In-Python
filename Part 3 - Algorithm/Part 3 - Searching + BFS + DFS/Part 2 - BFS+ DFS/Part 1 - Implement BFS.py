from typing import Union
import json


def node(value) -> Union[dict, None]:
    return {
        "value": value,
        "left": None,
        "right": None,
    }


def traverse(node) -> Union[dict]:
    tree = {
        "value": node["value"],
        "left": None if node["left"] is None else traverse(node["left"]),
        "right": None if node["right"] is None else traverse(node["right"])
    }
    return tree


def traverse_in_order(node: dict, my_list: list) -> list:
    if node["left"] is not None:
        traverse_in_order(node["left"], my_list)
    my_list.append(node["value"])

    if node["right"] is not None:
        traverse_in_order(node["right"], my_list)
    return my_list


def traverse_post_order(node: dict, my_list: list) -> list:
    if node["left"] is not None:
        traverse_post_order(node["left"], my_list)

    if node["right"] is not None:
        traverse_post_order(node["right"], my_list)

    my_list.append(node["value"])
    return my_list


def traverse_pre_order(node: dict, my_list: list) -> list:
    my_list.append(node["value"])

    if node["left"] is not None:
        traverse_pre_order(node["left"], my_list)

    if node["right"] is not None:
        traverse_pre_order(node["right"], my_list)
    return my_list


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root

            while True:
                if value < current_node["value"]:  # so, working with left node
                    # if left node is empty, then add there
                    if current_node["left"] is None:
                        current_node["left"] = new_node
                        return self
                    # else select this left node as current node this time
                    current_node = current_node["left"]
                else:  # so, now have to work with the right nodes
                    # if next right node is empty, then add there
                    if current_node["right"] is None:
                        current_node["right"] = new_node
                        return self
                    # else select the right node as current node this time
                    current_node = current_node["right"]

    def lookup(self, value):
        if self.root is None:
            return None

        current_node = self.root
        while current_node is not None:
            if value < current_node["value"]:  # go to left side
                current_node = current_node["left"]
            elif value > current_node["value"]:  # go to right node
                current_node = current_node["right"]
            elif current_node["value"] == value:  # otherwise we have found the node
                return current_node

        return None

    def remove(self, value):  # There is a bug. Have to remove
        if self.root is None:
            return False

        current_node = self.root
        parent_node = None

        while current_node:
            if value < current_node["value"]:
                parent_node = current_node
                current_node = current_node["left"]
            elif value > current_node["value"]:
                parent_node = current_node
                current_node = current_node["right"]
            elif current_node["value"] == value:
                # we have a match, get to work!

                # Option 1: No right child
                if current_node["right"] is None:
                    if parent_node is None:
                        self.root = current_node["left"]
                    else:
                        # if parent > current value, make current left child a child of parent
                        if current_node["value"] < parent_node["value"]:
                            parent_node["left"] = current_node["left"]

                        # if parent < current value, make left child a right child of parent
                        elif current_node["value"] > parent_node["value"]:
                            parent_node["right"] = current_node["left"]

                # Option 2: Right child which doesn't have a left child
                elif current_node["right"]["left"] is None:
                    if parent_node is None:
                        self.root = current_node["left"]
                    else:
                        # current_node["right"]["left"] = current_node["left"]

                        # if parent > current, make right child of the left the parent
                        if current_node["value"] < parent_node["value"]:
                            parent_node["left"] = current_node["right"]
                        # if parent < current, make right child a right child of the parent
                        elif current_node["value"] > parent_node["value"]:
                            parent_node["right"] = current_node["right"]
                # Option 3: Right child that has a left child
                else:
                    # find the right child's left most child
                    left_most = current_node["right"]["left"]
                    left_most_parent = current_node["right"]

                    while left_most["left"] is not None:
                        left_most_parent = left_most
                        left_most = left_most["left"]

                    # Parent's left subtree is now left most's right subtree
                    left_most_parent["left"] = left_most["right"]
                    left_most["left"] = current_node["left"]
                    left_most["right"] = current_node["right"]

                    if parent_node is None:
                        self.root = left_most
                    else:
                        if current_node["value"] < parent_node["value"]:
                            parent_node["left"] = left_most
                        elif current_node["value"] > parent_node["value"]:
                            parent_node["right"] = left_most
                return True

    def breadth_first_search(self):
        current_node = self.root
        mylist = []
        queue = [current_node]

        while len(queue) > 0:
            current_node = queue[0]
            del queue[0]
            mylist.append(current_node["value"])
            if current_node["left"]:
                queue.append(current_node["left"])
            if current_node["right"]:
                queue.append(current_node["right"])

        return mylist

    def breadth_first_search_recursive(self, queue, array):
        if len(queue) == 0:
            return array

        current_node = queue[0]
        array.append(current_node["value"])
        del queue[0]

        if current_node["left"] is not None:
            queue.append(current_node["left"])

        if current_node["right"] is not None:
            queue.append(current_node["right"])

        return self.breadth_first_search_recursive(queue, array)

    def dfs_in_order(self):
        return traverse_in_order(self.root, [])

    def dfs_post_order(self):
        return traverse_post_order(self.root, [])

    def dfs_pre_order(self):
        return traverse_pre_order(self.root, [])


if __name__ == "__main__":
    my_bst = BinarySearchTree()
    my_bst.insert(9)
    my_bst.insert(4)
    my_bst.insert(6)
    my_bst.insert(20)
    my_bst.insert(170)
    my_bst.insert(15)
    my_bst.insert(1)
    print(json.dumps(my_bst.root, indent=4))
    print("BFS:")
    print(my_bst.breadth_first_search())
    print("BFS Recursive")
    print(my_bst.breadth_first_search_recursive([my_bst.root], []))
    print("DFS In Order")
    print(my_bst.dfs_in_order())
    print("DFS Pre Order")
    print(my_bst.dfs_pre_order())
    print("DFS Post Order")
    print(my_bst.dfs_post_order())


#      9
#   4     20
# 1  6  15  170

# BFS       = [9, 4, 20, 1, 6, 15, 170]
# DFS:
# 1. Inorder   = [1, 4, 6, 9, 15, 20, 170]
# 2. Preorder  = [9, 4, 1, 6, 20, 15, 170]
# 3. Postorder = [1, 6, 4, 15, 170, 20, 9]
