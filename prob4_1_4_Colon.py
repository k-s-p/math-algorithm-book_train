#三角関数を用いて座標を求める
#座標は、(cosθ,sinθ)

import math


A,B,H,M = map(int,input().split())
PI = math.pi
PLx = math.cos((30*H + 0.5*M) * PI/180)*A
PLy = math.sin((30*H + 0.5*M) * PI/180)*A
PTx = math.cos(6*M * PI/180)*B
PTy = math.sin(6*M * PI/180)*B

#距離を求める
ans = math.sqrt((PLx-PTx)*(PLx-PTx) + (PLy-PTy)*(PLy-PTy))
print(ans)