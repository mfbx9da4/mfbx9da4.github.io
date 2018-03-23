# convert dict to json
#

import json

simple_types = set([int, float])

def solve_iter(obj):
  # couldn't work it out
  # https://stackoverflow.com/questions/49060962/convert-dict-to-json-iteratively-without-standard-libraries
  out = ''
  levels = {0: 1}
  stack = [(None, obj, 0, str(type(obj)))]
  path = []
  prev_level = -1
  while len(stack):
    key, val, level, obj_type = stack.pop()
    print(key, val, level, obj_type)

    while len(path) and len(path) > level:
      # jumped up, finish
      level -= 1
      last = path.pop()
      print('jumped up', path, last, cur_str_vals)
      res = "{\"" + str(last) + "\":" + cur_str_vals[0] + "}"
      cur_str_vals = [res]
      print(res)

    path.append(key)
    if type(val) is dict:
      cur_str_vals = []
      for key, val in val.items():
        stack.append((key, val, level + 1, 'dict'))
    elif type(val) is list:
      cur_str_vals = []
      for x in val:
        stack.append((None, x, level + 1, 'list'))
    elif type(val) in set([int, str, float]):
      # simple val
      str_val = '"' + str(val) + '"'
      print('leaf')
      cur_str_vals.append(str_val)
    else:
      raise "Unrecognized type"
    prev_level = level
  ans = [path[-1] + ':' + ','.join(cur_str_vals)]
  print(reduce_level(ans, dict))

def reduce_level(level_vals, level_type):
  val = ",".join(level_vals)
  if level_type == list:
    return "[" + val + "]"
  elif level_type == dict:
    return "{" + val + "}"
  else:
    raise "Not recognized type"

def solve(obj):
  out = ''
  obj_type = type(obj)
  if obj_type is dict:
    out += '{'
    for key, val in obj.items():
      out += '"' + str(key) + '"' + ':' + solve(val) + ','
    out = out[:-1] + '}'
  elif obj_type is list:
    out += '['
    for val in obj:
      out += solve(val) + ','
    out = out[:-1] + ']'
  elif obj is None:
    return 'null'
  elif obj_type is str:
    return '"' + str(obj) + '"'
  elif obj_type in simple_types:
    return str(obj)
  else:
    raise 'Dont recognize this type'
  return out

a = {
  'hi': 1,
  'b': "b",
  'x': ["b", "a"],
  'x': {"b": 1, "a": 2}
}

a = {
  'c': 'blah',
  'a': {
    'b': 'foo'
  }
}

print(json.loads(solve(a)))
print(solve_iter(a))
# print(json.loads(solve_iter(a)))
