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
    print('Treasure at', treasure_tuple, 'in a', rows, 'by', cols, 'grid')
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
      raise ValueError('Treasure out of range')

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

def guesser(val, fixed_row=0, fixed_col=None):
  if fixed_col is None and fixed_row is None:
    raise ValueError('Should provide either fixed_col or fixed_row')

  if fixed_col is not None:
    guess = (val, fixed_col)
  else:
    guess = (fixed_row, val)

  res = game.guess(guess)
  if res == HOTTER:
    print('guess', guess, 'hotter')
  else:
    print('guess', guess, 'colder')
  return res

def solve(game):
  first_row = 0

  # find col
  res = bisect_dimension(game, 0, game.cols - 1, fixed_row=first_row)
  found_treasure, final_col = res
  if found_treasure:
    print('YAY', (first_row, final_col))
    return (first_row, final_col)

  # find row
  res = bisect_dimension(game, 0, game.rows - 1, fixed_col=final_col)
  found_treasure, final_row = res
  print('YAY', (final_row, final_col))
  return (final_row, final_col)

def bisect_dimension(game, lo, hi, fixed_row=None, fixed_col=None):
  first_iteration = True
  prev = lo
  # prev_was_colder forces first guess at lower bound
  # and second guess at higher bound. This is so we can
  # bisect the range.
  prev_was_colder = True
  prev_was_lo_bound = False

  count = 0

  while hi > lo:
    count += 1
    if count > 10:
      raise ValueError('Too many')
    width = (hi - lo)
    mid = (width // 2) + lo
    guess = mid

    if prev_was_lo_bound:
      # guess at the other edge to bisect
      guess = hi
      prev_was_lo_bound = False
    elif prev_was_colder:
      # reset signal. start from lower bound
      guess = lo
      prev_was_lo_bound = True
    elif guess == prev:
      # edge case where mid of three values
      # is always the same
      guess = lo

    # make guess
    res = guesser(guess, fixed_row, fixed_col)

    if res == YAY: return True, guess

    is_hotter = res == HOTTER
    is_colder = res == COLDER

    # If prev was colder, next guess must be hotter.
    # So we have no info to adjust bounds.
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
treasure_tuple = (3, 15)
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
