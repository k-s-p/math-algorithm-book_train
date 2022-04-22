N = int(input())

dp = [0 for i in range(N+1)]
for i in range(N+1):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N])