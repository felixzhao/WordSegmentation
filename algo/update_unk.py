
def update_unk(terms, unk, candidate):
  updated_terms = terms.replace(unk, candidate)
  updated_sentence = updated_terms.replace(' ','')
  return updated_terms, updated_sentence
  
def update_unk_for_terms_list(terms_list, unk, candidate):
  updated_terms = []
  updated_sentences = []
  for terms in terms_list:
    cur_term, cur_sen = update_unk(terms, unk, candidate)
    updated_terms.append(cur_term)
    updated_sentences.append(updated_sentence)
  
if __name__ == '__main__':
  terms = '<unk>369 观 <unk>9 《 刘 少 奇 <unk>498 辉 业 <unk>786 展 览'
  unk = '<unk>9'
  candidate = '了'
  outfile = open('test/update_unk.txt','w')
  
  updated_terms, updated_sentence = update_unk(terms, unk, candidate)
  print >> outfile, updated_terms
  print >> outfile, updated_sentence