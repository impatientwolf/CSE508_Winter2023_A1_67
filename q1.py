import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import pickle
import os
from nltk import word_tokenize,sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')



os.chdir(os.path.dirname(os.path.abspath(__file__)))

pickle_off1 = open("dictionary.pickle", 'rb')
index = pickle.load(pickle_off1)
pickle_off1.close()

pickle_off2 = open("number_list.pickle", 'rb')
number_list = pickle.load(pickle_off2)
pickle_off2.close()


def lower_str(para):
    return para.lower()

def get_tokenize(para):
    return word_tokenize(para)

def get_stop_word(word_token):
    stop_words = set(stopwords.words('english'))
    without_stop_word=[]
    for w in word_token:
        if w not in stop_words:
            without_stop_word.append(w)
    return without_stop_word




def merging(L1,L2,L3,swt):
  i=0
  j=0
  k=0
  while i< len(L1) and j<len(L2):
    if(L1[i]==L2[j]):
      L3.append(L1[i])
      i+=1
      j+=1
    elif L1[i]<L2[j]:
      i+=1
    else :
      j+=1
    k+=1
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




d= int(input())

answer=[]
nu=1
while d>0:

    final_tokens = (lower_str(input())).translate(str.maketrans('', '', string.punctuation))
    final_tokens = get_stop_word(get_tokenize(final_tokens))

    order=input().split(",")
    query=f"Query : "+str(nu)+" "
    query+=final_tokens[0]
    templist=[]
    for i in range(len(order)):
      templist.append(i)

    for i in templist:
      query+=(" "+order[i]+" "+final_tokens[i+1])
    print(query)

    minus1=-1
    if(len(order)-len(final_tokens)==minus1):
        if(final_tokens[0] not in index):
            l1=[]
            
        else:
            l1=index[final_tokens[0]]
        cmp=0
        templist=[]
        for i in range(len(order)):
          templist.append(i)

        for i in templist:
            op=order[i]
            l2=index[final_tokens[i+1]]

            match op:
              case "AND":
                l1,a=AND(l1,l2)
                cmp+=a

              case "OR":
                l1,a=OR(l1,l2)
                cmp+=a

              case "AND NOT":
                l1,a=and_not(l1,l2,number_list)
                cmp+=a             
              case _:
                l1,a=and_or(l1,l2,number_list)
                cmp+=a

        print(f"Number of documents retrieved for query"+str(nu)+":"+str(len(l1)))
        str1=f"Names of the documents retrieved for query"+str(nu)+" "
        for i in l1:
            str1+=("carnfield"+i+",")
        print(str1[:-1])
        print(f"Number of comparisons done for query"+str(nu)+":"+str(cmp))


    d-=1
    nu+=1

