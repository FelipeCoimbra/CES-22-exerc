
def scalar_mult(a, b):
    new_vec = []
    for i in range(len(b)):
        new_vec.append(a*b[i])
    return new_vec


assert scalar_mult(5, [1, 1]) == [5, 5]
assert scalar_mult(3, [1, 0, -1]) == [3, 0, -3]
assert scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14]
