'''
    replace unk with cand in test text
'''
def update_unk(test_text, k, c):
  return [x.replace(k + ' ', c + ' ') for x in test_text]