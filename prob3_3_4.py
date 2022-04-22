#100円と400円の組み合わせ
#200円と300円の組み合わせを足す

N = int(input())

A = list(map(int, input().split()))

a, b, c, d = 0, 0, 0, 0 #100,200,300,400の数がそれぞれa,b,c,d
for i in A:
    if i == 100:
        a += 1
    elif i == 200:
        b += 1
    elif i == 300:
        c += 1
    elif i == 400:
        d += 1

ans = a*d + b*c
print(ans)