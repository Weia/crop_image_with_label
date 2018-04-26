# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 8:48
# @Author  : weic
# @FileName: merge_label.py
# @Software: PyCharm

#合并裁剪后的label文件，天池数据集中的
import numpy as np
from PIL import  Image
import matplotlib.pyplot as plt

def merge_labels_file(file1,file2,out_file_name='merge_result.txt'):
    #选出有六个点的line保存到新的文件
    res_f=open('./'+out_file_name,'w')
    with open(file1) as f1:
        content=f1.readlines()
        for line in content:
            list_line=line.split(' ')
            labels=np.asarray([float(x) for x in list_line[1:-1]]).reshape(-1,2)
            if [0.0,0.0] in labels:
                continue
            else:
                res_f.write(line)
    with open(file2) as f2:
        content=f2.readlines()
        for line in content:
            list_line=line.split(' ')
            labels=np.asarray([float(x) for x in list_line[1:-1]]).reshape(-1,2)
            if [0.0,0.0] in labels:
                continue
            else:
                res_f.write(line)
    res_f.close()



file1='./merge_label/dress_label.txt'
file2='./merge_label/outwear_label.txt'

merge_labels_file(file1,file2)

# with open(r'merge_label/merge_result.txt') as f:
#     content=f.readlines()
#     for line in content:
#         new=line.split(' ')
#         name=new[0]
#         category=name.split('.')[0].split('_')[0]
#
#         label=new[1:-1]
#         #print(name)
#         img=Image.open(r'D:\数据集\数据集\tianchi_part_image'+'\\'+category+'\\'+name)
#         new_label=np.asarray([float(x) for x in label]).reshape(-1,2)
#         plt.plot(new_label[:,0],new_label[:,-1],'r*')
#
#         plt.imshow(img)
#         plt.show()