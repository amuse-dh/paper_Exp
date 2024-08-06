import os

path = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/data/images/valid/images"
names = os.listdir(path)
des = "/home/dhjeon/yolov7/data/valid/images/"

with open("val_linux.txt", "w") as f:
    for i in range(len(names)):
        f.write(des+ names[i] +'\n')
