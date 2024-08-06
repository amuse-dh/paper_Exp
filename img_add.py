import cv2
import os
import numpy as np

'''
img_path = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/data/images/train/images/"
label_path = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/data/images/train/labels/"

#path = "C:/Users/user/Desktop/data/soda/"
back_path = "C:/Users/user/Desktop/0000_00/"

back_ids = os.listdir(back_path)
image_ids = os.listdir(img_path)
#txt_ids = os.listdir(label_path)
train_txt = []

extra_data_path = "C:/Users/user/Desktop/data/curry/"
label_ids = os.listdir(extra_data_path)

txt = []
image = []

for i in range(len(label_ids)):
    if ".txt" in label_ids[i]:
        txt.append(label_ids[i])
    else:
        image.append(label_ids[i])
'''

'''
for i in range(len(image_ids)):
     image_ids[i] = image_ids[i].replace(".png","")

for i in range(len(image_ids)):
    txt_ids[i] = txt_ids[i].replace(".txt","")
    #txt_ids.append(image_ids[i])

for i in range(len(image_ids)):
    if image_ids[i] in txt_ids:
        train_txt.append(image_ids[i])


for i in range(len(txt)):
    txt = open(extra_data_path + txt[i], "r")
    copy = open("C:/Users/user/Desktop/datas/"+train_txt[i]+".txt", "w")

    data = txt.read()
    copy.write(data)

    txt.close()
    copy.close()
'''

'''
for j in range(1,9):
    for i in range(len(txt)):
        txt_file = open(extra_data_path + txt[i], "r")
        copy = open("C:/Users/user/Desktop/datas/"+str(j)+"_"+str(i+484)+".txt", "w")

        data = txt_file.read()
        copy.write(data)

        txt_file.close()
        copy.close()
'''


'''
for i in range(len(ids)):
    if ".png" in ids[i]:
        image_ids.append(ids[i])
        
for i in range(len(image_ids)):
    back_ground = cv2.imread(back_path + back_ids[i])
    img = cv2.imread(path + image_ids[i])
    #back_ground = back_ground.resize(1080, 1920)

    img_back_sub = img - back_ground
    #img_back_sub = np.where(np.logical_and((img <back_ground+2 ),(img > back_ground-2)), 0, 255)
    img_back_sub = np.where(img_back_sub <250, 0, 1)

    cv2.imwrite("./sub/"+str(i)+".png",img_back_sub)



mask_path = "C:/Users/user/PycharmProjects/pythonProject1/sub/"
mask_id = os.listdir(mask_path)
mask_ids = []

for i in range(len(mask_id)):
    for j in range(len(mask_id)):
        if str(i)+".png" == mask_id[j]:
            mask_ids.append(mask_id[j])


print(image_ids)
print(mask_ids)


for i in range(len(image_ids)):
    mask = cv2.imread(mask_path + mask_ids[i])
    img = cv2.imread(path + image_ids[i])

    #back_ground = back_ground.resize(1920, 1080)

    mask_mult_img = img*mask
    #img_back_sub = np.where(np.logical_and((img <back_ground+2 ),(img > back_ground-2)), 0, 255)
    #img_back_sub = np.where(img_back_sub <220, 0, 1)

    cv2.imwrite("./mult/"+str(i)+".jpg",mask_mult_img)
'''


path = "C:/Users/user/Desktop/data/vanila/soda/"
from pathlib import Path
from rembg import remove, new_session

session = new_session()

for file in Path(path).glob("*.png"):
    input_path = str(file)
    output_path = str('./sub/' + (file.stem+".out.png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session)
            o.write(output)


#백그라운드 합성

import natsort

path = "C:/Users/user/PycharmProjects/pythonProject1/sub/"
back_ground_path = "C:/Users/user/Desktop/new__folder2/"
txt_path = "C:/Users/user/Desktop/data/vanila/soda/"
aug_ids = os.listdir(path)

txt_ids = os.listdir(txt_path)
txt = []
for i in range(len(txt_ids)):
    if ".txt" in txt_ids[i]:
        txt.append(txt_ids[i])

txt = natsort.natsorted(txt)


for i in range(1,9):
    back_ground = cv2.imread(back_ground_path+str(i)+".png")
    #back_ground = np.asarray(back_ground)

    for j in range(len(aug_ids)):
        img = cv2.imread(path+aug_ids[j])

        if img.shape == (1079,1919,3) or back_ground.shape == (1079,1919,3):
            continue
        else:
            img = np.where(img == 0, back_ground, img)
            with open(txt_path+txt[j],"r") as file:
                og_file = file.read()
                with open("C:/Users/user/Desktop/data/606_back/soda/"+str(i)+"_"+str(j)+".txt", "w") as new_file:
                    new_file.write(og_file)

            #img = np.array(img)
            cv2.imwrite("C:/Users/user/Desktop/data/606_back/soda/"+str(i)+"_"+str(j)+".png", img)


'''
path = "C:/Users/user/Desktop/data/"
path2 = "C:/Users/user/Desktop/label/"

txt = []
for i in range(1,2):
    file_list = os.listdir(path+"cantata/")
    for k in file_list:
        if ".txt" in k:
           txt.append(k)

    for j in range(622, 712):

        file1 = open(path+"cantata/"+txt[j-621], "r")
        data = file1.read()

        file2 = open(path2+str(i)+"_"+str(j)+".txt", "w")

        file2.write(data)

        file1.close()
        file2.close()
'''

'''
path = "C:/Users/user/Desktop/label/"
txt = os.listdir(path)
print(len(txt))

for i in range(2,10):
    for j in range(len(txt)):

        if j+1 == 69 or j+1 == 137 or j+1 == 138 or j+1 == 207 or j+1 == 206 or j+1 == 276 or j+1 == 275 or j+1 == 345 or j+1 == 344 or j+1 == 437 or j+1 == 436 or j+1 == 529 or j+1 == 528 or j+1 == 621 or j+1 == 620 or j+1 == 712 or j+1 == 713 or j+1 == 714:
            continue
        else:
            file1 = open(path+"1_"+str(j+1)+".txt", 'r')
            file2 = open(path+str(i)+"_"+str(j+1)+".txt", 'w')
            a = file1.read()
            file2.write(a)

            file1.close()
            file2.close()

'''
'''
path = "C:/Users/user/Desktop/data/cantata/"
files = os.listdir(path)
txt = []
for i in files:
    if ".txt" in i:
        txt.append(i)

for i in txt:
    file1 = open(path+i,"r")
    a = file1.readline().split()

    a[0] = "8"

    file2 = open(path+i,"w")
    file2.write(a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4])

    file1.close()
    file2.close()
'''





