import cv2
import numpy as np
import csv
from sklearn.externals import joblib

# input parameter
sub_pic_size = 150
window_size = 1
im_main = cv2.imread('pic/input.jpg')
base_clusters_path = 'clusters/'


# #################### load map file ####################
def load_map_file(file_name):
    csv_file = open(base_clusters_path + '/map_files/' + str(file_name) + '.csv', mode='r')
    csv_reader = csv.DictReader(csv_file)
    rows = list(csv_reader)
    return rows


# #################### load clustering model ####################
model = joblib.load(base_clusters_path + 'cluster.pkl')


def find_closest_sub_pic(rgb_px, sub_size, csv_reader_):
    min_dif_value = 800
    min_dif_path = ""

    for row in csv_reader_:
        dif = abs(rgb_px[0] - int(row["r"])) + abs(rgb_px[1] - int(row["g"])) + abs(rgb_px[2] - int(row["b"]))
        if dif < min_dif_value:
            min_dif_value = dif
            min_dif_path = row["path"]
            # print(min_dif_path)

    sub_im = cv2.imread('data/normal/' + min_dif_path)
    sub_im = cv2.resize(sub_im, (sub_size, sub_size))
    return sub_im


v_tmp = []
for i in range(0, im_main.shape[0] - window_size, window_size):
    h_tmp = []
    for j in range(0, im_main.shape[1] - window_size, window_size):
        tmp = im_main[i: i + window_size, j: j + window_size]
        r = int(np.round(np.average(tmp[:, :, 0])))
        g = int(np.round(np.average(tmp[:, :, 1])))
        b = int(np.round(np.average(tmp[:, :, 2])))

        cluster = model.predict([[r, g, b]])
        h_tmp.append(find_closest_sub_pic([r, g, b], sub_pic_size, load_map_file(cluster[0])))
    v_tmp.append(cv2.hconcat(h_tmp))

im_master = cv2.vconcat(v_tmp)
cv2.imwrite('pic/output.png', im_master)

print("done!")
