import math

def create_m(gakuseki, p, q):
    n = p*q
    m = gakuseki % (n-2)
    mm = gakuseki//(n-2)
    if m == 456:    # 今回は特別にこれを追加(gptじゃないヨ)(完璧主義)
        m = 457
    return m+2, mm


# 最小公倍数を求める(ほんとはlcmにしたい)
def sc(a, b):
    return math.lcm(a-1, b-1)


# 最大公約数を用いて、1の時にeの値を考える
def gc(b):
    for i in range(1,b+1):
        h = math.gcd(i, b)
        if i == 1:  # 1だと課題書く上であんまりよくない
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
    # print(s_m**e == m)
    # if s_m**e == m:
    #     print("この掛け算(筆算)は適切に処理されています")
    # else:
    #     print("この掛け算(筆算)は間違っています")
    
    seikaim = m//n  # 正解値の計算
    seikainm = m%n  # 正解値の計算
    mstr = str(m)   # mのstring
    l = len(str(n)) # ビット数
    waru_dict = []  # 引き算を用いた割り算の筆算の実行結果
    waru_dict_count = []
    waru_dict_count_all = []
    count = 0        # 何回引いたか
    f1 = 0
    while True:
        # 引かれる数先頭の引く数ビット文が引く数よりも大きいとき
        if int(mstr[0:l]) > n:
            a = int(mstr[0:l])
            
            # 割り算の筆算を行うための引き算実行部
            while True:
                count += 1   # if文の中で一回引き算をするので引き算の回数+1
                # n(引く数)よりも割り算の引き算部分が大きいかどうか
                if a-n < n:
                    mstr = str(a-n) + mstr[l:len(mstr)]
                    waru_dict.append(int(mstr))
                    waru_dict_count.append(count)
                    waru_dict_count_all.append(str(count))
                    #print(str(a-n),mstr,count)
                    count = 0
                    l = len(str(n))
                    
                    # 商が0であるときの処理
                    if len(mstr) == len(str(n)):
                        if int(mstr) < n:
                            if f1 == 1:
                                waru_dict_count.append("0")
                                waru_dict_count_all.append("0")
                    f1 = 0
                    if len(mstr) > len(str(n)):
                        if int(str(a-n) + mstr[l-1:l+1-1]) < n: # 筆算において次の数を割られる数に足しても割る数の大きさに満たない場合
                            if len(str(a-n)) < len(str(n)): # どれだけ0を入れればいいかビット数の判定586-589の時は0を1追加56-589の時は2追加
                                for i in range(1, len(str(n))-len(str(a-n))+1):
                                    if int(str(a-n) + mstr[l-1:l+i-1]) >= n:    #もし割られる数が割る数よりも大きければ590-589になってしまった時はbreak
                                        f1 = 1
                                        break
                                    waru_dict_count.append("0")
                                    waru_dict_count_all.append("0")
                                
                    break
                a -= n  # 引き算
                
        # 大きくない時はビット数を増やす
        else:
            l += 1
            if len(mstr) != l:
                f1 = 1
            continue
        
        # もし、もう割るものがないなら
        if int(mstr) < n:
            print("\n以下が割り算の過程である。")
            print(waru_dict)
            print("\n以下は割り算の割った数のリストである")
            print(waru_dict_count)
            all_count = ''.join(waru_dict_count_all)
            print(f"\nよって、割られる数:{m} 割る数{n} \n商:{all_count} 余り:{int(mstr)}である")
            break
    # print(seikaim == int(all_count), seikaim, all_count, type(seikaim), type(all_count))
    # print(seikainm == int(mstr))
    # if seikaim == int(all_count):
    #     print("この割り算(筆算)は適切に処理されています")
    # else:
    #     print("この割り算(筆算)は間違っています")
        
    # if seikainm == int(mstr):
    #     print("この余り算(筆算)は適切に処理されています")
    # else:
    #     print("この余り算(筆算)は間違っています")
        
    return int(mstr)


