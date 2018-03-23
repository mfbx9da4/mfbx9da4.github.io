
factorials = [1,2]

def factorial(n):
  if len(factorials) > n:
    return factorials[n - 1]
  for i in range(len(factorials), n + 1):
    factorials.append((i + 1) * factorials[i - 1])
  return factorials[n - 1]

factorial(30)

def num_zeros(x):
  string = str(x)
  count = 0
  c = -1
  while string[c] == '0':
    count += 1
    c -= 1
  return count

for i, x in enumerate(factorials):
  print(i + 1, x, num_zeros(x))
