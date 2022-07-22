basket = ["apples", "grapes", "pears"]

"""
Structure of a linked list:

apples
8947  ---> grapes
           8742
                  ---> pears
                       372
                             ---> None

Tool to understand the topic: https://visualgo.net/en/list

Big O of Linked List:
1. prepend --> O(1) # add item at the beginning
2. append  --> O(1) # add item at the last
3. lookup  --> O(n)
4. insert  --> O(n)
5. delete  --> O(n)

Pros:
1. Fast Insertion
2. Fast Deletion
3. Ordered
4. Flexible Size

Cons:
1. Slow lookup
2. More Memory
"""