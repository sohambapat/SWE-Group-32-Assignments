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



if __name__ == "__main__":
    test_sym()
    