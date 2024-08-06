import os
import natsort



def odr(ground_truth_path ,target_path):
    labels = os.listdir(target_path)
    labels = natsort.natsorted(labels)

    labels_txt = []

    for i in range(len(labels)):
        if ".txt" in labels[i]:
            labels_txt.append(labels[i])

    ground_truth_labels = os.listdir(ground_truth_path)
    ground_truth_labels = natsort.natsorted(ground_truth_labels)

    ground_truth_labels_txt = []

    for i in range(len(ground_truth_labels)):
        if ".txt" in ground_truth_labels[i]:
            if "classes" not in ground_truth_labels[i]:
                ground_truth_labels_txt.append(ground_truth_labels[i])
                print(ground_truth_labels[i])

    count_of_detect = 0
    count_of_label = 0

    for label in labels_txt:
        with open(target_path+label,"r") as detection_result:
            label_count = detection_result.readlines()
            count_of_detect += len(label_count)

    print("count of detect : " +str(count_of_detect))

    for ground_truth in ground_truth_labels_txt:
        with open(ground_truth_path+ground_truth, "r") as labeling_result:
            ground_cont = labeling_result.readlines()
            count_of_label += len(ground_cont)

    print("count of label : " +str(count_of_label))

    detection_rate = count_of_detect/count_of_label
    detection_rate = detection_rate*100

    print("detection rate : " +str(detection_rate)+"%")

    with open("detection_rate_vanila.txt", "w") as file:
        file.write("count of detect : " +str(count_of_detect)+"\n")
        file.write("count of label : " + str(count_of_label) + "\n")
        file.write("detection rate : " + str(detection_rate) + "\n")


odr("C:/Users/user/Desktop/final_test/", "C:/Users/user/PycharmProjects/yolo_v5/runs/detect/bag24/labels/")



#87.7%
#68.26%

