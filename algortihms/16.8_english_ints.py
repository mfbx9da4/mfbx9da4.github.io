nums = {
  3: 'three',
  2: 'two',
  1: 'one',
  0: 'zero'
}

tens = {
  20: 'twenty',
  30: 'thirty'
}

magnitudes = {
  100: 'hundred',
  1000: 'thousand',
  1000000: 'million',
  1000000000: 'billion'
}

def print_num(num):
  out = []
  queue = [num]
  while len(queue):
    num = queue.pop()
    if type(num) == str:
      out.insert(0, num)
      continue
    if num < 10:
      out.insert(0, nums[num])
      continue
    if num < 100:
      times = num // 10
      queue.append(tens[times * 10])
      queue.append(num % 10)
      continue
    for m, string in magnitudes.items():
      if num > m:
        mag = m
        mag_str = string
    times = num // mag
    rem = num % mag
    print(num, mag, rem)
    queue.append(times)
    queue.append(mag_str)
    if rem:
      queue.append(rem)
  print(out)


print_num(3200032)
