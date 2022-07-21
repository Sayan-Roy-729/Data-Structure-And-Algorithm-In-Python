nemo = ["nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt", "darla", "hank"]
large = ["nemo" for i in range(10000)]

def findNemo(array):
    for i in range(len(array)):
        if array[i] == "nemo":
            print("Found NEMO!")
            break


findNemo(large)  # O(n) --> Linear Time
