N = int(input())

prime = [True for i in range(N+1)]

#エラトステネスのふるい
for i in range(2, int(N**0.5)+1):
    if prime[i] == True:
        for j in range(2*i, N+1, i):
            prime[j] = False

ans = []
for i in range(2, N+1):
    if prime[i] == True:
        ans.append(i)

print(*ans)
