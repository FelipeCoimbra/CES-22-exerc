

def is_palindrome(string):
    for i in range(0, len(string)):
        if string[i] != string[len(string)-(i+1)]:
            return False
    return True

assert is_palindrome("abba")
assert not is_palindrome("abab")
assert is_palindrome("tenet")
assert not is_palindrome("banana")
assert is_palindrome("straw warts")
assert is_palindrome("a")
