def swap (dict,set):
  for k in list(dict.keys()):
    if k in set:
        dict[dict[k]] = k
        #add a new pairs of swapped k,v
        del dict[k]
        #delete the old pairs
