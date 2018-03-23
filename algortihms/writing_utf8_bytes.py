#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convert_to_bits(integer):
  digit = 16
  bits = []
  while digit != 0:
    if digit == 1:
      digit = 0
    else:
      digit = digit // 2

    bit_val = 2 ** digit

    if integer // bit_val:
      bits.append(1)
    else:
      bits.append(0)

    integer = integer % bit_val
  print(bits)
  return ''.join(str(x) for x in bits)

with open('/tmp/output', 'wb') as f:
  f.write(bytes('😊', 'utf-8'))
with open('/tmp/output', 'rb') as f:
  print(f.read())
with open('/tmp/output', 'r') as f:
  print(f.read())
with open('/tmp/output', 'wb') as f:
  my_bytes = b'\xf0\x9f\x98\x8a'
  assert my_bytes == bytes('😊', 'utf-8')
  bits = ''
  # convert to bits
  for integer in my_bytes:
    bits += convert_to_bits(integer)
    print(integer, bits)
  # convert to number
  # number = int(bits, 2)
  # print(number)
  print(int(bits, 2).to_bytes(4, 'little'))
  f.write(int(bits, 2).to_bytes(4, 'little'))
with open('/tmp/output', 'r') as f:
  print(f.read())
