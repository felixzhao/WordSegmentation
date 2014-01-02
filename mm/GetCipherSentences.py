
def GetSentences(filePath, unk, match_word, maxLen):
  sentences = []
  lines = open(filePath,'r').readlines()
  for line in lines:
    words = line.split(' ')
    unk_index_list = [item for item in range(len(words)) if words[item] == unk]
    if len(unk_index_list) > 0:
      for index in unk_index_list:
        terms = words[index - maxLen : index + maxLen + 1]
        ## update unk
        words = [w.replace(unk, match_word) for w in terms]
        ## generate sentence
        sentences.append(''.join(terms))
  return sentences

if __name__ == '__main__':
  cipher_text_path = 'corpus\src-67percent\test-unknown.txt'
  