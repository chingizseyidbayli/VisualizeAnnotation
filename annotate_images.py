import os
import cv2
import  xml.dom.minidom
import tqdm
import argparse
 

def annotate_images(image_path, annotation_path, output_path):
    files_name = os.listdir(image_path)
    for filename_ in tqdm.tqdm(files_name):
        filename, _ = os.path.splitext(filename_)
        img_path =os.path.join(image_path, filename+'.jpg')
        xml_path =os.path.join(annotation_path, filename+'.xml')
        img = cv2.imread(img_path)
        dom = xml.dom.minidom.parse(xml_path)
        root = dom.documentElement
        objects=dom.getElementsByTagName("object")
        i=0
        for object, i in enumerate(objects):
            bndbox = root.getElementsByTagName('bndbox')[i]
            xmin = bndbox.getElementsByTagName('xmin')[0]
            ymin = bndbox.getElementsByTagName('ymin')[0]
            xmax = bndbox.getElementsByTagName('xmax')[0]
            ymax = bndbox.getElementsByTagName('ymax')[0]
            xmin_data=xmin.childNodes[0].data
            ymin_data=ymin.childNodes[0].data
            xmax_data=xmax.childNodes[0].data
            ymax_data=ymax.childNodes[0].data
            print(object)        
            print(xmin_data)
            print(ymin_data)            
            cv2.rectangle(img,(int(xmin_data),int(ymin_data)),(int(xmax_data),int(ymax_data)),(55,255,155),5)
        cv2.imwrite(os.path.join(output_path, "{}.jpg".format(filename),img))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--annotation_files_path', type=str, required=True, help="Directory where annotation files are placed")
    ap.add_argument('--image_files_path', type=str, required=True, help="Directory where image files are placed")
    ap.add_argument('--output_path', type=str, required=True, help="Directory where annotated images will be placed")
    args = ap.parse_args()

    annotate_images(args.annotation_files_path, args.image_files_path, args.output_path)

	
