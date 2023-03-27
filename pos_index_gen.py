path = r"C:\Users\Priyanshu\Downloads\CSE508_Winter2023_A1_66\CSE508_Winter2023_Dataset"
import os
from nltk import word_tokenize
import os
import pickle

position={}

def create():
    
    # for file in sorted(os.listdir()):
    #     file_path = f"{path}/{file}"
    #     with open(file_path, 'r') as f:    

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

            f = open(path, "r")
            content=str(f.read())
            tokens = word_tokenize(content)
            templist=[]
            for i in range(len(tokens)):
                templist.append(tokens[i])
            for token in templist:
                # token= tokens[i]

                if token not in position:
                    position[token] = {}
                doc_dict=position[token]
                if file_no not in doc_dict:
                    doc_dict[file_no] = []
                doc_dict[file_no].append(i)




def dumper():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    pickling = open("pos_dict.pickle","wb")
    pickle.dump(position, pickling)
    pickling.close()

create()
dumper()



