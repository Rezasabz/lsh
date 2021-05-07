import glob
import time
import string
import re
import multiprocessing
import os
import numpy as np
import tableprint
import numpy as np
from itertools import permutations
import random
# from rich.table import Column, Table
# from rich.console import Console


# console = Console()

# --------------------------------------------------
#  path files
# -----------------------------------------------
path_files = glob.glob('*.txt')

bad_chars = [';', ':', '!', "*", ",", "\n", ".", "?", '"',"@","$","%","^","&","(",")","=","+","_","{","}","[","]","<",">","-","'"]
# docments = []

# preprocess on eache file
# def preprocess(text):
#     text = re.sub(r'[^\w\s]','',text)
#     tokens = text.lower()
#     tokens = tokens.split()
#     return tokens

shingles = []
# --------------------------------------------------
#  get k-shingle value of user
# -----------------------------------------------
# while True:
#     try:
#         k = int(input("Please Enter k value for k-shingle: "))
#     except ValueError:
#         print("Your input is not valid. Give a positive natural number > 0...")
#         continue
#     if k <= 0:
#         continue
#     else:
#         break
k = 3

# --------------------------------------------------
#  values for Matrix
# -----------------------------------------------
# temp_folder
tmp = "temp_folder"
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
        for i in bad_chars:
            content = content.replace(i,'')
            if not os.path.exists(tmp):
                os.mkdir(tmp)
            with open("temp_folder"+"/"+filename,'w') as newFile:
                newFile.write(content)
        # print("-----------------------------------------------------------------------------------------------------------")
        for i in range(len(content) - k + 1):
            shingles[index].append("")
            for j in range(i, i + k):
                shingles[index][i] += content[j]
        shgl.append(shingles[index])
        # if j < (i + k - 1):
        #    shingles[index][i] += " "
        # print(shingles[index])
        # print("-----------------------------------------------------------------------------------------------------------")
concat_array = np.concatenate(shgl)
shingle_unique = np.unique(concat_array)
# print(shingle_unique)


# print("==================================")
# print(np.unique(concat_array))
# print('Reading data took %.2f sec.' % (time.time() - t0))
mt = []
for i in glob.glob(tmp + "/" + "*.txt"):
    answer = [0] * len(shingle_unique)
    # print(answer)
    with open(i, 'r') as f:
        content = f.read()
        index = 0
        for j in shingle_unique:
            if j in content:
                answer[index] = 1
            index += 1
    mt.append(answer)

print(mt)



def creat_permutations(arr_name,limit):
    range_arr_len = []
    perm_list = []
    arr_len = len(arr_name[0])
    for i in range(1,arr_len+1):
        range_arr_len.append(i)
    perm = permutations(range_arr_len)
    for i in perm:
        perm_list.append(i)
    return random.sample(perm_list,limit)

def create_signatures(array):
    p = creat_permutations(array,3)
    signatures_list = []
    for i in range(len(p)):
        sort_list_shingles = []
        for j in array:
            zip_perm = zip(p[i],j)
            sort_perm = sorted(zip_perm)
            sort_list = [el for _, el in sort_perm]
            sort_list_shingles.append(sort_list)
        signatures = []
        for l in range(len(sort_list_shingles)):
            k = 0
            while(sort_list_shingles[l][k] != 1):
                k += 1
            signatures.append(k+1)
        signatures_list.append(signatures)
    return signatures_list


# print(create_signatures(mt))

# table = Table(show_header=True, header_style="bold magenta")
# for i in docs:
#     table.add_column(i)
# for i in range(len(shingle_unique)):
#     table.add_row(str(np.transpose(mt)[i][0]), str(np.transpose(mt)[i][1]))
# console.print(table)

# print(shingle_unique)
# =============================================================================
#               Create Matrix of Docs and Shingles
# =============================================================================
# --------------------------------------------------
#  Table of availability of shingles in documents
# -----------------------------------------------
# tableprint.table(np.transpose(mt), docs, align='center')

# exit(0)

# def create_signatures(array):
    # p = creat_permutations(array,3)
    # signatures_list = []
    # for i in range(3):
    #     p = np.random.permutation(len(array[0]+1))
    #     print(p)
    #     sort_list_shingles = []
    #     for j in array:
    #         zip_perm = zip(p,j)
    #         sort_perm = sorted(zip_perm)
    #         sort_list = [el for _, el in sort_perm]
    #         sort_list_shingles.append(sort_list)
    #         print(sort_list)
    #     signatures = []
    #     for l in range(len(sort_list_shingles)):
    #         k = 0
    #         while(sort_list_shingles[l][k] != 1):
    #             k += 1
    #         signatures.append(k+1)
    #     signatures_list.append(signatures)
    # return signatures_list