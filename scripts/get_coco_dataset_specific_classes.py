import os
import json
from os import listdir, getcwd
from os.path import join

classes = ["person","bicycle","car","motorcycle","bus"]

#box form[x,y,w,h]
def convert(size,box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = box[0]*dw
    y = box[1]*dh
    w = box[2]*dw
    h = box[3]*dh
    return (x,y,w,h)

def convert_annotation(file_path):
    with open('/media/yehao/ye/coco/annotations/instances_val2014.json','r') as f:
        data = json.load(f)
    for item in data['images']:
        image_id = item['id']
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
        outfile = open('/media/yehao/ye/coco/labellabel/%s.txt'%(file_name[:-4]), 'a+')
        for item2 in value:
            category_id = item2['category_id']
            value1 = filter(lambda item3: item3['id'] == category_id,data['categories'])
            name = value1[0]['name']
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width,height),box)
            outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        outfile.close()
			
if __name__ == '__main__':
    convert_annotation()