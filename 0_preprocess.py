import cv2
import glob
import numpy as np
import csv

dis_file_path = "data/normal/"
image_list = []
cnt = 0

with open('clusters/rgb_file.csv', mode='w') as employee_file:
    rgb_archive = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    rgb_archive.writerow(["path", "r", "g", "b"])

    for filename in glob.glob('data/raw/*.jpg'):  # assuming gif
        # filename = "E:/project/payCharm/nnProject/datasets/svhn/train/1.png"
        im = cv2.imread(filename)
        im = cv2.resize(im, (im.shape[0], im.shape[0]))

        cv2.imwrite(dis_file_path + str(cnt) + ".jpg", im)
        r_avg = int(np.round(np.average(im[:, :, 0])))
        g_avg = int(np.round(np.average(im[:, :, 1])))
        b_avg = int(np.round(np.average(im[:, :, 2])))

        rgb_archive.writerow([str(cnt) + ".jpg", r_avg, g_avg, b_avg])
        cnt += 1
        image_list.append(im)
