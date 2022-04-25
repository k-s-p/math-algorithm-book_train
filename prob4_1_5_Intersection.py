#cross()を求めることで、点C,Dが線分ABの上にあるか下にあるかを判定する
#上下にあるのなら、それは交差する
#また、点A,Bが線分CDの右にあるか左にあるかも判定
#両方を満たすとき、交わる

from operator import truediv


x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())
x4,y4 = map(int, input().split())

#crossを計算する関数
def cross(x_1, y_1, x_2, y_2):
    return x_1*y_2 - x_2*y_1

ABAC = cross(x2-x1, y2-y1, x3-x1, y3-y1)
ABAD = cross(x2-x1, y2-y1, x4-x1, y4-y1)
CDCA = cross(x4-x3, y4-y3, x1-x3, y1-y3)
CDCB = cross(x4-x3, y4-y3, x2-x3, y2-y3)

#全部が一直線の時は例外
if ABAC == ABAD == CDCA == CDCB == 0:
    A = (x1,y1) #点A
    B = (x2, y2)
    C = (x3,y3)
    D = (x4,y4)
    if A>B:
        tmp = B
        B = A
        A = tmp
    if C>D:
        tmp = D
        D = C
        C = tmp
    if max(A,C) <= min(B,D):
        print('Yes')
    else:
        print('No')
#普通の場合
else:
    IsAB = False #線分ABが点C,Dを分けるか？
    IsCD = False #線分CDが点A,Bを分けるか？
    if ABAC * ABAD <= 0:
        IsAB = True
    if CDCA * CDCB <= 0:
        IsCD = True
    
    #答え
    if IsAB == IsCD == True:
        print('Yes')
    else:
        print('No')