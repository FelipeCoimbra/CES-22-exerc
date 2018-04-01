import string
import re

def cleanword(s):
    new_str = ""
    for c in s:
        if c.isalpha():
            new_str += c
    return new_str


def has_dashdash(s : string):
    pos = s.find("--")
    if pos > 0:
        return True
    return False


def extract_words(s):
    a = re.split("[^a-zA-Z]+", s)
    if len(a[len(a)-1]) == 0:
        a.pop()
    for i in range(0, len(a)):
        a[i] = a[i].lower()
    return a


def wordcount(word, words):
    count = 0
    for w in words:
        if w == word:
            count = count+1
    return count


def wordset(words):
    s = set()
    a = []
    for word in words:
        s.add(word)
    for word in s:
        a.append(word)
    a.sort()
    return a


def longestword(words):
    ans = 0
    for word in words:
        if len(word) > ans:
            ans = len(word)
    return ans

