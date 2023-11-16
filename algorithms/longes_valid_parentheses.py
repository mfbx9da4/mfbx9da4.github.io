def solve(s: str):
    i = 0
    best_length = 0
    while i < len(s):
        i = consume_invalid(s, i)
        i, length = consume_valid_section(s, i)
        best_length = max(best_length, length)
        i += 1
    return best_length


def consume_invalid(s, i):
    while i < len(s) and s[i] == ')':
        i += 1
    return i


def consume_valid_section(s, i):
    depth = 0
    sections = {0: [i, None]}
    best_section = 0
    while i < len(s):
        c = s[i]
        if c == '(':
            sections[depth] = sections.get(depth, [i, None])
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == -1:  # transitioned to invalid section
                break
            if depth in sections:
                if depth + 1 in sections:
                    # we've found a longer substring so discard child
                    sections.pop(depth + 1)
                sections[depth][1] = i + 1
                open, close = sections[depth]
                best_section = max(close - open, best_section)
        i += 1
    return i, best_section


# print(solve("((((((()))))())"))
# print(solve("()))()"))
# print(solve("((()))"))
# print(solve("()"))
# print(solve("()))()()"))
# print(solve("((("))
# print(solve("))))))))((((((((()))))))))"))
# print(solve("()((())()"))
print(solve("(())()(()(("))
