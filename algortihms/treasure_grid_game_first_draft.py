import pprint

# Cruise Interview
# treasure finding cave
# 2d board = array of arrays => chars
# num rows, num cols
# treasure position (row, col)
# all positions hidden, player reveals positions
# player starts where he wants

# betting site, find treasure on board
# moves to next user

HOTTER = 0
COLDER = 1
YAY = 2

class Game():
  def __init__(self, treasure_tuple, rows, cols):
    print("TREASURE", treasure_tuple, (rows, cols))
    self.printer = pprint.PrettyPrinter(indent=4).pprint
    self.cols = cols
    self.rows = rows
    self.last_diff_row = None
    self.last_diff_col = None
    self.is_first_guess = True
    self.board = [[0 for col in range(cols)] for row in range(rows)]
    if self.in_range(treasure_tuple):
      self.treasure_tuple = treasure_tuple
    else:
      raise ValueError("Treasure out of range")

  def in_range(self, pos):
    row, col = pos
    return row >= 0 and col >= 0 and row < self.rows and col < self.cols

  def _print(self):
    self.printer(self.board)

  def guess(self, guess_tuple):
    if self.in_range(guess_tuple):
      row, col = guess_tuple
      self.board[row][col] = 1
      # self._print()
      t_row, t_col = self.treasure_tuple
      d_row, d_col = abs(t_row - row), abs(t_col - col)
      cur_diff = d_row + d_col
      if cur_diff == 0:
        return YAY
      message = HOTTER
      if not self.is_first_guess:
        last_diff = self.last_diff_row + self.last_diff_col
        if last_diff < cur_diff:
          message = COLDER
      else:
        self.is_first_guess = False
      self.last_diff_row = d_row
      self.last_diff_col = d_col
      return message


