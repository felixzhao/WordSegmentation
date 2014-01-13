
def GetSentences(lines, unk, match_word, maxLen):
  terms_list = []
  sentences = []
  for line in lines:
## update unk
    words = line.replace(unk, match_word).split(' ')
## get unk index
    unk_index_list = [item for item in range(len(words)) if words[item] == match_word]
# debug
    if unk_index_list != []: print unk_index_list
# end debug
    if len(unk_index_list) > 0:
      for index in unk_index_list:
        terms = words[index - maxLen : index + maxLen + 1]        
        if terms != '' and len(terms) > 0:
          if terms[-1] == '\n':
            terms = terms[:-1]
## Add to terms
          terms_list.append(' '.join(terms))
## Add to sentences
          sentences.append(''.join(terms))
          
## log
#        print sub_sentence
## end log
  return terms_list, sentences

if __name__ == '__main__':
  cipher_text_path = '../corpus/src-33percent/test-unknown.txt'
  unk = '<unk>588'
  match_word = '奇'
  maxLen = 6
  
  lines = open(cipher_text_path,'r').readlines()
  
  terms_list, sentences = GetSentences(lines, unk, match_word, maxLen)
  
  out_terms_list = open('out/terms_list.txt','w')
  out_sentences = open('out/sentences.txt','w')
  
  for s in sentences:
    print >> out_sentences, s
  for t in terms_list:
    print >> out_terms_list, t
  