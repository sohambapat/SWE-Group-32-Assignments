import sys
sys.path.append('src')
from Sym import Sym
from Num import Num
from Data import Data
import Utils

def test_sym():
    sym = Sym(0,"")
    for x in ["a","a","a","a","b","b","c"]:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    #entropy is complex, so take real number part only
    entropy = (1000*entropy.real)//1/1000
    # print output: oo({mid=mode, div=entropy})
    #print('mid: {}, div: {}'.format(mode, entropy))
    Utils.oo({"mid": mode, "div": entropy})
    
    # assert mode=="b" and 1.37 <= entropy and entropy <= 1.38
    if not (mode=="a" and 1.37 <= entropy and entropy <= 1.38):
        raise AssertionError()
    else:
        print("Sym test passed")

def test_num():
    num = Num(0,"")
    for i in range(1,100):
        num.add(i)
    mid = num.mid()
    div = num.div()
    print('mid: {}, div: {}'.format(mid, div))
    if not (mid >= 50 and mid <= 52 and div > 30.5 and div <32):
        raise AssertionError()
    else:
        print("Num test passed")
    
def test_bignum():
    num=Num(0, '')
    Utils.the['nums'] = 32
    for x in range(1, 1000):
        num.add(x)
    Utils.oo(num.nums())
    print('Passed? =', len(num._has) == 32)

def test_the():
    Utils.oo(Utils.the)
    return True

def test_data():
    d = Data(Utils.the['file'])
    for _,col in enumerate(d.cols.y):
        print(':at {} :hi {} :isSorted {} :lo {} :n {} :name {} :w {}'.format(col.at, col.hi, col.isSorted, col.lo, col.n, col.name, col.w))
    return True

def test_csv():
    def function(row):
        function.counter += 1
        if function.counter > 10:
            return
        else:
            Utils.oo(row)
    function.counter = 0
    Utils.csv(Utils.the['file'], function)
    return True

def test_stats():
    data = Data(Utils.the['file'])
    def div(col):
        return col.div()
    def mid(col):
        return col.mid()
    print("xmid", Utils.o( data.stats(2,data.cols.x, mid)))
    print("xdiv", Utils.o( data.stats(3,data.cols.x, div)))
    print("ymid", Utils.o( data.stats(2,data.cols.y, mid)))
    print("ydiv", Utils.o( data.stats(3,data.cols.y, div)))
    return True

if __name__ == "__main__":
    Utils.init()
    test_the()
    test_sym()
    test_num()
    test_bignum()
    test_csv()
    test_data()
    test_stats()