def rw_label(df):
    for i in range(len(df)):
        src = open(df.iloc[i]['label_src'])
        dst = open("label"+str(i)+".txt")
        lines = src.readlines()

        for j in range(len(lines)):
            dst.write(lines[j])



