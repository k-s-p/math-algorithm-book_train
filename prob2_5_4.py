n = int(input())

for i in range(2, n+1):
    ok = True
    for j in range(i):
        if j > 1:
            if i%j == 0:
                ok = False
                break
    if ok:
        print(i, end='')
        if i == n+1:
            print('')
        else :
            print(' ', end='')

#回答例
# def isprime(N):
# 	for i in range(2, N):
# 		if N % i == 0:
# 			return False
# 	return True

# N = int(input())
# A = []
# for i in range(2,N+1):
# 	if isprime(i) == True:
# 		A.append(i)

# print(*A)