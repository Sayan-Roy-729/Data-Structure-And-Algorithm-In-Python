# Create a function that reverses a string:
# "Hi My name is Sayan" should be:
# "nayaS si eman yM iH"

def reverse(string: str) -> str:
    # check input
    if string == None or type(string) != str or len(string) < 2:
        raise Exception("hmm that is not good")

    # method 1 --> O(n) time complexity
    # rev_string = ""
    # for i in range(len(string) - 1, -1, -1):
    #     rev_string += string[i]

    # method 2 --> O(n) time complexity
    return string[::-1]

    # method 3 - O(n) time complexity
    # backwards  = []
    # totalItems = len(string) - 1

    # for i in range(totalItems, -1, -1):
    #     backwards.append(string[i])

    # return "".join(backwards)

if __name__ == "__main__":
    print(reverse("Hi My name is Sayan"))
    # print(reverse(40))
