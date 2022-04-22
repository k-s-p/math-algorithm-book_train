#赤:xC2,黄:yC2,青:zC2として足す

N = int(input())
A = list(map(int, input().split()))

x, y, z = 0, 0, 0

for i in A:
    if i == 1:
        x += 1
    elif i == 2:
        y += 1
    elif i == 3:
        z += 1

ans = (x*(x-1))/2 + (y*(y-1))/2 + (z*(z-1))/2

print(int(ans))