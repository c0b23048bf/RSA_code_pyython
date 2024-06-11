import math

def create_m(gakuseki, p, q):
    n = p*q
    m = gakuseki % (n-2)
    if m == 456:    # 今回は特別にこれを追加(gptじゃないヨ)(完璧主義)
        m = 457
    return m


# 最小公倍数を求める(ほんとはlcmにしたい)
def sc(a, b):
    return math.lcm(a-1, b-1)


# 最大公約数を用いて、1の時にeの値を考える
def gc(b):
    for i in range(1,b+1):
        h = math.gcd(i, b)
        if i == 1:
            continue
        if h == 1:
            return i


# dの値を作る
def mk_d(e, sc1):
    for i in range(1, 100000):
        if (i * e-1)%sc1 == 0:
            return i
        

# 暗号化
def anngouka(m, e, n):
    r_l = []
    s_m = m
    for i in range(1,e):  # 本当はこんなことしたくない(m**eでおわる)
        m *= s_m
        r_l.append(m)
        
    print(f"{s_m}の{e}乗の過程をリスト抽出")
    print(r_l)
    
    return m % n


# 復号化
def hukugouka(d, n, c):
    r_l = []
    s_c = c
    for i in range(1,d):  # 本当はこんなことしたくない(c**dでおわる)
        c *= s_c
        r_l.append(c)
    print(f"{s_c}の{d}乗の過程をリスト抽出")
    print(r_l)
    
    return c % n


if __name__ == '__main__':
    # 学籍番号
    gakuseki = 23048
    p = 19
    q = 31
    
    # 平文mを作る
    m = create_m(gakuseki, p, q)
    
    # 最小公倍数を求める
    sc1 = sc(p, q)
    n = p*q
    
    # 最大公約数が1となるe
    e = gc(sc1)
    
    # 値dを求める
    d = mk_d(e, sc1)
    
    print("平文m:" + str(m) + " 最小公倍数:" + str(sc1) + \
        " eの値:" + str(e) + " dの値:" + str(d) + "\n")
    
    print("秘密鍵: d = " + str(d))
    print("公開鍵: e = " + str(e) + ", n = " + str(n))
    print("平文:   m = " + str(m) + "\n")
    
    print("------------ここから暗号化-------------")
    
    # 暗号化
    c = anngouka(m, e, n)
    print("暗号:" + str(c))
    
    print("------------ここから復号化-------------")
    
    # 復号化
    h_m = hukugouka(d, n, c)
    print("復号:" + str(h_m) + "\n")
    
    if m == h_m:
        print("復号化成功！！！")
    else:
        print("エラーがあります！！！")