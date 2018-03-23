def solve(items, total_weight):
  memoized = [0 for x in range(total_weight + 1)]
  for item in items:
    weight, value = item
    print('weight, value', weight, value)

    for j in range(weight, total_weight + 1):
      exisiting_best_value = memoized[j]

      look_ahead = j - weight
      if look_ahead > 0:
        # get the solved sub problem for the remainder
        sub_problem_remainder = memoized[look_ahead]
        combined_solution = sub_problem_remainder + value
      else:
        # no combined solution possible
        combined_solution = -1

      best_value = max(combined_solution, value)

      if best_value > exisiting_best_value:
        memoized[j] = best_value

  return memoized[-1]

items = [
  (1, 10),
  (1, 10),
  (3, 40),
  (1, 10)
]
total_weight = 4

print(solve(items, total_weight))
