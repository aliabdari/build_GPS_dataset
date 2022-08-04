import os

list_files = []
for file in os.listdir("./cabspottingdata"):
    if file.endswith(".txt"):
        if file.__contains__("_cabs"):
            continue
        print(os.path.join("/cabspottingdata", file))
        list_files.append('./cabspottingdata' + os.sep + file)

if os.path.exists("GPS_data.txt"):
    os.remove("GPS_data.txt")
data_file = open("GPS_data.txt", "w")


def check_boundaries(listX, listY, d):
    if 37.0 <= float(listX[d]) and float(listX[d + 1]) and float(listX[d + 2]) < 38.0:
        if -123.0 < float(listY[d]) and float(listY[d + 1]) and float(listY[d + 2]) <= 122.0:
            return True


for file in list_files:
    with open(file) as f:
        contents = f.readlines()
        list_time_stamp = []
        list_x = []
        list_y = []
        contents.reverse()
        for c in contents:
            list_time_stamp.append(int(c.split(" ")[-1][:-1]))
            list_x.append(c.split(" ")[0][:-1])
            list_y.append(c.split(" ")[1][:-1])
        differences = [x - list_time_stamp[i - 1] for i, x in enumerate(list_time_stamp)][1:]
        for d in range(len(differences) - 1):
            if 55 < differences[d] < 65 and 55 < differences[d + 1] < 65:
                if check_boundaries(list_x, list_y, d):
                    data_file.write(list_x[d] + "," + list_y[d])
                    data_file.write(",")
                    data_file.write(list_x[d + 1] + "," + list_y[d + 1])
                    data_file.write(",")
                    data_file.write(list_x[d + 2] + "," + list_y[d + 2])
                    data_file.write("\n")
    print("one file finished")
data_file.close()

print('Processed')
