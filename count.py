import pandas as pd
import re
import csv

path = "C:/User/users/PycharmProjects/pythonProject1/yolov5-master/runs/detect/exp20/labels/"

fir_cnt = 1
fields = ['product', 'cnt']

event = 1

def count(i):
    f = []
    if i>0:
        with open(path + "1_" + str(i) + ".txt", 'a+') as txt1:
            txt1 = open(path + "1_" + str(i) + ".txt", 'r')

            first = txt1.readlines() #첫번쨰 파일 읽어오기

            for k in range(len(first)):
                first_list = re.findall('\d+',first[k])
                f.append(first_list[0]) #첫번째 파일의 클래스만 f에 저장

                with open('count.csv', 'w', newline='') as file:  # csv파일 open
                    # using csv.writer method from CSV package
                    write = csv.writer(file)
                    write.writerow(fields)  # 행 레이블 write
                    file.close()
                df = pd.read_csv('count.csv')  # csv파일 read
                for p in range(len(f)):
                    if f[p] in df['product'].tolist():
                        idx = df['product'].values.tolist().index(f[p])
                        cnt = int(df.loc[idx, 'cnt'])
                        cnt = cnt + 1
                        df.loc[idx, 'cnt'] = cnt
                    else:
                        df.loc[p] = [f[p], fir_cnt]  # 첫 프레임에서 재고 저장

        for x in range(len(df)):
            if int(df.loc[x, 'cnt']) == 0:
                df = df.drop(x)
        df.to_csv("count.csv", index=False, mode='w')
