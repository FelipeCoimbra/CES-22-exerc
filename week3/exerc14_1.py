
def fa(a,b):
    s = set()
    lst = []
    for item in b:
        s.add(item)
    for item in a:
        if item in s:
            lst.append(item)

    return lst


def fb(a, b):
    s = set()
    lst = []
    for item in b:
        s.add(item)
    for item in a:
        if item not in s:
            lst.append(item)

    return lst


def fc(a, b):
    s = set()
    lst = []
    for item in a:
        s.add(item)
    for item in b:
        if item not in s:
            lst.append(item)

    return lst


def fd(a, b):
    sa = set()
    sb = set()
    lst = []
    for item in a:
        sa.add(item)
    for item in b:
        sb.add(item)
    for item in a:
        if item not in sb:
            lst.append(item)
    for item in b:
        if item not in sa:
            lst.append(item)

    return lst


def fe(a, b):
    s = set()
    lst = []
    for item in b:
        s.add(item)
    for item in a:
        if item not in s:
            lst.append(item)
        else:
            s.discard(item)

    return lst
