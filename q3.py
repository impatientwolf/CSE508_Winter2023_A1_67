import os
import pickle
import string
import nltk
from runner2 import find_bigram_query



import fileinput

import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk import word_tokenize,sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')


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


def function_and(T1, T2):
    i = 0
    j = 0
    _list = []
    while i < len(T1) and j < len(T2):
        if int(T1[i]) == int(T2[j]):
            _list.append(T1[i])
            i += 1
            j += 1
        if T1[i] < T2[j]:
            i += 1
        elif T1[i] > T2[j]:
            j += 1
    return _list


def contains_value(value, _list):
    Flag = False
    for val in _list:
        if value == val:
            Flag = True
    return Flag


def checker(doc_value, word_list, pos_dict):
    main_flag = False
    for value in pos_dict[word_list[0]][doc_value]:
        flag = True
        for i in range(0, len(word_list)):
            u = value + i
            if not contains_value(u, pos_dict[word_list[i]][doc_value]):
                flag = False
        main_flag = main_flag or flag
    return main_flag


def query_int(word_list, pos_dict):
    T_list = []
    # for i in word_list:
    #     if i not in pos_dict:
    #         return []
    for i in range(0, len(word_list)):
        T_list.append([])
    for i in range(0, len(word_list)):
        for keys in pos_dict[word_list[i]].keys():
            T_list[i].append(keys)

    T_common = []
    for i in range(0, len(T_list)):
        if i == 0:
            continue
        elif i == 1:
            T_common = function_and(T_list[0], T_list[1])
        else:
            T_common = function_and(T_list[i], T_common)
    ans_list = []
    for value in T_common:
        if checker(value, word_list, pos_dict) == True:
            ans_list.append(value)
    return ans_list


os.chdir(os.path.dirname(os.path.abspath(__file__)))

pickle_off = open("postional_dict.pickle", 'rb')
pos_dict_1 = pickle.load(pickle_off)
pickle_off.close()

answer = []

q = int(input())


def content_retirvel(query):
    content = query.lower()
    content = content.translate(str.maketrans('', '', string.punctuation))
    content = get_tokenize(content)
    content = get_stop_word(content)
    return content

def ut(b,a):
    global answer
    strt = ""
    if len(b) != 0:
        for val in b:
            strt += "carnfield" + val + ","
        answer.append(a + strt[:-1])
    else:
        answer.append(a)

for i in range(q):
    str = input()
    query = str
    content = content_retirvel(query)

    for u in find_bigram_query(str, i + 1):
        answer.append(u)

    b = query_int(content, pos_dict_1)
    print(f"documents retrieved for query {q + 1} using p_inverted index are {len(b)}")
    a = f"Names of documents retrieved for query {q + 1} using p_inverted index are "
    ut(b,a)

for i in range(0,len(answer)):
    print(answer[i])
