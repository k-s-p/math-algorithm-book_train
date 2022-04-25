#単純に積雪量を足していく方法だと時間がオーバーする
#なので、配列には階差をつかう
#つまり、区画iの積雪から区画i-1の積雪を引いた値を配列に格納していく
#これにより、前の区画とどれだけ差があるかを保持していくことができる。
#また、この階差に累積和をとると、積雪量になる

N, Q = map(int,input().split())

#区間lから区間rまでの積雪をxcm増加させる処理は、Blの値をx増加させ、Br+1の値をx減少させることと同じ
B = [0 for i in range(N+1)]
for i in range(Q):
    L,R,X = map(int,input().split())
    B[L-1] += X
    B[R] -= X

ans = []
for i in range(1,N):
    if B[i] > 0:
        ans.append('<')
    elif B[i] < 0:
        ans.append('>')
    else:
        ans.append('=')

print(''.join(ans))