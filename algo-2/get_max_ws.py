

def get_max_for_key_unks(cands_dict, test_text, seg_lim, word_dict):
    max_word_length = 0

    for k in cands_dict.keys():
        for c in cands_dict[k]:
            doc = update_key_to_can(k, c, test_text)
            W_dict = get_related_dict(word_dict, c)
            S = get_related_sentence(doc, c, seg_lim)
            cur_length = get_max_word_length_for_cand(seg_lim, S, W_dict)
            if cur_length > max_word_length:
                max_word_length = cur_length

    return max_word_length
    
def get_max_word_length_for_cand(seg_lim, S, W_dict):
    result = 0
    for sen in S:
        continue
    return result

'''
W_dict is a list, each elements in it is a list of the word in dict
sentence is sub sentence which contain the key word.
seg_lim is the width of the sentence.(which means, n words before k and n after it. n = seg_lim)
'''
def  process_in_s(seg_lim,sentence, W_dict):
    hs = heap
    hs.push(sentence)
    dict = W_dict.clone()
    while(len(S_set) > 0):
        s = hs.pop()

