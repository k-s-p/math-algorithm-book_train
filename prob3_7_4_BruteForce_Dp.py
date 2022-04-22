N, S = map(int, input().split())
A = list(map(int, input().split()))

#初期化
dp = [[False for j in range(S+1)] for i in range(N+1)]
dp[0][0] = True

#動的計画法で解ける
for i in range(1, N+1):
    for j in range(S+1):
        if j < A[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
                dp[i][j] = True

ans = dp[N][S]
if ans:
    print('Yes')
else:
    print('No')