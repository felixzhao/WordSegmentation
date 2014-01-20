
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
    print 'in update dict'
    return

def get_intersection(w_d, w_s):
    return list(set(w_d), set(w_s))

def update_sentence(s, inter_list, i):
    result = []
    for w in inter_list:
        result.append( s[:i-1] + w + s[i:i+len(s)])
    return result

def  process_in_s(sentence, W_dict, C_dict):
    result = 0

    if len(sentence) == 0:
        return result

    for i in xrange(len(sentence)):
        words_in_dict = get_char_list(W_dict, i)
        if len(words_in_dict) == 0:
            break

        cur_word = sentence[i]
        if check_unk(cur_word) == False :
            ## remove all word if i position not equal sentence_i(cur_word)
            W_dict = update_dict(W_dict, i, cur_word)
            result += 1
        else:
            words_in_sen = []
            words_in_sen.append(C_dict[sentence[i]])
            inter_list = get_intersection(words_in_dict, words_in_sen)
            if len(inter_list) == 0:
                break
            else: ## | inter words | > 0
                for inter in inter_list:
                    cur_sentence = update_sentence(sentence, inter, i)
                    result += process_in_s(sentence[i:],dict, C_dict)
                break
    return result

if __name__ == '__main__':
    s = 'a u1 k'.split()
    W_d = ['abk']
    C_d = {'u1':['b']}
    Expected = 3
    Actual = process_in_s(s, W_d, C_d)
    print Actual
    print Actual == Expected
    

                        
                        
                                    
