'''
    sort word segmetation result,
    based on score.
    return top n doc, n is beam_width.
    return first score as max score.
'''
def get_top_n_score(cur_score_list, beam_width): ## [( score, #d)], #bw
  top_n_docs = [] ## string list, each element is a doc
  cur_max_score = 0 ## a interge number, max score 
  
  top_n = sorted(cur_score_list, key = lambda x:x[0],reverse=True)[:beam_width]
  top_n_docs = list(set([x[1] for x in top_n]))
  cur_max_score = max(cur_score_list,key=lambda item:item[0])[0]
  
  return top_n_docs, cur_max_score