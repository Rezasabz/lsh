import glob
import time
import string
import re
import multiprocessing
import os
import numpy as np

#--------------------------------------------------
#  path files
#-----------------------------------------------
path_files = glob.glob('/home/reza_rexer/Documents/Lsh/*.txt')

# docments = []

# preprocess on eache file
# def preprocess(text):
#     text = re.sub(r'[^\w\s]','',text)
#     tokens = text.lower()
#     tokens = tokens.split()
#     return tokens

shingles = []
#--------------------------------------------------
#  get k-shingle value of user
#-----------------------------------------------
while True :
    try:
        k = int(input("Please Enter k value for k-shingle: "))
    except ValueError:
        print("Your input is not valid. Give a positive natural number > 0...")
        continue
    if k <= 0:
        continue
    else:
        break

print("Shingling articles...")

#--------------------------------------------------
#  values for Matrix
#-----------------------------------------------
# columns
docs = []
# rows
shgl = []
# state
index = -1
for file in path_files:
    with open(file, 'r') as f:
        index += 1
        shingles.append([])
        time.sleep(1)
        content = f.read()
        filename = os.path.basename(file)
        docs.append(filename)
        print("-----------------------------------------------------------------------------------------------------------")
        for i in range(len(content) - k + 1):
            shingles[index].append("")
            for j in range(i, i + k):
                shingles[index][i] += content[j]
        shgl.append(shingles[index])
                #if j < (i + k - 1):
                #    shingles[index][i] += " "
        # print(shingles[index])
        print("-----------------------------------------------------------------------------------------------------------")
concat_array = np.concatenate(shgl)
unique = np.unique(concat_array)
# print(shgl)
print("==================================")
# print(np.unique(concat_array))
        # print('Reading data took %.2f sec.' % (time.time() - t0))
# matrix = []
# for i in range(len(unique)):
#     a = []
#     for j in range(len(docs)):
#         a.append(concat_array[j])
#     matrix.append(a)

# for i in range(len(unique)):
#     for j in range(len(docs)):
#         print(matrix[i][j], ' ')

#     print()


print(np.array([docs,
                unique]))

# =============================================================================
#               Create Matrix of Docs and Shingles
# =============================================================================


exit(0)
