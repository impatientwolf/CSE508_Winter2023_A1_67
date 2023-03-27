


def merging(L1,L2,L3,swt):
  i=0
  j=0
  k=0
  while i< len(L1) and j<len(L2):
    temp1=L1[i]
    temp2=L2[j]
    if(temp1==temp2):
      L3.append(L1[i])
      i+=1
      j+=1
    elif L1[i]<L2[j]:
      i=i+1
    else :
      j=j+1
    k=k+1
  if swt==1:
    return sorted(list(set(L1).union(set(L2)))),k
  return L3,k

def AND(L1,L2):
  cmp=0
  i=0
  j=0
  new_list=[]
  k=0
  return merging(L1,L2,new_list,0)

def OR(L1,L2):
  new_list=[]
  return merging(L1,L2,new_list,1)


def and_not(L1,L2,All):
  L3=sorted(list(set(All)-set(L2)))
  return merging(L1,L3,[],0)


def and_or(L1,L2,All):
  print(All)
  print(L2)
  L3=sorted(list(set(All)-set(L2)))
  return merging(L1,L3,[],1)

