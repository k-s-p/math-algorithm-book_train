def cal_comb(n, r):
    child = 1
    for i in range(r):
        child *= n-i
    mom = 1
    for i in range(r):
        mom *= i+1
    return int(child/mom)

n, r = map(int, input().split())

print(cal_comb(n, r))
