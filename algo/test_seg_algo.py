
from GetTopWordSegmentationScore import get_top_score

def load_unks_orgword(word_map_path):
  result = [] ## tuple list : (unk, word)
  lines = open(word_map_path, 'r').readlines()
  for line in lines:
    if len(line) > 1:
      term = line.split(' ')
      result.append((term[1],term[0]))
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

if __name__ == '__main__':
  test_text_path = '../corpus/src-33percent/test-unknown.txt'
  unk_path = '../corpus/src-33percent/word-map.txt'
  bms_sf_result_path = '../result_bms_sf/updated_out.bw10.ns0.sfw0.type33.txt'
  out_path = 'out/top_score_bms_sf_10_0_0_33_ws_.txt'
  
  test_text = open(test_text_path, 'r').readlines()
  out_file = open(out_path, 'w')
  
  top_score = {}
  unks = {}
  cands = {}
  dict = {} ## to do, get from prof source file.
  sentence_split_len = 6
  seg_max_width = 4 
  beam_width = 5
  
  unks = load_unks(unk_path)
  cands = GetDataDict(bms_sf_result_path)
  top_score = get_top_score( test_text, unks, cands, dict, sentence_split_len, seg_max_width, beam_width)
  
  for k in top_score.keys():
    print k, top_score[k]
    print >> out_file, k, top_score[k]