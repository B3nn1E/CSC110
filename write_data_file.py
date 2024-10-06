def write_csv(dict,file_name):
  f = open(file_name,"w")
  for k, v in dict.items(): 
    f.write (str(k))
    i = 0
    while i < len(v):
      f.write (",")
      f.write (str(v[i]))
      if i == len(v)-1:
        f.write ("\n")
      i+=1
  f.close ()
  

  

  