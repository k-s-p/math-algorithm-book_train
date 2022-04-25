#おそらく、階差をとってどうにかする
T = int(input())
N = int(input())

LR = [list(map(int, input().split())) for i in range(N)]
# print(LR)

#店員の増減の階差Biをとる
#-1からT+1までとっとく
B = [0 for i in range(T+3)]
#階差は、時刻Lに+1,時刻R+1に-1すればよい
for i in range(N):
    B[LR[i][0] + 1] += 1
    B[LR[i][1] + 1] -= 1
# print(B)
#階差の累積和をとる
A = [0 for i in range(T+1)]
A[0] = B[1]
for i in range(1, T+1):
    A[i] += A[i-1] + B[i+1] 

#出力
for i in range(T):
    print(A[i])