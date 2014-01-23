
from left_process import *

if __name__ == '__main__':
    s = 'u1 b u2'.split()
    W_d = ['abc','hb']
    C_d = {'u1':['a','h'], 'u2':['c','d']}
    Expected = 3
    Actual = process_in_s(s, 0, W_d, C_d)
    print >> log, Actual
    print >> log, Actual == Expected
    
    print Actual
    print Actual == Expected