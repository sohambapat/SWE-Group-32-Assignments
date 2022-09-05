import sys
sys.path.append('src')
from Sym import Sym
from Num import Num

def test_sym():
    sym = Sym(0,"")
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    mode, entropy = sym.mid(0,""), sym.div()
    #entropy is complex, so take real number part only
    entropy = (1000*entropy.real)//1/1000
    # print output: oo({mid=mode, div=entropy})
    print('mid: {}, div: {}'.format(mode, entropy))
    
    # assert mode=="b" and 1.37 <= entropy and entropy <= 1.38
    if not (mode=="a" and 1.37 <= entropy and entropy <= 1.38):
        raise AssertionError()
    else:
        print("Sym test passed")

def test_num():
    num = Num(0,"")
    for i in range(1,100):
        num.add(i)
    mid = num.median
    div = num.stdDev
    print('mid: {}, div: {}'.format(mid, div))
    if not (mid >= 50 and mid <= 52 and div > 30.5 and div <32):
        raise AssertionError()
    else:
        print("Num test passed")
    
def test_bignum():
    print('\n-----------------------------------')
    num=Num(0, '')
    for x in range(1, 1000):
        num.add(x, 32)
    # print output: oo(num.nums())
    num._has.sort()
    print(num._has)
    print('Passed? =', len(num._has) == 32)

if __name__ == "__main__":
    test_sym()
    test_bignum()
    