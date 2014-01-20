
'''
get i char from each word in dict
'''
def get_char_list(dict, i):
    result = []
    for w in dict:
        result.append(w[i])
    return result

'''
check a word is an unkown word
'''
def check_unk(w):
    result = False
    if w.startswith('u'):
        result = True
    return result

'''
 remove all word if i position not equal sentence_i(cur_word)
'''
def update_dict(dict, i, w):
    result = []
    for dw in dict:
        if dw[i] == w:
            result.append(dw)
    return result

def get_intersection(w_d, w_s):
    result = []
#    print 'w_d : ',w_d, ' ; w_s : ', w_s
#    print 'set w_d : ', set(w_d), ' ; set w_s : ', set(w_s)
    result = list(set(w_d) & set(w_s)) 
#    print 'intersection : ', result
    return result

def update_sentence(s, inter_list, i):
    result = []
#    print 'inter : ', inter_list
#    print 'sentence : ', s
#    print 'i : ', i
    for w in inter_list:
        u_s = s
        u_s[i] = w
        result.append(u_s)
    return result

def  process_in_s(sentence, W_dict, C_dict):
    result = 0
    if len(sentence) == 0:
        return result
    for i in xrange(len(sentence)):
        words_in_dict = []
        print W_dict
        for w in W_dict:
            words_in_dict.append(w[i])
        if len(words_in_dict) == 0:
            break

        cur_word = sentence[i]
        if check_unk(cur_word) == False :
            ## remove all word if i position not equal sentence_i(cur_word)
            print 'before update dict', W_dict
            W_dict = update_dict(W_dict, i, cur_word)
            print 'after update dict : ', W_dict
            if len(W_dict) > 0:
                result += 1
                print ' add one, match with a known word. '
        else:
            words_in_sen = C_dict[sentence[i]]
            inter_list = get_intersection(words_in_dict, words_in_sen)
            if len(inter_list) == 0:
                print ' no match, end algo. '
                break
            else: ## | inter words | > 0
                for inter in inter_list:
                    cur_sentence = update_sentence(sentence, inter, i)
                    result += process_in_s(cur_sentence[i:],dict, C_dict)
                break
    return result

if __name__ == '__main__':
    s = 'a u1 k'.split()
    W_d = ['abk','cde']
    C_d = {'u1':['b']}
    Expected = 3
    Actual = process_in_s(s, W_d, C_d)
    print Actual
    print Actual == Expected
    

                        
                        
                                    
