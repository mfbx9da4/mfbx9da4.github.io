def number_permutations(my_num, i, word='', words=[]):
    if i == len(my_num):
        words.append(word)
        return word
    else:
        for l in pad[my_num[i]]:
            number_permutations(my_num, i+1, word + l, words)
    return words


if __name__ == '__main__':
    pad = {
        "0": "0",
        "1": "1",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    my_num = '98358507'

    words = number_permutations(my_num, 0)
    f = open("/usr/share/dict/words")
    for word in f.xreadlines():
        for permutation in words:
            if word.find(permutation) > -1:
                print word
    f.close()

