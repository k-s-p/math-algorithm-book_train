import math

N = int(input())

anser = []

LIMIT = int(N ** 0.5)
for i in range(2, LIMIT + 1):
    while N%i == 0:
        N /= i
        anser.append(i)

if N >= 2:
    anser.append(int(N))

print(*anser)