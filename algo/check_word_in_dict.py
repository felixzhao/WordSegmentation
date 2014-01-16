# -*- coding: utf-8 -*- 

log = open('log/log_test_check_word_in_dict.txt','w')

'''
    word string, which is the cand of unk
    word_dict list of string, which is word dict from prof
'''
def checkdict(word, word_dict, len_limit):
  #print >> log,'limit : ', len_limit
  cur_word_dict = []
  limit = len_limit * 3
  for w in word_dict:
    if (word in w) :
      #print >> log,'=> word : ' + w
      #print >> log, '**> len of w : ', len(w)
      #print >> log, '**> compare result : ',  len(w) <= limit
      if (len(w) <= limit) :
        #print >> log,'==> word with limit : ' + w
        cur_word_dict.append(w)
  return cur_word_dict

if __name__ == '__main__':
  word_dict_path = '../Dict/_Dict-SC2TC.Sort.V1_Simple_Chinese_UTF8.txt'
  fout_path = 'out/test_check_word_in_dict.txt'
  
  word_list = open(word_dict_path,'r').readlines()
  fout = open(fout_path, 'w')
  word_dict = [x[:-1] for x in word_list]
  word = '天'
  len_limit = 6
  
  cur_word_dict = checkdict(word, word_dict, len_limit)
  
  for w in cur_word_dict:
    print >> fout, w