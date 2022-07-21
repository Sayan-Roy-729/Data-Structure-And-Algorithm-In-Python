boxes = [0, 1, 2, 3, 4, 5]

def logFirstTwoBoxes(boxes):
    print(boxes[0])  # O(1)
    print(boxes[1])  # O(1)

logFirstTwoBoxes(boxes)  # O(2) --> O(1) - Constant Time
