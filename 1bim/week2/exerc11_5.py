
def add_vectors(a, b):
    new_vec = []
    for i in range(len(a)):
        new_vec.append(a[i]+b[i])
    return new_vec


assert add_vectors([1, 1], [1, 1]) == [2, 2]
assert add_vectors([1, 2], [1, 4]) == [2, 6]
assert add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4]
