import pandas as pd
from get_data import mk_column as c

img = []
folder = []
image_dir = "C:/Users/user/Desktop/object_data/"
label_dir = "C:/Users/user/Desktop/object_data/"

img, folder = c(img, folder)

df = pd.DataFrame({'f_name': img,
                   'folder': folder, })

print(df)

for i in range(len(df)):
    df.at[i, 'image_dir'] = image_dir
    df.at[i, 'label_dir'] = label_dir

df['img_src'] = df['image_dir'].astype(str) + df['folder'].astype(str) + "/"+ df['f_name'].astype(str) + ".png"
df['label_src'] = df['label_dir'].astype(str) + df['folder'].astype(str) + "/"+ df['f_name'].astype(str) + ".txt"

print(df)

df.to_csv('conv_prod')
