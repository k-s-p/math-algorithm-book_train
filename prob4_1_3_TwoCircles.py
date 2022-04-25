#２点の距離が、r1+r2なら4、r1+r2より大きいなら5だと思う
#２点の距離が、|r1-r2|なら2, |r1-r2|より小さいなら1だと思う
import math
x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

#2点の距離P1P2を求める
P1P2 = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

if P1P2 == r1+r2:
    print('4')
elif P1P2 > r1+r2:
    print('5')
elif P1P2 < abs(r1-r2):
    print('1')
elif P1P2 == abs(r1-r2):
    print('2')
else:
    print('3')