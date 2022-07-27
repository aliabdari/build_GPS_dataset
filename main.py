import os

list_files = []
for file in os.listdir("./cabspottingdata"):
    if file.endswith(".txt"):
        print(os.path.join("/cabspottingdata", file))
        list_files.append('./cabspottingdata' + os.sep + file)

for file in list_files:
    with open(file) as f:
        contents = f.readlines()
        print(contents)

print('Processed')
