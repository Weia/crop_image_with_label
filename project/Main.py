# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:29
# @Author  : weic
# @FileName: Main.py
# @Software: PyCharm

"""
裁取五部分
1、头、颈 3个点 012
2、肩、胸、腰 6个点 345678
3、左肩、臂、肘、腕 4个点 3  13 9 11
4、右   4个点  4 14 10 12
5、脚  1个点 15

输入，一张图片，要截取的点的位置

"""
import crop_image

if __name__ == '__main__':
    img_dir=r'D:\数据集\数据集\邹博士量体照片\front'
    label_file='./label_files/mirror_zero_label.txt'
    posi_to_path=[

        [[4, 10, 12, 14], 'right-arm'],
        [[15], 'foot']]
    positions=[[0,1,2]]
    root_path=r'D:\数据集\数据集\parts-images'
    for posi,category in posi_to_path:
        save_path=root_path+'\\'+category
        crop_image.crop_image_use_label(img_dir,label_file,posi,save_path)


