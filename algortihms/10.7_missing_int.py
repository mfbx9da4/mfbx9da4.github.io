# An input file with four billion non-negative integers
# Generate an integer not contained by the file with 1GB of mem
# Follow up: what if all numbers are unique and you only
# have 10MB of memory
# p416

import random
import sys

max_64 = sys.maxsize
max_32 = 2**32 - 1

large_filename = 'large_number_of_ints.txt'
small_filename = 'small_number_of_ints.txt'
filename_32bit = '32bit_ints.txt'

#
# is it possible for 64 bit? =>
# 2**63 = 3 billion billion possible integers
#
# bit_vector = bytearray(array_size // 8)
# byte array overhead is 57 bytes
# each byte is then 1 byte after that


# bit_vector = bytearray((max_32 + 1) // 8)
# print(len(bit_vector))
# print(bit_vector[0])
# bit_vector[0] |=  1 << 5
# print(bit_vector[0])
# bit_vector |= 1 << 5
# print(bit_vector)

def solve(filename, largest_int):
  """
  Solve with large bit vector.
    - Create bit vector of length max_int_size
    - Set bit every time int found
    - Iterate through bit vector until first 0

  If we have 64 bit integers the bit vector would
  be too large to fit into mem. Instead we must
  pass through the data in ranges of about (2**32)
  or whatever our memory capacity for the bitvector
  is.
  """

  if largest_int > max_32:
    raise TypeError('Largest int should be less than ' + str(max_32))

  total = (largest_int + 1) # +1 for 0
  num_bytes = total // 8
  remainder = total % 8
  if remainder:
    num_bytes += 1
  print('total', total, num_bytes)
  bit_vector = bytearray(num_bytes)

  # create bit vector
  with open(filename) as file:
    for line in file:
      num = line.split('\n')[0]
      if num:
        num = int(num)
        index = num // 8
        remainder = num % 8
        bit_vector[index] |= 1 << remainder
        # TODO: special case of 0

  for i in range(1, largest_int + 1):
    index = i // 8
    remainder = i % 8
    has_bit = bit_vector[index] & 1 << remainder
    if has_bit == 0:
      return print('missing bit', i)


def write_random_ints(filename, number_of_ints=max_32, largest_int=max_32, chunk_size=100000):

  # TODO: ensure unique
  rand = lambda x: random.randint(x, largest_int)

  with open(filename, "w") as file:
    total = 0
    while total < number_of_ints:
      chunk = chunk_size
      if chunk_size + total > number_of_ints:
        chunk = number_of_ints - total
      total += chunk_size
      contents = ''.join(str(rand(i)) + '\n' for i in range(chunk))
      file.write(contents)
      prev = chunk
      print('Wrote', total, 'lines')

print(max_32)

def write_small_file(number_of_ints=100, largest_int=100):
  filename = small_filename
  chunk_size = 50
  write_random_ints(filename, number_of_ints=number_of_ints, \
    largest_int=largest_int, chunk_size=chunk_size)

def solve_small():
  largest_int = 10
  number_of_ints = 10
  write_small_file(number_of_ints=number_of_ints, largest_int=largest_int)
  solve(small_filename, largest_int)

def write_32_bit():
  largest_int = max_32
  number_of_ints = max_32
  write_random_ints(filename_32bit, number_of_ints=number_of_ints, largest_int=largest_int)

def solve_32_bit():
  largest_int = max_32
  solve(filename_32bit, largest_int)

# write_32_bit()
solve_32_bit()
