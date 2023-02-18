#파일경로를 지정하고 다시 피클로 load를 하면 된다.
#이렇게 하면 list_final이라는 변수에 리스트가 할당됨
#현재 폴더 위치에 해당 list_final.txt파일이 있으면 

import pickle


filePath = './list_final.txt'

with open(filePath, 'rb') as lf:
    list_final = pickle.load(lf)
