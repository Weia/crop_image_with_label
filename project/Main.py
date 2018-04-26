# -*- coding: utf-8 -*-
# @Time    : 2018/4/25 10:29
# @Author  : weic
# @FileName: Main.py
# @Software: PyCharm
import crop_image
#根据label截取图片，label文件支持两种，自己标记的label和天池数据集中的csv文件
"""
自己的图像
裁取五部分
1、头、颈 3个点 012
2、肩、胸、腰 6个点 345678
3、左肩、臂、肘、腕 4个点 3  13 9 11
4、右   4个点  4 14 10 12
5、脚  1个点 15

输入，一张图片，要截取的点的位置

"""

def myself_picture():
    img_dir = r'D:\数据集\数据集\邹博士量体照片\front'
    label_file = './label_files/mirror_zero_label.txt'
    posi_to_path = [
        [[0, 1, 2], 'head'],
        [[3, 4, 5, 6, 7, 8], 'body'],
        [[3, 9, 11, 13], 'left-arm'],
        [[4, 10, 12, 14], 'right-arm'],
        [[15], 'foot']]

    root_path = r'D:\数据集\数据集\parts-images'
    for posi, category in posi_to_path:
        save_path = root_path + '\\' + category
        crop_image.crop_image_use_label(img_dir, label_file, posi, save_path)

"""
blouse posi 2,3,5,6 肩、胸  
outwear 2,3,4,5,6,7 肩、胸、腰 
dress 2,3,5,6,7,8 肩、胸、腰
都加2
"""

def tianchi_picture():
    img_dir=r'D:\数据集\数据集\天池数据集\[update] warm_up_train_20180222\train'
    label_root_path='./label_files'
    posi_to_label=[
        [[5, 6, 7, 8], 'blouse'],
        [[4, 5, 6, 7, 8, 9], 'outwear'],
        [[5,6, 7, 8,9, 10], 'dress']

    ]
    save_root_path=r'D:\数据集\数据集\tianchi_part_image'
    for posi,label_file in posi_to_label:
        label_file_path=label_root_path+'/'+label_file+'.csv'
        save_image_path=save_root_path+'\\'+label_file
        crop_image.crop_tianchi_images(label_file_path,posi,save_image_path,img_dir)




if __name__ == '__main__':
    tianchi_picture()



