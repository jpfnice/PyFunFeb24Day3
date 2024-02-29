
# afile = open("data.txt")

# for line in afile:
#     print(line)

# afile.close()

import os.path
fileName=input("Name of the file to read: ")
if os.path.exists(fileName):
    with open(fileName) as afile:
        for line in afile:
            print(line)
else:
    print(f"{fileName} does not exists")
    
print("The end")