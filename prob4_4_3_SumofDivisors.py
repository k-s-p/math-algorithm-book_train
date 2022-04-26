#解法
#f(x)を1~Nまで用意し、1の倍数f(x)に＋１
#2の倍数f(2),f(4),...に+1
#3の倍数、4の倍数と、Nまで繰り返すと、各xに対するf(x)が求められる

N = int(input())

fx = [0 for i in range(N+1)]
for i in range(1, N+1):
    #iの倍数のxのf(x)に1を足す
    for j in range(i, N+1, i):
        fx[j] += 1

ans = 0
for i in range(1, N+1):
    ans += fx[i] * i

print(ans)