import math
def create_m(gakuseki, p, q):
    n = p*q
    m = gakuseki % (n-2)
    return m


#   最小公倍数を求める(ほんとはlcmにしたい)
def sc(a, b):
    return math.lcm(a-1, b-1)


def gc(b):
    for i in range(1,b+1):
        h = math.gcd(i, b)
        if h == 1:
            return i

if __name__ == '__main__':
    #   学籍番号
    gakuseki = 23048
    p = 19
    q = 31
    
    #   平文mを作る
    m = create_m(gakuseki, p, q)
    print("平文m:" + str(m))
    
    #   最小公倍数を求める
    sc1 = sc(p, q)
    print("最小公倍数:" + str(sc1))
    
    #   最大公約数が1となるe
    e = gc(sc1)
    print("eの値:" + str(e))
    
    d = 1 % sc1
    print("dの値:" + str(d))
    