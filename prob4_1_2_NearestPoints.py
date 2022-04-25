#とりあえず、すべての点を調べる全探索でいく
import math

N = int(input())

P = [list(map(int, input().split())) for _ in range(N)]

ans = 10**15
for i in range(N-1):
    for j in range(i+1, N):
        #点iと点jの成分を求める
        IJx = P[i][0]-P[j][0]
        IJy = P[i][1]-P[j][1]
        #二点の距離を求める(ベクトルの大きさ)
        a = math.sqrt(IJx*IJx + IJy*IJy)
        ans = min(ans, a)
print(ans)