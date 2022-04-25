#累積和を先に求める,
#その後、R1日目までの合計 - L1日目までの合計で質問の答えがでる

N, Q = map(int, input().split())
A = list(map(int, input().split()))

#累積和の計算
B = [0 for i in range(N+1)]
for i in range(1,N+1):
    B[i] += B[i-1] + A[i-1]

for i in range(Q):
    L,R = map(int, input().split())
    ans = B[R] - B[L-1]
    print(ans)