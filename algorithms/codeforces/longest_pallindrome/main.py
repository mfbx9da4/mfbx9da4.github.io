"""
"""
from collections import defaultdict


def int_as_array(num): return list(map(int, [y for y in str(num)]))


def array_as_int(arr): return int(''.join(map(str, arr)))


def read_int(): return int(input())


def read_int_array(): return list(map(int, input().split(' ')))


def int_array_to_string(arr, sep=' '): return sep.join(map(str, arr))


def solve(array):
    single_pals = set()
    pair_pals = defaultdict(lambda: {'D': [], 'A': []})

    for word in array:
        reverse = word[::-1]
        key = min(word, reverse)
        if word == key:
            pair_pals[key]['A'].append(word)
        else:
            pair_pals[key]['D'].append(word)
        if reverse == word:
            single_pals.add(word)

    center = ''
    # find the first single pal which has an odd count and
    # put in the center
    for word in single_pals:
        # there will be no descending values for single pals
        all_words = pair_pals[word]['A']
        if len(all_words) % 2 == 1:
            center = ''.join(all_words)
            # avoid reusing these words again later
            del(pair_pals[word])
            break
    longest = [center]
    for key, words in pair_pals.items():
        asc = words['A']
        desc = words['D']
        total = len(asc) + len(desc)
        if total > 1:
            if key in single_pals:
                _total = total if total % 2 == 0 else total - 1
                all_words = asc
            else:
                sub_len = min(len(asc), len(desc))
                _total = sub_len * 2
                all_words = asc[:sub_len] + desc[:sub_len]
            mid = len(all_words) // 2
            longest = all_words[:mid] + longest + all_words[mid:_total]
    ans = ''.join(longest)
    print(len(ans))
    print(ans)


N, M = read_int_array()
words = []
for i in range(N):
    words.append(input())
solve(words)