def center(bounds):
  # guess in center of bounds
  mid_row = ((bounds['south'] - bounds['north']) // 2) + bounds['north']
  mid_col = ((bounds['right'] - bounds['left']) // 2) + bounds['left']
  return mid_row, mid_col

def solve2(game):
  bounds = {
    'north': 0,
    'south': game.rows,
    'left': 0,
    'right': game.cols
  }
  prev_row, prev_col = (0,0)
  res = game.guess((prev_row, prev_col))
  if res == YAY:
    return (prev_row, prev_col)
  count = 0
  while True:
    count += 1
    if count > 2: return
    row, col = center(bounds)
    print(row, col)
    res = game.guess((row, col))
    if res == YAY:
      print(YAY, row, col)
      return (row, col)
    is_hotter = res == HOTTER
    is_colder = not is_hotter
    is_above = row < prev_row
    is_below = not is_above
    is_left = col < prev_col
    is_right = not is_left
    mid_col = (abs(col - prev_col) // 2) + min(col, prev_col)
    mid_row = (abs(row - prev_row) // 2) + min(row, prev_row)
    print('is_hotter', is_hotter, 'is_colder', is_colder, 'is_above', is_above, 'is_below', is_below, 'is_left', is_left, 'is_right', is_right)

    if (is_hotter and is_above) or (is_colder and is_below):
      bounds['south'] = mid_row
      print('south', bounds['south'])
    elif (is_hotter and is_below) or (is_colder and is_above):
      bounds['north'] = mid_row + 1
      print('north', bounds['north'])

    if (is_hotter and is_left) or (is_colder and is_right):
      bounds['right'] = mid_col
    elif (is_hotter and is_right) or (is_colder and is_left):
      bounds['left'] = mid_col + 1
    prev_row = row
    prev_col = col

def solve3(game):
  final_row, final_col = bisect_cols(game)
  if final_row is not None:
    print('YAY found in first row', final_row, final_col)
    return final_row, final_col
  print('COL', final_col)
  final_row = bisect_rows(game, final_col)
  print('YAY found', (final_row, final_col))
  return final_row, final_col

def bisect_rows(game, final_col):
  # guess other edge
  # if hotter move row++ lo_row to mid
  # if colder move row-- hi_row to mid
  # if down to last two columns
  # return the other
  first_iteration = True
  lo_row = 0
  hi_row = game.rows - 1

  while hi_row - lo_row > 1:
    width = hi_row - lo_row
    mid = (width // 2) + lo_row

    if first_iteration:
      guess = (hi_row, final_col)
      first_iteration = False
    else:
      guess = (hi_row, mid)
  return None


def solve(game):
  guess_set = set()
  # TODO: move to external and refactor to one
  def guess(fixed_col=None):
    def _guess(val):
      guess = (val, fixed_col) if fixed_col is not None else (0, val)
      # TODO: remove, for debugging only
      if guess in guess_set:
        print('Warning: Already guessed')
      guess_set.add(guess)
      res = game.guess(guess)
      if res == HOTTER:
        print('guess', guess, 'hotter')
      else:
        print('guess', guess, 'colder')
      return res
    return _guess

  found_treasure, final_col = bisect_dimension(game, guess(), 0, game.cols - 1)
  print("FINAL COL", final_col)
  if found_treasure:
    print("YAY", (0, final_col))
  found_treasure, final_row = bisect_dimension(game, guess(final_col), 0, game.rows - 1)
  print("YAY", (final_row, final_col))
  return (final_row, final_col)

def bisect_dimension(game, guesser, lo, hi):
  # first guess at origin
  # origin = (0, 0)
  # print('guess', origin)
  # res = game.guess(origin)
  # if res == YAY:
  #   return (0,0)

  first_iteration = True
  prev = lo
  # TODO: refactor, prev_was_colder should be true
  prev_was_lo_bound = False
  prev_was_colder = True
  count = 0
  while hi > lo:
    # TODO: remove
    count += 1
    if count > 10:
      return
    width = hi - lo
    mid = (width // 2) + lo
    guess = mid

    if prev_was_lo_bound:
      # guess at the other edge to bisect
      guess = hi
      prev_was_lo_bound = False
    elif prev_was_colder:
      guess = lo
      prev_was_lo_bound = True
    elif guess == prev:
      print('Warning about to try', guess)
      guess = lo

    # make guess
    res = guesser(guess)

    if res == YAY: return True, guess

    is_hotter = res == HOTTER
    is_colder = res == COLDER

    # If prev was colder, next guess must be hotter.
    # So we have no info to adjust bounds
    if not prev_was_colder:
      prev_was_higher = guess < prev
      prev_was_lower = not prev_was_higher
      mid_guess_to_prev = ((prev - guess) // 2) + guess
      mid_prev_to_guess = ((1 + guess - prev) // 2) + prev

      if is_hotter and prev_was_higher:
        # equidistant is hotter
        hi = mid_guess_to_prev
      elif is_hotter and prev_was_lower:
        lo = mid_prev_to_guess
      elif is_colder and prev_was_higher:
        lo = mid_guess_to_prev + 1
      elif is_colder and prev_was_lower:
        hi = mid_prev_to_guess - 1

    prev = guess
    prev_was_colder = is_colder
    print('lo, hi', lo, hi)

  return False, lo


def bisect_dimension_draft(game, guesser, lo, hi):
  first_iteration = True
  prev = lo
  while hi - lo > 1:
    width = hi - lo
    mid = (width // 2) + lo
    guess = mid

    if first_iteration:
      # ensure first guess is at edge
      guess = hi
      first_iteration = False

    # make guess
    res = guesser(guess)

    if res == YAY: return True, guess
    if res == HOTTER and prev < guess:
      # equidistant is hotter
      mid_to_guess = ((guess - lo) // 2) + lo
      hi = mid_to_guess
      lo = guess
    elif res == HOTTER and prev > guess:
      mid_to_guess = ((guess - lo) // 2) + lo
      lo = mid_to_guess
      lo = guess
    elif res == COLDER and prev < guess:
      hi = guess - 1
    elif res == COLDER and prev > guess:
      lo = guess + 1
    prev = guess
    print('lo, hi', lo, hi)

  # down to last two columns
  # choose the hotter column

  if hi - lo == 0:
    return False, lo

  # TODO: can we avoid this final case?
  # TODO: need to ensure guess is in right column for hotness
  # of the row
  res_lo = guesser(lo)
  if res_lo == YAY: return True, lo
  res_hi = guesser(hi)
  if res_hi == YAY: return True, hi
  if res_hi == HOTTER:
    return False, hi
  return False, lo


print('## 1x1')
treasure_tuple = (0, 0)
game = Game(treasure_tuple, 1, 1)
assert solve(game) == treasure_tuple

print('## 2x2, at extreme')
treasure_tuple = (1, 1)
game = Game(treasure_tuple, 2, 2)
assert solve(game) == treasure_tuple

print('## 7x7, at extreme')
treasure_tuple = (2, 3)
game = Game(treasure_tuple, 7, 7)
assert solve(game) == treasure_tuple

print('## 15x17, in top left region')
treasure_tuple = (2, 1)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple

print('## 15x17, in top left extreme')
treasure_tuple = (0, 0)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple

print('## 15x17, in top right region')
# TODO: change to 15
treasure_tuple = (3, 16)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple

print('## 15x17, in top right extreme')
treasure_tuple = (0, 16)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple

print('## 15x17, in bottom left region')
treasure_tuple = (12, 2)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple

print('## 15x17, in bottom left extreme')
treasure_tuple = (14, 0)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple

print('## 15x17, in bottom right region')
treasure_tuple = (13, 15)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple

print('## 15x17, in bottom right extreme')
treasure_tuple = (14, 16)
game = Game(treasure_tuple, 15, 17)
assert solve(game) == treasure_tuple
