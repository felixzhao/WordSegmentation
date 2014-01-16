# -*- coding: utf-8 -*- 

log = open('log/log_segmentation.txt','w')

def get_word_segmentation_score(word, match_word):
  cur_score = len(word)
  if (match_word not in word):
    cur_score = 0
  return cur_score

'''
    get longest string which contain match word,
    return the length of string as score for this sentence.
'''
def segmentation(dict, maxLen, sentence_source, match_word):
  ## log
  #print 'start segmentation for word : ' + str(match_word)
  ## end log
  score = 0
  sentence = sentence_source.split(' ')
  while(len(sentence)>0):
    word=sentence[0:maxLen]
    process_word = ''.join(word)
    meet=False;
    while((not meet) and (len(word)>0)):
      ## log
      print '                         ++> word : ' + process_word
      print >> log, '                         ++> word : ' + process_word
      ## end log
      if(process_word in dict):
        ## log
        if process_word in dict : 
          print '  ++> match dict : ' + process_word
          print '  ++> for word : ' + match_word
          print >> log, '  ++> match dict : ' + process_word
          print >> log, '  ++> for word : ' + match_word
        ## end log
        cur_score = get_word_segmentation_score(word, match_word)
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
  
  #for sen in sentences:
  for i in xrange(len(sentences)):
    ## log
    print ' -> start process ' + str(i) +' sentence, total is ' + str(len(sentences))
    print >> log, ' -> start process ' + str(i) +' sentence, total is ' + str(len(sentences))
    ## end log
    cur_score = segmentation(dict, seg_max_width, sentences[i], k)
    ## log
    print ' -> score of sen is ' + str( cur_score)
    print >> log, ' -> score of sen is ' + str( cur_score)
    ## end log
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