
from left_process import *

if __name__ == '__main__':
    s = 'a b c'.split()
    W_d = ['hij','opq']
    C_d = {'u1':['b','e']}
    Expected = 0
    Actual = process_in_s(s, 0, W_d, C_d)
    print >> log, Actual
    print >> log, Actual == Expected
    
    print Actual
    print Actual == Expected