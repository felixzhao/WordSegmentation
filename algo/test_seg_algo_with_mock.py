# -*- coding: utf-8 -*- 

from GetTopWordSegmentationScore import get_top_score
 
if __name__ == '__main__':
  out_path = 'out/test_mock.txt'
  out_file = open(out_path, 'w')
  
  top_score = {}
  unks = []
  cands = {}
  dict = []
  sentence_split_len = 3
  seg_max_width = 3
  beam_width = 2
  
  unks = ['<unk>1','<unk>123','<unk>1,234']#load_unks(unk_path)
  cands = {'<unk>1':['大','天'],'<unk>123':['是','好'],'<unk>1,234':['一','二']}#GetDataDict(bms_sf_result_path)
  dict = ['好大','大的好']#GetWordDict(word_dict_path)
  test_text = ['执 <unk>1,234 法 监 督 卡 林 加 <unk>123 <unk>1 省 法 兰 克 <unk>1,234 大 数 据 反 垃 圾 税 的 库 夫 拉 但 <unk>1,234 是 看 风 <unk>1 景 啊 <unk>123 是', \
  '借 了 几 万 放 假 <unk>1 馈 <unk>123 <unk>1,234 咯 晶 粒 间 界 哦 我', \
  '理 论 <unk>123 急 哦 违 <unk>1,234 法 乱 纪 <unk>123 我 非 礼 弗 <unk>1,234 动 反 对 封 建']#open(test_text_path, 'r').readlines()
  
  top_score = get_top_score( test_text, unks, cands, dict, sentence_split_len, seg_max_width, beam_width)
  
  for k in top_score.keys():
    print k, top_score[k]
    print >> out_file, k, top_score[k]