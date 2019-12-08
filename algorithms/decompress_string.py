# https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#code-challenge


def create_brackets_map(input):
    # could use regex to speed up?
    open_to_close = {}
    openers = []
    for i, c in enumerate(input):
        if c == '[':
            openers.append(i)
        elif c == ']':
            open_to_close[openers.pop()] = i
    return open_to_close


def decompress(input):
    open_to_close = create_brackets_map(input)
    out = _decompress(input, 0, len(input), open_to_close)
    return out


def _decompress(input, lo, hi, open_to_close):
    print('input', input[lo:hi])
    state = "outer"

    outer_number = ''
    inner_value = ''
    result = ''

    i = lo
    while i < hi:
        char = input[i]
        if state == "outer":
            if char.isdigit():
                outer_number += char
            elif char == '[':
                state = "inner"
            else:
                mul = 1 if outer_number == '' else int(outer_number)
                result += mul * char
                outer_number = ''
        elif state == "inner":
            close_index = open_to_close[i - 1]
            inner_value = _decompress(input, i, close_index, open_to_close)
            state = "outer"
            result += int(outer_number) * inner_value
            outer_number = ''
            inner_value = ''
            i = close_index
        i += 1

    return result


print('==> "2b"')
assert decompress("2b") == 'bb'
print('==> "2ba"')
assert decompress("2ba") == 'bba'
print('==> "2c3[ab]d"')
assert decompress("2c3[ab]d") == 'ccabababd'
print(decompress("x2[a2[b]c]"))
assert decompress("x2[a2[b]c]") == 'xabbcabbc'

