import fileinput

import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk import word_tokenize,sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')

# def lower_str(para):
#     return para.lower()

# def get_tokenize(para):
#     return word_tokenize(para)

# def get_stop_word(word_token):
#     stop_words = set(stopwords.words('english'))
#     without_stop_word=[]
#     for w in word_token:
#         if w not in stop_words:
#             without_stop_word.append(w)
#     return without_stop_word


# def remove_blank_spces(tokens):
#      new_token=[]
#      for  i in tokens:
#          if i==" ":
#              continue
#          else:
#              new_token.append(i)
#      return new_token


# path= r"C:\Users\Priyanshu\Downloads\CSE508_Winter2023_A1_66\CSE508_Winter2023_Dataset"

def edit_file(file_path):

    for file_no in range(1,1400+1):
        path = r"C:\Users\Priyanshu\Downloads\CSE508_Winter2023_A1_66\CSE508_Winter2023_Dataset"
        if(file_no<10):
            file_no="000"+str(file_no)
            path = path + "\\"+"cranfield"+str(file_no)
        elif(file_no<100):
            file_no="00"+str(file_no)
            path = path + "\\"+"cranfield"+str(file_no)
        elif(file_no<1000):
            file_no="0"+str(file_no)
            path = path + "\\"+"cranfield"+str(file_no)
        else:
            path = path + "\\"+"cranfield"+str(file_no)

        f=open(path,"r")
        content= str(f.read())
        f.close()

        # print("intital content",content)
        content= content.lower()
        content = content.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(content)

        stop_words = set(stopwords.words('english'))
        without_stop_word=[]
        for w in tokens:
            if w not in stop_words:
                without_stop_word.append(w)
        
        final_tokens=without_stop_word
        # print("final_content",final_tokens)

        f=open(file_path,"w")

        for item in final_tokens:
            f.write(item + " ")
        f.close()


path= r"C:\Users\Priyanshu\Downloads\CSE508_Winter2023_A1_66\CSE508_Winter2023_Dataset"
edit_file(path)





