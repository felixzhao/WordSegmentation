# -*- coding: utf-8 -*- 

from segmentation import get_score
from ref.update import update_unk
from ref.get_sentence import get_sentence
from ref.get_top_n_score import get_top_n_score
from check_word_in_dict import checkdict

log = open('log/log_get_top_word_segmentation_score.py','w')

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
    ## log
    print >> log, 'start process', r
    print >> log, 'cands for ', r
    for c in r_cands:
      print >> log, c,
    print >> log, ' '
    ## end log
    
    for k in r_cands:
    
      cur_dict = checkdict(k, dict, sentence_split_len)
      ## ignore cand not existed in dict
      if len(cur_dict) == 0:
        ## log
        print 'the cand : ' + k + ' ; of unk : ' + r + ' , not existed in dict'
        print >> log, 'the cand : ' + k + ' ; of unk : ' + r + ' , not existed in dict'
        ## end log
        continue
      
      ## log
      print >> log, '-=-> the cand : ' + k + ' ; of unk : ' + r
      for w in cur_dict:
        print >> log, '-=-=->', w
      print >> log, ' '
      '''
      print >> log, ' doc list type: ', type(docs)
      print >> log, ' type of test text: ', type(test_text)
      print >> log, ' r : ', r
      print >> log, ' k : ', k
      print >> log, ' first doc type : ', type([x.replace(r + ' ', k + ' ') for x in test_text])
      '''
      ## end log
      
      docs.append( [x.replace(r + ' ', k + ' ') for x in test_text]) #update_unk(test_text, r, k))
      
      ## log
      print >> log, '=> start process :', r
      print >> log, '=> word :', k
      
      print '=> start process :' + str(r)
      print '=> word :' + str(k)
      ## end log
      
      for u in unks:
        if u == r: continue ## ignore k
        ## log
        print '==> start process unk :' + str(u)
        print >> log, '==> start process unk :' + str(u)
        ## end log
        u_cands = cands[u]
        for c in u_cands:
          ## log
          print '===> start process cand : ' + str(c) + ' for unk : ' + str(u)
          print >> log, '===> start process cand : ' + str(c) + ' for unk : ' + str(u)
          ## end log
          cur_score_list = [] ## [( score, #d)]
          
          for d in xrange(len(docs)):
            d_u = [x.replace(u + ' ', c + ' ') for x in docs[d]] #update_unk(docs[d], u, cands[u])
            sentences = []
            sentences = get_sentence(d_u, k, sentence_split_len)
            ## log
            print '====> sentences is ' + str(len(sentences)) + ' for word : ' + str(k)
            print >> log, '====> sentences is ' + str(len(sentences)) + ' for word : ' + str(k)
            print >> log, '=====> s : ', sentences[0]
            ## end log
            cur_score_list.append( (get_score(sentences, cur_dict, seg_max_width, k),d)) ## [( score, #d)]
          
          top_n_docs, cur_score = get_top_n_score(cur_score_list, beam_width) ## [( score, #d)], #
          ## log
          print '===> cur score : ' + str(cur_score)
          print '===> for doc : ' + str(d)
          print >> log, '===> cur score : ' + str(cur_score)
          print >> log, '===> for doc : ' + str(d)
          ## end log
          if cur_score > cur_max_score: cur_max_score = cur_score
          docs = []
          docs = top_n_docs
        score[r] = cur_max_score
        ## log
        print >> log, '==> replace : ', u
        print >> log, '==> word : ', c
        print >> log, '==> score : ', cur_max_score
        
        print '==> replace : ' + str(u)
        print '==> word : ' + str(c)
        print '==> score : ' + str(cur_max_score)
        ## end log
  return score  