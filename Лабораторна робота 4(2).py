s = input()

if s:
    first = s[0]
    target_lower = first.lower()
    target_upper = first.upper()

    rest = s[1:]
    rest = rest.replace(target_lower, "*HIDE*")
    rest = rest.replace(target_upper, "*HIDE*")

    print(first + rest)