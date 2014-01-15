
from segmentation import get_score
from ref.update import update_unk
from ref.get_sentence import get_sentence
from ref.get_top_n_score import get_top_n_score
  
log = open('log/word_seg_main_algo.txt','w')
  
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
    r_cands = cands[r]
    for k in r_cands:
      
      ## log
      print >> log, ' doc list type: ', type(docs)
      print >> log, ' type of test text: ', type(test_text)
      print >> log, ' r : ', r
      print >> log, ' k : ', k
      print >> log, ' first doc type : ', type([x.replace(r + ' ', k + ' ') for x in test_text])
      
      
      docs.append( [x.replace(r + ' ', k + ' ') for x in test_text]) #update_unk(test_text, r, k))
      
      for u in unks:
        if u == r: continue ## ignore k
        
        u_cands = cands[u]
        for c in u_cands:
        
          cur_score_list = [] ## [( score, #d)]
          
          for d in xrange(len(docs)):
            d_u = [x.replace(u + ' ', c + ' ') for x in docs[d]] #update_unk(docs[d], u, cands[u])
            sentences = []
            sentences = get_sentence(d_u, k, sentence_split_len)
            cur_score_list.append( (get_score(sentences, dict, seg_max_width, k),d)) ## [( score, #d)]
          
          top_n_docs, cur_score = get_top_n_score(cur_score_list, beam_width) ## [( score, #d)], #
          if cur_score > cur_max_score: cur_max_score = cur_score
          docs = []
          docs = top_n_docs
        score[r] = cur_max_score
  return score  