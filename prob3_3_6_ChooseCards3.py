N = int(input())

A = list(map(int, input().split()))

#2つ選んで100000となる組み合わせを探す
cnt = [0 for i in range(100000)]
#A[i]の中の数字を数える
for i in range(N):
    cnt[A[i]] += 1

ans = 0
#答えを求める(組み合わせをかけて、足し合わせる)
for i in range(1, 50000):
    ans += cnt[i]*cnt[100000-i]
ans += (cnt[50000]*(cnt[50000]-1)) // 2
print(ans)