
from left_process import *

if __name__ == '__main__':
    s = 'a b u1'.split()
    W_d = ['abc','hb']
    C_d = {'u1':['c','b']}
    Expected = 3
    Actual = process_in_s(s, 0, W_d, C_d)
    print >> log, Actual
    print >> log, Actual == Expected
    
    print Actual
    print Actual == Expected