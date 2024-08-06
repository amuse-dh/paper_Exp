import pandas as pd
from sklearn.model_selection import train_test_split
from torchvision import transforms
from PIL import Image
import albumentations as A
import numpy as np


#def data path
df = pd.read_csv("C:/Users/user/train.csv")
img_dir = "C:/Users/user/train_images/"
aug_dir = "C:/Users/user/train_images/video_3/"

#add img_dir and annot
df['annotations'] = df['annotations'].apply(eval)
df['img_dir'] = img_dir + "video_" + df['video_id'].astype(str) + "/" + df['video_frame'].astype(str) + ".jpg"

for i in range(len(df)):
    df.at[i, 'annot_len'] = len(df.iloc[i]['annotations'])

#split train and valid , delete no annot data
df_train, df_valid = train_test_split(df, test_size = 0.2, random_state = 2000)
df_train = df_train[df_train.annot_len < 882].reset_index(drop = True)
df_train = df_train[df_train.annotations.str.len() > 0].reset_index(drop=True)
df_valid = df_valid[df_valid.annot_len < 882].reset_index(drop = True)
df_valid = df_valid[df_valid.annotations.str.len() > 0].reset_index(drop=True)

#mk empty list
bboxes = []
transform_dir = []
aug_box = []

#torchvision transform
transform = transforms.Compose([
    transforms.RandomOrder([
        transforms.RandomVerticalFlip(p=0.5),
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(degrees = 10)
    ])
])

#albumentation transform
A_transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.Flip(p=0.5),
    A.Rotate(p=0.5)
], bbox_params = A.BboxParams(format="coco", min_visibility = 0.4, label_fields=[],),)

#prepare bbox
for i in range(len(df_train)):
    boxes = pd.DataFrame(df_train.iloc[i]['annotations'], columns=['x', 'y', 'width', 'height']).astype(np.uint8).values
    bboxes.append(boxes[0])

print(type(bboxes))

#save img and annot
for i in range(len(df_train)):
    #img = cv2.imread(df_train.iloc[i]['img_dir'])

    img = Image.open(df_train.iloc[i]['img_dir']).convert('RGB')
    img = np.array(img)

    img = A_transform(image = img, bboxes = bboxes)

    img['image'] = Image.fromarray(img['image'])

    #img = transform(img)
    img['image'].save("C:/Users/user/train_images/video_3/" + str(i)+".jpg", 'jpeg')

    transform_dir.append("C:/Users/user/train_images/video_3/" + str(i)+".jpg")
    aug_box.append(img['bboxes'])


#add data dir

for i in range(0,3950):
    df_train.loc[i+3950] = ['3', '0', '0', '0', '0', aug_box[i], transform_dir[i], len(aug_box[i])]
    #df_train.at[i, 'img_dir'] = transform_dir[i]
    #df_train.at[i, 'annotations'] = aug_box[i]

df_train.to_csv("df_train.csv")
print(df_train)