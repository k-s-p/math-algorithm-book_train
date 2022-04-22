N = int(input())

A = list(map(int, input().split()))

#初期化
dp = [None for i in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    if i == 1:
        dp[i] = A[i-1]
    else:
        #i日目は、２日前の実力にi日目の上昇値を足す
        #または、一日前の上昇値の大きいほう
        dp[i] = max(dp[i-2] + A[i-1], dp[i-1])

print(dp[N])