from Queue import * 

log = open('log\left_process_5.txt','w')

def process_in_s(sentence, pos, W_dict, C_dict):
    result = 0
    
    if pos == len(sentence):
      return 0
    
    unk_flag = 'u'
    
    #q = Queue()
    #q.put(sentence)
    
    #while q.empty() == False :
        #cur_s = q.get()
    cur_s = sentence
    print >> log, '='*50
    print >> log, '1> process sentence : ', cur_s
    for i in xrange(pos,len(cur_s)):
        print >> log, '2> Round ', i
        print >> log, '2> dict : ', W_dict
        print >> log, '2> process : ', cur_s[i]
        
## get chars which in all words in dict i position
        w_d = []
        for w in W_dict:
            w_d.append(w[i])
        print >> log, '2> chars at i positon in word dict : ', w_d
        
## if no word at i position in dict match current process char then next sentence
        if len(w_d) == 0:
            break

        cur_word = cur_s[i]

## chenck the word is unk
        if cur_word.startswith(unk_flag) == False :
            print >> log, '3> in known word brunch.'
        ## remove all word if i position not equal sentence_i(cur_word)
            print >> log, '3> before update dict :', W_dict
            print >> log, '3> process word : ', cur_word
            print >> log, '3> process position : ', i
            W_dict = [x for x in W_dict if len(x)> i and x[i] == cur_word]
            print >> log, '3> after update dict : ', W_dict
            if len(W_dict) > 0:
                result += 1
                print >> log, '==> add one, match with a known word. '
            print >> log, '3> end known word brunch.\n'
        else:
            print >> log, '3> in unk brunch.'
            w_s = C_dict[cur_s[i]]
            print >> log, '3> process word : ', cur_s[i]
            print >> log, '3> cands : ', w_s
            inter_list = list(set(w_d) & set(w_s))#get_intersection(words_in_dict, w_s)
            print >> log, '3> inters list : ', inter_list
            if len(inter_list) == 0:
                print >> log, '==> no match, end algo. '
                break
            else: ## | inter words | > 0
                print >> log, '3*> in mulit cands brunch.'
                max_sub_score = 0
                for w in inter_list:
                    print >> log, '4> process inter word : ', w
                    print >> log, '4> process sentence : ', cur_s
                    print >> log, '4> replace position : ', i
                    cur_s[i] = w
                    print >> log, '4> updated sentence : ', cur_s, '\n'
                    sub_score = 0
                    sub_score += process_in_s(cur_s, i+1, W_dict, C_dict)
                    if sub_score > max_sub_score: max_sub_score = sub_score
                result += max_sub_score + 1 ## because this unk get match, so add one
                break
    print >> log, '1> end of sentence process : ', cur_s, '\n'
    print >> log, '='*50
    return result

if __name__ == '__main__':
    s = 'a u1 k'.split()
    W_d = ['abk','cde']
    C_d = {'u1':['b']}
    Expected = 3
    Actual = process_in_s(s, 0, W_d, C_d)
    print >> log, Actual
    print >> log, Actual == Expected
    
    print Actual
    print Actual == Expected