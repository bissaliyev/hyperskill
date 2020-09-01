import sys

sys.setrecursionlimit(10000)


def is_equal(a, b):
    if a == b or a == '.':
        return True
    return False


def match(re, st):
    if re == '$':
        if st:
            return False
        return True
    if not re:
        return True
    if not st:
        return False
    if re and st:
        # scenario for quantifier '?'
        if re[0] == '\\':  # escape symbol
            re = re[1:]
        if (re[0].isalpha() or re[0] == '.') and re[1:2] and re[1:2] in '?*+':
            if re[1:2] == '?':
                # preceding character occurs zero times
                if not is_equal(re[0], st[0]):
                    return match(re[2:], st)
                # preceding character occurs once
                elif is_equal(re[0], st[0]) and (len(st) > 1 and not is_equal(re[0], st[1]) or len(st) == 1):
                    return match(re[2:], st[1:])

            # scenario for quantifier '*'
            elif re[1:2] == '*':
                # preceding character occurs zero times
                if not is_equal(re[0], st[0]):
                    return match(re[2:], st)
                # preceding character occurs more than once
                elif is_equal(re[0], st[0]) and len(st) > 1 and is_equal(re[0], st[1]):
                    return match(re, st[1:])
                # preceding character occurs once
                elif is_equal(re[0], st[0]) and (len(st) > 1 and not is_equal(re[0], st[1]) or len(st) == 1):
                    return match(re[2:], st[1:])

            # scenario for quantifier '+'
            else:
                # preceding character occurs once
                if is_equal(re[0], st[0]) and st[0] != st[1:2]:
                    return match(re[2:], st[1:])
                # preceding character occurs more than once
                elif is_equal(re[0], st[0]) and st[0] == st[1:2] and is_equal(re[0], st[1:2]):
                    return match(re, st[1:])
        # default scenario
        else:
            if is_equal(re[0], st[0]):
                return match(re[1:], st[1:])
            else:
                return False


def match_all(re, st):
    if not re:
        return True
    if not st:
        return False
    while st:
        if match(re, st):
            return True
        else:
            st = st[1:]
    return False


def regex(re, st):
    if re.startswith('^') and re.endswith('$'):
        return match(re[1:], st)
    elif re.startswith('^'):
        return match_all(re[1:], st[:len(re[1:])])
    elif re.endswith('$'):
        return match_all(re[:-1], st[-len(re[:-1]):])
    else:
        return match_all(re, st)


re, st = input().split("|")
# re, st = "\\.$|end.".split("|")
print(regex(re, st))
