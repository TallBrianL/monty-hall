import random

N = pow(2, 18)
truth = [random.randrange(3) for _ in range(N)]
print(len(truth))
print(truth[1:10])

# guess 0

guess = [1 for _ in range(N)]
probability_first_guess = sum([x == y for x, y in zip(truth, guess)]) / len(truth)
print(probability_first_guess)

reveal = [0 for _ in range(N)]
for i, t in enumerate(truth):
    if t == 0:
        reveal[i] = random.randrange(2) + 1
    elif t == 1:
        reveal[i] = 2
    else:  # t == 2
        reveal[i] = 1

newGuess = [0 for _ in range(N)]
for i in range(N):
    if reveal[i] == 1:
        newGuess[i] = 2
    else:  # reveal 2
        newGuess[i] = 1

probability_new_guess = sum([x == y for x, y in zip(truth, newGuess)]) / len(truth)
print(probability_new_guess)
