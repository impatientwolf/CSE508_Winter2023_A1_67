import os
import pickle
dict={}
master=[]





def create_dict(file_path):
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
        temp = f.read()
        wordset = set()
        master.append(str(file_no))
        templist=[]
        for word in temp.split(" "):
            templist.append(word)
        for i in templist:
            if i not in dict:
                dict[i] = []
            if i not in wordset:
                wordset.add(i)
                dict[i].append(file_no)
                

    for word in dict.keys():
        print(word, dict[word])








def dumper():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    pickling_on1 = open("dictionary.pickle","wb")
    pickle.dump(dict, pickling_on1)
    pickling_on2 = open("number_list.pickle","wb")
    pickle.dump(master, pickling_on2)

create_dict("")
dumper()
