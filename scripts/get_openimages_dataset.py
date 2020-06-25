import csv
import os

#select classes you want to download at https://github.com/openimages/dataset/blob/master/dict.csv
CLASS_LIST = ( '/m/01g317', #person
                '/m/01bjv', #bus
                '/m/0k4j', #car
                '/m/04_sv', #motorcycle
                '/m/07r04' #truck
            )
img_name = "111111111111"
path_to_obj_folder = '../build/darknet/x64/data/obj/'

#download csv from https://storage.googleapis.com/openimages/web/download.html
with open('../oidv6-train-annotations-bbox.csv', newline='') as csvfile:
    bboxs = csv.reader(csvfile, delimiter=',', quotechar='|')
    for bbox in bboxs:
        if bbox[2] in CLASS_LIST:
            if img_name != bbox[0]:
                if not os.path.isfile(path_to_obj_folder+"%s.jpg"%bbox[0]):
                    os.system("gsutil cp gs://open-images-dataset/train/%s.jpg %s"%(bbox[0], path_to_obj_folder))
                    out_file = open(path_to_obj_folder+"%s.txt"%bbox[0], 'w')
                    img_name = bbox[0]
            if img_name == bbox[0]:
                out_file.write(str(CLASS_LIST.index(bbox[2])) + " " + str(float(bbox[4])+(float(bbox[5])-float(bbox[4]))/2) + " " + str(float(bbox[6])+(float(bbox[7])-float(bbox[6]))/2)+ " " + str(float(bbox[5])-float(bbox[4])) + " " + str(float(bbox[7])-float(bbox[6])) + '\n')
