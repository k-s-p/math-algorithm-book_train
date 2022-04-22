N = int(input())

dp_t = [0 for i in range(N)]
H = list(map(int, input().split()))

for i in range(N):
    if i == 0:
        dp_t[i] = 0
    elif i == 1:
        dp_t[i] = abs(H[i-1] - H[i])
    else:
        #ひとつ前からジャンプする場合
        v1 = dp_t[i-1] + abs(H[i-1] - H[i])
        #二つ前からジャンプする場合
        v2 = dp_t[i-2] + abs(H[i-2] - H[i])

        dp_t[i] = min(v1, v2)

print(dp_t[N-1])