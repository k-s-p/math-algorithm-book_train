N, W = map(int, input().split())

Item = [list(map(int, input().split())) for _ in range(N)]

#配列の初期化
dp = [[None for j in range(W+1)] for i in range(N+1)]
dp[0][0] = 0
for i in range(1,W+1):
    dp[0][i] = -2**60

#動的計画法
for i in range(1, N+1):
    for j in range(W+1):
        #j<w_iのときは、一つの方法しか選択できない（その品物を選ぶことができない）
        if j < Item[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            #j>=w_iのときは、その品物をえらぶかどうか選択できる。
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-Item[i-1][0]] + Item[i-1][1])
    #print(dp[i])
print(max(dp[N]))