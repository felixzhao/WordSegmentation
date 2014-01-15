
log = open('log/word_seg_main_algo.txt','w')

'''
    get sub sentence list in doc,
    which n word before k and n word after k.
    the n is the len.
'''
def get_sentence(d_u, k, len):
  result = [] ## a list of string, each word split by space

  ## log
  print >> log, ' doc of u type: ', type(d_u)
  print >> log, ' the first line of doc u: ', d_u[0]
  print >> log, ' k : ', k
  print >> log, ' len : ', len
  
  for line in d_u:
  ## try
    li = line.split()
    index = li.index(k)
    s = index - maxLen
    e = index + maxLen + 1
    if index - maxLen < 1:
      s = 0
    terms = line[s: e]
    
  ## end try
  
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