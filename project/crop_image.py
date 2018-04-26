# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:39
# @Author  : weic
# @FileName: crop_image.py
# @Software: PyCharm
import numpy as np
import os
from PIL import Image
import csv
import matplotlib.pyplot as plt
def _open_label_file(label_file):

    with open(label_file) as f:
        contents=f.readlines()

    return contents
def _parse_a_line(line,position):

    list_line=line.split(' ')
    imgName=list_line[0]

    float_labels=np.asarray([float(x) for x in list_line[1:-1]]).reshape(-1,2)
    valid_label=float_labels[position,:]#有效label

    return imgName,valid_label
def _crop_image(img_dir,imgName,label):
    img_path=os.path.join(img_dir,imgName)
    ##print(label)
    img = Image.open(img_path)
    img_width,img_height=img.size
    ##print('img_width',img_width,img_height)
    no_zero_label=np.asarray([x for x in label if not np.array_equal(x,[0.0,0.0])]).reshape(-1,2)
    if len(no_zero_label)==0:
        raise IndexError
    else:
        x_min,y_min=np.min(no_zero_label,axis=0)
        x_max,y_max=np.max(no_zero_label,axis=0)
        width=x_max-x_min
        height=y_max-y_min
        width=(600 if width<20 else width)
        height=(600 if height<20 else height)
        #print('width',width,height)
        x_min=(1 if x_min-width*0.2<0 else x_min-width*0.2)
        y_min=(1 if y_min-height*0.2<0 else y_min-height*0.2)
        x_max = (img_width-1 if x_max + width * 0.2>img_width else x_max + width * 0.2)
        y_max = (img_height-1 if y_max + height * 0.2>img_height else y_max + height * 0.2)
        #print('xy',x_min,x_max,y_min,y_max)
        for index,point in enumerate(label):
            ##print(point)
            if not np.array_equal(point,[0.0,0.0]):
                label[index, 0]=label[index,0]-x_min
                label[index, 1]=label[index,1]-y_min
        ##print(label)


        part_image=img.crop((x_min,y_min,x_max,y_max))
        # plt.imshow(part_image)
        # plt.plot(label[:,0],label[:,1])
        # plt.show()
        #
        return part_image,label

def _save_img_label(img,imgName,path,label):
    category=path.split('\\')[-1]
    img_save_path=path+'\\'+category+'_'+imgName
    label_save_path=path+'\\'+category+'_label.txt'
    img.save(img_save_path)
    line=''
    list_label=label.reshape(1,-1).tolist()[0]
    line+=category+'_'+imgName
    for point in list_label:
        str_point=' ' +str(round(point,4))#保留4位小数
        line+=str_point
    ##print(line)
    with open(label_save_path,'a') as f:
        f.write(line)
        f.write(' \n')
    pass

def crop_image_use_label(img_dir,label_file,position,save_path):
    """
    crop image by label
    """
    file_contents=_open_label_file(label_file)
    for index,line in enumerate(file_contents):
        print(index+1)
        imgName,label=_parse_a_line(line,position)
        try:
            img,label=_crop_image(img_dir,imgName,label)
        except IndexError:
            continue
        _save_img_label(img,imgName,save_path,label)
        if index>50:
            break


def _open_csv_file(label_file_path):
    f=open(label_file_path)
    content=csv.reader(f)
    return content


def _parse_tc_line(line,posi):
    img_relative_path=line[0]
    posi_labels=[line[x] for x in posi]
    x_y_labels=np.asarray([x.split('_')[:-1] for x in posi_labels]).astype(np.float32)
    valid_labels=np.asarray([x if not np.array_equal(x,[-1.0,-1.0]) else [0.0,0.0] for x in x_y_labels]).reshape(-1,2)
    #print(valid_labels)
    return img_relative_path,valid_labels
    pass


def crop_tianchi_images(label_file_path,posi,save_image_path,img_dir):
    file_content=_open_csv_file(label_file_path)
    for index,line in enumerate(file_content):
        print(index+1)
        img_relative_path,labels=_parse_tc_line(line,posi)
        try:
            part_image,labels=_crop_image(img_dir,img_relative_path,labels)
        except IndexError:
            continue
        imgName=img_relative_path.split('/')[-1]
        _save_img_label(part_image,imgName,save_image_path,labels)
    print('*'*20,'Done','*'*20)

#
# with open(r'D:\数据集\数据集\tianchi_part_image\blouse\blouse_label.txt') as f:
#     content=f.readlines()
#     for line in content:
#         new=line.split(' ')
#         name=new[0]
#         label=new[1:-1]
#         #print(name)
#         img=Image.open(r'D:\数据集\数据集\tianchi_part_image\blouse'+'\\'+name)
#         new_label=np.asarray([float(x) for x in label]).reshape(-1,2)
#         plt.plot(new_label[:,0],new_label[:,-1],'r*')
#
#         plt.imshow(img)
#         plt.show()




