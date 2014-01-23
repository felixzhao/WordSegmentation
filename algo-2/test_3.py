
from left_process import *

if __name__ == '__main__':
    s = 'u1 b c'.split()
    W_d = ['hbc','hb']
    C_d = {'u1':['h','u']}
    Expected = 3
    Actual = process_in_s(s, 0, W_d, C_d)
    print >> log, Actual
    print >> log, Actual == Expected
    
    print Actual
    print Actual == Expected