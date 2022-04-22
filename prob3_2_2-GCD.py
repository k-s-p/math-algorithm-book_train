
#ユークリッドの互除法を行う関数
def gcd(A, B):
    while A >= 1 and B >= 1:
        #大きい方を、大きい方割る小さいほうのあまりと置き換える
        if A > B:
            A = A % B
        else:
            B = B % A
    if A >= 1:
        return A
    else :
        return B

N = int(input())

A = list(input().split())
a, b = 0, 0
for i in range(N):
    if i == 0:
        a = int(A[i])
    else:
        b = int(A[i])
        a = gcd(a, b)

print(a)