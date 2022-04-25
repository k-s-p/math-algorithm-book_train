#累積和を求めてから、駅Bj - Bj-1の距離を足し合わせたら答えになる?

N = int(input())
A = list(map(int, input().split()))

#駅の距離の累積和
S = [0 for i in range(N)]
for i in range(1, N):
    S[i] += S[i-1] + A[i-1]
# print(S)

M = int(input())
a = int(input()) #太郎君が最初にいた駅
ans = 0
for i in range(1, M):
    b = int(input())
    ans += abs(S[b-1] - S[a-1]) #太郎君が今いる駅までの距離と前にいた駅の距離の差を足す
    a = b
#input()
print(ans)
