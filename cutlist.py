def cutlist(listx,devidenum):
  length = len(listx)
  finallist = []
  sum = 0
  for i in range(int(length/devidenum)+1):
    if i <length/devidenum:
      finallist.append([x for x in listx[:devidenum]])
      listx = listx[devidenum:]
    elif i == int(length/devidenum) and length%devidenum != 0:
      finallist.append(listx[:])
  return finallist
