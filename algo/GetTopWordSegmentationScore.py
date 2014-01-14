
from segmentation import get_score

'''
    replace unk with cand in test text
'''
def update_unk(test_text, k, c):
  return test_text.replace(k + ' ', c + ' ')

'''
    get sub sentence list in doc,
    which n word before k and n word after k.
    the n is the len.
'''
def get_sentence(d_u, k, len):
  result = [] ## a list of string, each word split by space

  for line in d_u:
## get unk index
    unk_index_list = [item for item in range(len(line)) if line[item] == k]
    if len(unk_index_list) > 0:
      for index in unk_index_list:
        terms = line[index - maxLen : index + maxLen + 1]        
        if terms != '' and len(terms) > 0:
          if terms[-1] == '\n':
            terms = terms[:-1]
## Add to terms
          result.append(' '.join(terms))
  
  return result

'''
    sort word segmetation result,
    based on score.
    return top n doc, n is beam_width.
    return first score as max score.
'''
def get_top_n_score(cur_score_list, beam_width): ## [( score, #d)], #bw
  top_n_docs = [] ## string list, each element is a doc
  cur_max_score = 0 ## a interge number, max score 
  
  top_n = sorted(cur_score_list, key = lambda x:x[0],reverse=True)[:width]
  top_n_docs = list(set([x[1] for x in top_n]))
  cur_max_score = max(cur_score_list,key=lambda item:item[0])[0]
  
  return top_n_docs, cur_max_score
  
'''
    test_text = string
    unks = unknown word flag in test_text
    cands = { unk: cand[] }
'''
def get_top_score( test_text, unks, cands, dict, sentence_split_len = 6, seg_max_width = 4, beam_width = 5):
  docs = []
  score = {}
  for r in unks:
    cur_max_score = 0
    k = cands[r]
    docs.append(update_unk(test_text, r, k))
    for u in unks:
      if u == r: continue ## ignore k
      
      cur_score_list = [] ## [( score, #d)]
      
      for d in xrange(len(docs):
        d_u = update_unk(docs[d], u, cands[u])
        sentences = []
        sentences = get_sentence(d_u, k, sentence_split_len)
        cur_score_list.append( (get_score(sentences, dict, seg_max_width, k),d)) ## [( score, #d)]
      
      top_n_docs, cur_score = get_top_n_score(cur_score_list, beam_width) ## [( score, #d)], #
      if cur_score > cur_max_score: cur_max_score = cur_score
      docs = []
      docs = top_n_docs
    score[r] = cur_max_score
  return score  