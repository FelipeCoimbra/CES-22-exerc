
def is_multiple(a,b):
    return a>=b and a%b == 0

assert is_multiple(12 ,3)
assert is_multiple(12, 4)
assert not is_multiple(12, 5)
assert is_multiple(12, 6)
assert not is_multiple(12, 7)
