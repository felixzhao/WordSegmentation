
def  process_in_s(seg_lim,sentence, W_dict, C_dict):
    result = 0

    hs = heap
    hs.push(sentence)
    dict = W_dict.clone()
    while(S_set.Empty() == False):
        S_set = hs.pop()
        for i in xrange(seg_lim - 1, -1, -1):
            words_in_dict = get_word(dict, i)

            cur_word = sentence[i]
            if check_unk(cur_word) == False :
                dict = update_dict(dict, i, cur_word) # remove all word if i position not equal sentence_i(cur_word)
            else:
                words_in_sen = []
                words_in_sen.append(C_dict[sentence[i]])
                inter = get_intersection(words_in_dict, words_in_sen)
                if len(inter) == 0:
                    return result
                elif len(inter) == 1:
                    sentence = update_sentence(sentence, inter[0])
                    hs.push(sentence)
                    break
                else:
                    for j in xrange(len(inter)):
                        sentence = update_sentence(sentence, inter[j])
                        hs.push(sentence)
                        
                        
                                    
