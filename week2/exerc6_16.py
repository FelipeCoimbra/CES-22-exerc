
def is_factor(a,b):
    return b>=a and b%a == 0

assert is_factor(3, 12)
assert not is_factor(5,12)
assert is_factor(7,14)
assert not is_factor(7,15)
assert is_factor(1,15)
assert is_factor(15,15)
assert not is_factor(25,15)
