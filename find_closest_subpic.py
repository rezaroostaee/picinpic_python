import numpy as np
import csv

main_pix = [80,90,40]

min_dif_value = 800
min_dif_path = ""

with open('rgb_file.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        dif = abs(main_pix[0] - int(row["r"])) + abs(main_pix[1] - int(row["g"])) + abs(main_pix[2] - int(row["b"]))
        if dif < min_dif_value:
            min_dif_value = dif
            min_dif_path = row["path"]
    print(min_dif_path)