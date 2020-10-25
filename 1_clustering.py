import csv
import os
import shutil

from sklearn.cluster import KMeans
from sklearn.externals import joblib

k = 391
cluster_file_path = "clusters/map_files/"
# ######################### load input_data #############################
data = []
path = []
with open('clusters/rgb_file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        data.append([row["r"], row["g"], row["b"]])
        path.append(row["path"])

# ######################### create directory #############################
    if os.path.exists(cluster_file_path):
        shutil.rmtree(cluster_file_path)
    os.mkdir(cluster_file_path)

# ######################### train and save model #############################
model = KMeans(n_clusters=k).fit(data)
centroids = model.cluster_centers_
print(centroids)

joblib.dump(model, 'clusters/cluster.pkl')


# ######################### load model and predict inputs #############################
model = joblib.load('clusters/cluster.pkl')
cluster = model.predict(data)


# ######################### create separated file #############################
dic = []
for i in range(k):
    dic.append([])

for j in range(path.__len__()):
    dic[cluster[j]].append([path[j], data[j]])

for i in range(k):
    tmp = dic[i]
    with open(cluster_file_path + str(i) + ".csv", mode='w') as clu_file:
        archive = csv.writer(clu_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        archive.writerow(["path", "r", "g", "b"])
        for j in range(dic[i].__len__()):
            archive.writerow([tmp[j][0], tmp[j][1][0], tmp[j][1][1], tmp[j][1][2]])





