# -*- coding: utf-8 -*- 

import numpy as np
import re

log = open('log/log_get_sentence.txt','w')

'''
    get sub sentence list in doc,
    which n word before k and n word after k.
    the n is the length.
'''
def get_sentence(d_u, k, length):
  result = [] ## a list of string, each word split by space

  length *= 3
  ## log
  print >> log, ' doc of u type: ', type(d_u)
  print >> log, ' the first line of doc u: ', d_u[0]
  print >> log, ' k : ', k
  print >> log, ' length : ', length
  ## end log
  
  for l in d_u:
    ## replace unk flag to 'U', which no process in this turn
    line = re.sub('<unk>[\d ,]* ', 'U ', l)
    ## log
    print >> log, ' *** sentence which updated unk. *** '
    print >> log, line
    ## end log
  ## try
    #word_list = np.array(line.split())
    #index_list = np.where(word_list == k)[0] # word_list.index(k)
    
    ## get k position list
    index_list = []
    word_list = line.split(' ')
    for i in xrange(len(word_list)):
      if word_list[i] == k:
        index_list.append(i)
    
    ## log
    print >> log, ' index list : '
    for index in index_list:
      print >> log, str(index), ','
    ## end log
      
    for index in index_list:
      s = index - length
      e = index + length + 1
      if index - length < 1:
        s = 0
      terms = line[s: e]
      ## log
      print >> log, 'sub line : ', line[s: e]
      ## end log
      result.append(' '.join(terms))
      ## log
      print >> log, 'result : ',' '.join(terms)
      ## end log
    
  ## end try
  return result

'''  
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