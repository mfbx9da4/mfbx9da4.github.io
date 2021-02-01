def next_guess(g, N):
    return (g + (N / g)) / 2


def solve(n, max_iterations=100):
    prev_guess = None
    guess = n / 2
    i = 0
    while prev_guess != guess and i < max_iterations:
        prev_guess = guess
        guess = next_guess(guess, n)
        i += 1
    return guess


print(solve(9812, 1000))
