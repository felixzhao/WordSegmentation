# -*- coding: utf-8 -*- 

from GetTopWordSegmentationScore import get_top_score

def load_unks_orgword(word_map_path):
  result = [] ## tuple list : (unk, word)
  lines = open(word_map_path, 'r').readlines()
  for line in lines:
    term = line.split(' ')
    if len(term) > 1:
      result.append((term[1][:-1],term[0]))
  return result

def load_unks(word_map_path):
  result = []
  tuples = load_unks_orgword(word_map_path)
  result = [x[0] for x in tuples]
  return result

def GetDataDict(path):
    infile = open(path, 'r')
    dict = {}
    '''
        Create infile data dict
    '''
    for line in infile.readlines():
        if line.startswith(' '):
            continue
        else:
            w = line.split(':')
            if len(w) > 1:
                t = w[1].split('|')
                v = [x.lstrip(' ').split(' ')[0].strip(' ') for x in t][:-1]
                dict[w[0].strip(' ')] = v
    return dict

def GetWordDict(path):
  result = []
  
  word_list = open(path,'r').readlines()
  result = [x[:-1] for x in word_list]
  
  return result

  '''
def GetTestText(path):
  result = []
  lines = open(test_text_path, 'r').readlines()
  for line in lines:
    result.append(line)
  return result
  '''
  
if __name__ == '__main__':
  test_text_path = '../corpus/src-33percent/test-unknown.txt'
  unk_path = '../corpus/src-33percent/word-map.txt'
  bms_sf_result_path = '../result_bms_sf/updated_out.bw10.ns0.sfw0.type33.txt'
  word_dict_path = '../Dict/_Dict-SC2TC.Sort.V1_Simple_Chinese_UTF8.txt'
  out_path = 'out/top_score_bms_sf_10_0_0_33_ws_.txt'
  
  out_file = open(out_path, 'w')
  
  top_score = {}
  unks = []
  cands = {}
  dict = []
  sentence_split_len = 6
  seg_max_width = 4 
  beam_width = 5
  
  unks = load_unks(unk_path)
  cands = GetDataDict(bms_sf_result_path)
  dict = GetWordDict(word_dict_path)
  test_text = open(test_text_path, 'r').readlines()
  
  top_score = get_top_score( test_text, unks, cands, dict, sentence_split_len, seg_max_width, beam_width)
  
  for k in top_score.keys():
    print k, top_score[k]
    print >> out_file, k, top_score[k]