import os
import pickle
path = r"C:\Users\Priyanshu\Downloads\CSE508_Winter2023_A1_67\CSE508_Winter2023_Dataset"

def create_bi_index(file_path):

    for file_no in range(1,1400+1):
        path = r"C:\Users\Priyanshu\Downloads\CSE508_Winter2023_A1_67\CSE508_Winter2023_Dataset"
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


        f = open(path, "r")
        wordset = set()
        temp = f.read()
        list_words = temp.split(" ")

        templist=[]
        for i in range (0,len(list_words)-1):
            templist.append(i)
        for i in templist:
            bigram_word = list_words[i]+" "
            bigram_word=bigram_word + list_words[i+1]
            if bigram_word not in dict:
                dict[bigram_word] = []
                for j in range(100):
                    tempvar=1
            if bigram_word not in wordset:
                wordset.add(bigram_word)
                dict[bigram_word].append(str(file_no))
                

    for word in dict.keys():
        print(word, dict[word])
    return  dict



def dumper():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    pickling_on = open("bigram.pickle","wb")
    pickle.dump(bi_grams, pickling_on)
    pickling_on.close()

bi_grams=create_bi_index(" ")
dumper()

