import pandas as pd
import yaml
import shutil
from sklearn.model_selection import train_test_split


tr_img_dir = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/data/images/train/images/"
vld_img_dir = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/data/images/valid/images/"
tr_label_dir = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/data/images/train/labels/"
vld_label_dir = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/data/images/valid/labels/"

df = pd.read_csv("conv_prod")

df_train, df_valid = train_test_split(df, test_size = 0.2, random_state = 100)

df_train['label_dst'] = tr_label_dir + df['folder'].astype(str) + "_" + df['f_name'].astype(str) + ".txt"
df_train['img_dst'] = tr_img_dir + df['folder'].astype(str) + "_" + df['f_name'].astype(str) + ".png"

df_valid['label_dst'] = vld_label_dir + df['folder'].astype(str) + "_"+ df['f_name'].astype(str) + ".txt"
df_valid['img_dst'] = vld_img_dir + df['folder'].astype(str) + "_"+ df['f_name'].astype(str) + ".png"

"""
for i in range(len(df_train)):
    with open(df_train.iloc[i]['label_src'],"r") as src:
        lines = src.readlines()

        #class
        lines[0] = lines[0].rstrip()
        #box
        lines[1] = lines[1].rstrip()

        boxes = lines[1].split()
        cls_name = str(boxes[4:])
        boxes = boxes[:4]

        cls_name = cls_name.strip("[]").replace(",", "").replace("'", "")

        boxes[0] = int(boxes[0])
        boxes[1] = int(boxes[1])
        boxes[2] = int(boxes[2])
        boxes[3] = int(boxes[3])

        width = (boxes[2] - boxes[0]) / image_width
        height = (boxes[3] - boxes[1]) / image_height
        x_cen = ((boxes[2] + boxes[0]) / 2) / image_width
        y_cen = ((boxes[3] + boxes[1]) / 2) / image_height

        boxes[0] = x_cen
        boxes[1] = y_cen
        boxes[2] = width
        boxes[3] = height

        lines[1] = boxes
        lines[1] = str(lines[1]).strip("[]").replace(",", "")

    with open("C:/Users/user/Desktop/labels/train/"+df_train.iloc[i]["f_name"]+".txt", "w") as dst:
        dst.write(lines[0] + " " + lines[1])
        #for j in range(len(lines)):
            #dst.write(str(lines[j])+ + " ")

for i in range(len(df_valid)):
    with open(df_valid.iloc[i]['label_src'], "r") as src:
        lines = src.readlines()
        # class
        lines[0] = lines[0].rstrip()
        # box
        lines[1] = lines[1].rstrip()

        boxes = lines[1].split()
        cls_name = str(boxes[4:])
        boxes = boxes[:4]

        cls_name = cls_name.strip("[]").replace(",", "").replace("'", "")

        boxes[0] = int(boxes[0])
        boxes[1] = int(boxes[1])
        boxes[2] = int(boxes[2])
        boxes[3] = int(boxes[3])

        width = (boxes[2] - boxes[0]) / image_width
        height = (boxes[3] - boxes[1]) / image_height
        x_cen = ((boxes[2] + boxes[0]) / 2) / image_width
        y_cen = ((boxes[3] + boxes[1]) / 2) / image_height

        boxes[0] = x_cen
        boxes[1] = y_cen
        boxes[2] = width
        boxes[3] = height

        lines[1] = boxes
        lines[1] = str(lines[1]).strip("[]").replace(",", "")

    with open("C:/Users/user/Desktop/labels/valid/"+df_valid.iloc[i]["f_name"]+".txt","w") as dst:
        dst.write(lines[0] + " " + lines[1])

"""

for i in range(len(df_train)):

    shutil.copy(src=df_train.iloc[i]['img_src'], dst=df_train.iloc[i]['img_dst'])
    shutil.copy(src=df_train.iloc[i]["label_src"], dst=df_train.iloc[i]['label_dst'])
for i in range(len(df_valid)):

    shutil.copy(src=df_valid.iloc[i]['img_src'], dst=df_valid.iloc[i]['img_dst'])
    shutil.copy(src=df_valid.iloc[i]["label_src"], dst=df_valid.iloc[i]['label_dst'])

data_format = {'train' : "train_dir", "val" : "val_dir", "nc" : 8, "name" : ["toilet_paper", "ice_cream", "soda", "cup_rice", "oreo", "tooth_paste", "curry", "coca_cola"]}

with open("train.txt", "w") as f:
    f.write('\n'.join(df_train['img_dst'])+'\n')

with open("val.txt", "w") as f:
    f.write('\n'.join(df_valid['img_dst'])+'\n')

with open("tr_data.yaml", "w") as d:
    yaml.dump(data_format, d)

with open("tr_data.yaml", 'r') as d:
    data = yaml.load(d, Loader=yaml.FullLoader)
    data['train'] = "C:/Users/user/PycharmProjects/pythonProject1/train.txt"
    data['val'] = "C:/Users/user/PycharmProjects/pythonProject1/val.txt"

with open("tr_data.yaml", "w") as d:
    yaml.dump(data, d)
