# A B
# A B A

# how many ways to add up to a number
# using numbers including and below it?

def ways_to_add(num, prev=None):
  out = []
  if not num: return out
  print('ways_to_add', num)
  for i in range(1, num + 1):
    tot = i
    rem = num - tot
    for j in ways_to_add(rem):
      print('ways_to_add', num, 'size', i, 'rem', rem, 'child', j)
      out.append([i, j])
  print('ways_to_add', num, 'self')
  out.append([num])
  return out

def ways_to_add2(num, prev=None):
  prev = [] if prev is None else prev
  print('ways_to_add', prev, num)
  if not num:
    print('end', prev)
    # print('prev.pop()', prev.pop())
    return
  for i in range(1, num + 1):
    prev.append(i)
    rem = num - i
    ways_to_add2(rem, prev)
    prev.pop()
  return prev

# print(ways_to_add(3))
print(ways_to_add2(3))

def ways(string):
  out = [wrap(string)]
  # for each size of first half
  for i in range(1, len(string), 2):
    left = wrap(string[:i])
    op = string[i]
    right = string[i+1:]

    # combine with each size of second half
    for way_r in ways(right):
      out.append(left + op + way_r)

  return out

def wrap(string):
  return '(' + string + ')'

def recurse(str, lo, hi):
  if lo >= hi - 1:
    return str
  for j in range(hi, 0, -2):
    print(str, lo, j, hi)
    if j < hi:
      print(wrap(str[lo:j]) + str[j] + recurse(str[j+1:], j+1, hi))
    else:
      print(wrap(str[lo:j]))
    # print(wrap(str[i:j]) + str[j] + recurse(str[j + 1:], j + 1))

  # # (all)^1
  # # (all-)rec(1^1)
  # print(wrap(str[i:len(str) - 2]) + str[len(str)-2] + recurse(str[len(str)-1:], len(str)-1))
  # # print(str[:i] + wrap(str[i:1]) + str[1:], i + 2)
  # # print(str[:i] + wrap(str[i:1]) + str[1:], i + 2)
  # # recurse(str[:i] + wrap(str[i:2]) + str[2:], i + 2)
  # suffix = ''
  # if i + 3 < len(str):
  #   suffix = str[i + 3:]
  # recurse(str[:i] + wrap(str[i:i + 3]) + suffix, i + 3)


string = '0^0^0^0^0^0'
string = '1^2'
string = '1^2^3'
string = '1^2^3^4'
# 0^0^0
# (0^0)^0
# 0^(0^0)

# recurse(string, 0, len(string))
for x in ways(string):
  print(x)

