
logfile = open('log/segmentation.txt','w')

def get_score(word, match_word):
  cur_score = len(word)
  if (match_word not in word):
    cur_score = 0
  return cur_score

'''
    get longest string which contain match word,
    return the length of string as score for this sentence.
'''
def segmentation(dict, maxLen, sentence_source, match_word):
  score = 0
  sentence = sentence_source.split(' ')
  while(len(sentence)>0):
    word=sentence[0:maxLen]
    meet=False;
    while((not meet) and (len(word)>0)):
      print >> logfile, ''.join(word)
      if(''.join(word) in dict):
        print >> logfile, 'match dict :', ''.join(word), ''.join(word) in dict
        cur_score = get_score(word, match_word)
        if cur_score > score:
          score = cur_score
        #wordList.append(word)
        sentence=sentence[len(word):len(sentence)]
        meet=True;
      else:
        if(len(word)==1):
          #wordList.append(word)
          sentence=sentence[len(word):len(sentence)]
          meet=True;
        else:
          word=word[0:len(word)-1]
  return score

'''
    word segmetation algo.
    return max score.
'''
def get_score(sentences, dict, seg_max_width, k):
  result = 0 
  
  for sen in sentences:
    cur_score = segmentation(dict, seg_max_width, sen, k)
    if cur_score > result: 
      result = cur_score
  
  return result
  
if __name__ == '__main__':
  sentence = 'u 观 了 《 刘 少 奇 u 辉 业 u 展 览'
  match_word = '奇'
  dict = ['刘少奇', '展览','观了','刘少']
  maxLen = 3
  
  score = segmentation(dict, maxLen, sentence, match_word)
  
  print score