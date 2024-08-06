import os

def voting(start_point):
    path1 = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/runs/detect/new10_1/labels/"+str(start_point)+".txt"
    path2 = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/runs/detect/new10_2/labels/"+str(start_point+1)+".txt"
    path3 = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/runs/detect/new10_3/labels/"+str(start_point+2)+".txt"
    path4 = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/runs/detect/new10_4/labels/"+str(start_point+3)+".txt"
    path5 = "C:/Users/user/PycharmProjects/pythonProject1/yolov5-master/runs/detect/new10_5/labels/"+str(start_point+4)+".txt"

    cls0 = []
    cls1 = []
    cls2 = []
    cls3 = []
    cls4 = []
    cls5 = []
    cls6 = []
    cls7 = []

    with open(path1, "r") as file1:
        vote1 = file1.readlines()
        for i in range(len(vote1)):
            vote1[i] = vote1[i].split()
            if vote1[i][0] == "0":
                cls0.append(1)
            elif vote1[i][0] == "1":
                cls1.append(1)
            elif vote1[i][0] == "2":
                cls2.append(1)
            elif vote1[i][0] == "3":
                cls3.append(1)
            elif vote1[i][0] == "4":
                cls4.append(1)
            elif vote1[i][0] == "5":
                cls5.append(1)
            elif vote1[i][0] == "6":
                cls6.append(1)
            elif vote1[i][0] == "7":
                cls7.append(1)
            else:
                continue

    with open(path2, "r") as file2:
        vote2 = file2.readlines()
        for i in range(len(vote2)):
            vote2[i] = vote2[i].split()
            if vote2[i][0] == "0":
                cls0.append(1)
            elif vote2[i][0] == "1":
                cls1.append(1)
            elif vote2[i][0] == "2":
                cls2.append(1)
            elif vote2[i][0] == "3":
                cls3.append(1)
            elif vote2[i][0] == "4":
                cls4.append(1)
            elif vote2[i][0] == "5":
                cls5.append(1)
            elif vote2[i][0] == "6":
                cls6.append(1)
            elif vote2[i][0] == "7":
                cls7.append(1)
            else:
                continue

    with open(path3, "r") as file3:
        vote3 = file3.readlines()
        for i in range(len(vote3)):
            vote3[i] = vote3[i].split()
            if vote3[i][0] == "0":
                cls0.append(1)
            elif vote3[i][0] == "1":
                cls1.append(1)
            elif vote3[i][0] == "2":
                cls2.append(1)
            elif vote3[i][0] == "3":
                cls3.append(1)
            elif vote3[i][0] == "4":
                cls4.append(1)
            elif vote3[i][0] == "5":
                cls5.append(1)
            elif vote3[i][0] == "6":
                cls6.append(1)
            elif vote3[i][0] == "7":
                cls7.append(1)
            else:
                continue

    with open(path4, "r") as file4:
        vote4 = file4.readlines()
        for i in range(len(vote4)):
            vote4[i] = vote4[i].split()
            if vote4[i][0] == "0":
                cls0.append(1)
            elif vote4[i][0] == "1":
                cls1.append(1)
            elif vote4[i][0] == "2":
                cls2.append(1)
            elif vote4[i][0] == "3":
                cls3.append(1)
            elif vote4[i][0] == "4":
                cls4.append(1)
            elif vote4[i][0] == "5":
                cls5.append(1)
            elif vote4[i][0] == "6":
                cls6.append(1)
            elif vote4[i][0] == "7":
                cls7.append(1)
            else:
                continue

    with open(path5, "r") as file5:
        vote5 = file5.readlines()
        for i in range(len(vote5)):
            vote5[i] = vote5[i].split()
            if vote5[i][0] == "0":
                cls0.append(1)
            elif vote5[i][0] == "1":
                cls1.append(1)
            elif vote5[i][0] == "2":
                cls2.append(1)
            elif vote5[i][0] == "3":
                cls3.append(1)
            elif vote5[i][0] == "4":
                cls4.append(1)
            elif vote5[i][0] == "5":
                cls5.append(1)
            elif vote5[i][0] == "6":
                cls6.append(1)
            elif vote5[i][0] == "7":
                cls7.append(1)
            else:
                continue

    with open("C:/Users/user/Desktop/voting4/" + str(i) + ".txt", "w") as vote:
        if len(cls0) >= 3:
            vote.write("0\n")
        if len(cls1) >= 3:
            vote.write("1\n")
        if len(cls2) >= 3:
            vote.write("2\n")
        if len(cls3) >= 3:
            vote.write("3\n")
        if len(cls4) >= 3:
            vote.write("4\n")
        if len(cls5) >= 3:
            vote.write("5\n")
        if len(cls6) >= 3:
            vote.write("6\n")
        if len(cls7) >= 3:
            vote.write("7\n")
