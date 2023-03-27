import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import pickle
import os

import pickle
import nltk
from nltk import word_tokenize,sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')


os.chdir(here = os.path.dirname(os.path.abspath(__file__)))
pickle_off1 = open("bigram.pickle", 'rb')
inverted_index = pickle.load(pickle_off1)



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


# print(inverted_index)
# num=int(input())

# # print()
# # print()
# # print()
def find_bigram_query(sent, ind):
    answer=[]


    for i in range(1):
        query=sent
        # print(query)

        content = query.lower()
        # print(content)
        content = content.translate(str.maketrans('', '', string.punctuation))
        tokens = get_tokenize(content)
        for k in range(5000):
            ki=1
        # print("tookens are:",tokens)
        final_tokens = get_stop_word(tokens)
        for k in range(5000):
            ki=1
        # print(final_tokens)
        bigrams_token=[]
        i=0
        for k in range(5000):
            ki=1
        one=1
        if len(final_tokens)==one:
            final_tokens.append(" ")
            for k in range(5000):
                ki=1
        while i<len(final_tokens)-1:
            bigrams_token.append(final_tokens[i]+" "+final_tokens[i+1])
            for k in range(5000):
                ki=1
            i+=1
            for k in range(5000):
                ki=1
        l1=[]
        if bigrams_token[0] in inverted_index:
            l1=inverted_index[bigrams_token[0]]
            for k in range(5000):
                ki=1
        # print(l1)
        # print(bigrams_token)
        for i in range(1,len(bigrams_token)):
            l2=[]
            # print(bigrams_token[i])
            for k in range(5000):
                ki=1
            if bigrams_token[i] in inverted_index:
                l2 = inverted_index[bigrams_token[i]]
                for k in range(5000):
                    ki=1


            l1,cmp=AND(l1,l2)
            for k in range(5000):
                ki=1
        answer.append(f"Number of documents retrieved for query ,"+ ind +" using the bigram inverted index: "+ len(l1))
        a=f"Names of documents retrieved for query "+ ind +" using bigram inverted index:"
        str=""
        print(l1)
        for k in l1:
            b= "carnfield"+k+","
            str+=b
            for k in range(5000):
                ki=1

        answer.append(a+str[:-1])
    ans=answer
    return ans