# 復号化
def hukugouka(d, n, c):
    r_l = []
    s_c = c
    for i in range(1,d):  # 本当はこんなことしたくない(c**dでおわる)
        c *= s_c
        r_l.append(c)
    print(f"{s_c}の{d}乗の過程をリスト抽出")
    print(r_l)
    # print(s_c**e == m)
    
    # if s_c**d == c:
    #     print("この掛け算(筆算)は適切に処理されています")
    # else:
    #     print("この掛け算(筆算)は間違っています")
        
    seikaim = c//n  # 正解値の計算
    seikainm = c%n  # 正解値の計算
    cstr = str(c)   # mのstring
    l = len(str(n)) # ビット数
    waru_dict = []  # 引き算を用いた割り算の筆算の実行結果
    waru_dict_count = []
    waru_dict_count_all = []
    count = 0        # 何回引いたか
    f1 = 0
    while True:
        # 引かれる数先頭の引く数ビット文が引く数よりも大きいとき
        if int(cstr[0:l]) > n:
            a = int(cstr[0:l])
            
            # 割り算の筆算を行うための引き算実行部
            while True:
                count += 1   # if文の中で一回引き算をするので引き算の回数+1
                # n(引く数)よりも割り算の引き算部分が大きいかどうか
                if a-n < n:
                    cstr = str(a-n) + cstr[l:len(cstr)]
                    waru_dict.append(int(cstr))
                    waru_dict_count.append(count)
                    waru_dict_count_all.append(str(count))
                    count = 0
                    l = len(str(n))
                    
                    # 商が0であるときの処理
                    if len(cstr) == len(str(n)):
                        if int(cstr) < n:
                            if f1 == 1:
                                waru_dict_count.append("0")
                                waru_dict_count_all.append("0")
                    f1 = 0
                    
                    # 商が0であるときの処理
                    if len(cstr) > len(str(n)):
                        if int(str(a-n) + cstr[l-1:l+1-1]) < n: # 筆算において次の数を割られる数に足しても割る数の大きさに満たない場合
                            if len(str(a-n)) < len(str(n)): # どれだけ0を入れればいいかビット数の判定586-589の時は0を1追加56-589の時は2追加
                                for i in range(1, len(str(n))-len(str(a-n))+1):
                                    if int(str(a-n) + cstr[l-1:l+i-1]) >= n:    #もし割られる数が割る数よりも大きければ590-589になってしまった時はbreak
                                        f1 = 1
                                        break
                                    # print(int(str(a-n) + cstr[l:l+1]), n, len(str(n)), len(str(a-n)),i, cstr, l, str(a-n)+cstr[l:l+1], str(a-n))
                                    waru_dict_count.append("0")
                                    waru_dict_count_all.append("0")
                     
                    break
                a -= n  # 引き算
                
        # 大きくない時はビット数を増やす
        else:
            l += 1
            if len(cstr) != l:
                f1 = 1
            continue
        
        # もし、もう割るものがないなら
        if int(cstr) < n:
            print("\n以下が割り算の過程である。")
            print(waru_dict)
            print("\n以下は割り算の割った数のリストである")
            print(waru_dict_count)
            all_count = ''.join(waru_dict_count_all)
            print(f"\nよって、割られる数:{c} 割る数{n} \n商:{all_count} 余り:{int(cstr)} である")
            break

    # print(seikaim == int(all_count), seikaim, all_count, type(seikaim), type(all_count))
    # print(seikainm == int(cstr))
    # if seikaim == int(all_count):
    #     print("この割り算(筆算)は適切に処理されています")
    # else:
    #     print("この割り算(筆算)は間違っています")
        
    # if seikainm == int(cstr):
    #     print("この余り算(筆算)は適切に処理されています")
    # else:
    #     print("この余り算(筆算)は間違っています")
        
    return int(cstr)


if __name__ == '__main__':
    # 学籍番号
    # input("学籍番号を入力せよ: ")
    gakuseki = 23048
    p = 19
    q = 31
    
    # 平文mを作る
    m, mm = create_m(gakuseki, p, q)
    
    # 最小公倍数を求める
    sc1 = sc(p, q)
    n = p*q
    
    # 最大公約数が1となるe
    e = gc(sc1)
    
    # 値dを求める
    d = mk_d(e, sc1)
    
    print("平文m:" + str(m) + " 商:" + str(mm) + " 最小公倍数:" + str(sc1) + \
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