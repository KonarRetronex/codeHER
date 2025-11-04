# simple manual random integer generator (no import)

seed = id(object())  # use object id as a changing seed

def random_int(min_val, max_val):
    global seed
    # Linear Congruential Generator (LCG) formula
    seed = (seed * 1103515245 + 12345) % (2**31)
    # Scale to the desired range
    return min_val + seed % (max_val - min_val + 1)

# Example usage
for _ in range(1):
    print(random_int(1, 100))
