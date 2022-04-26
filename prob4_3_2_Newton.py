r = 2 #√2を求めるため
a = 2 #適当に決めた初期値

N = 10
for i in range(N):
    #点(a,f(a))における接線を求める
    zahyo_x = a
    zahyo_y = a*a*a

    #接線の式を求める(y = katamuki*x + sessen_b)
    katamuki = 3.0 * zahyo_x * zahyo_x
    sessen_b = zahyo_y - katamuki * zahyo_x

    #次のaの値next_aを求める
    next_a = (r-sessen_b) / katamuki
    print(next_a)
    a = next_a
