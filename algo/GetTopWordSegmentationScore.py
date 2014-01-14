
update_unk(test_text, k, c):
  return test_text.replace(k + ' ', c + ' ')

'''
    test_text = string
    unks = unknown word flag in test_text
    cands = { unk: cand[] }
'''
def get_top_score( test_text, unks, cands):
  docs = []
  score = 0
  sentence_split_len = 6
  seg_max_width = 4
  beam_width = 5
  for r in unks:
    k = cands[r]
    docs.append(update_unk(test_text, r, k))
    for u in unks:
      if u == r: continue ## ignore k
      
      cur_score_list = [] ## [( score, u, d)]
      
      for d in docs:
        d_u = update_unk(d, u, cands[u])
        sentences = get_sentence(d_u, k, sentence_split_len)
        cur_score_list.append( get_score(sentences, dict, seg_max_width, k))
      
      top_n_docs, cur_max_score = get_top_n_score(cur_score_list, beam_width)
      if cur_max_score > score: score = cur_max_score
      docs = []
      docs = top_n_docs
  return score