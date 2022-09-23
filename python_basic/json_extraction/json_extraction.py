import json
import os
import glob
from pprint import pprint


def json_to_dictionary(path):
    """
    read Json from a  given directory

    Args:
    path: the given directory

    returns:
    the Json Object from the given directory
    """
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def get_image_list(path):
    """
    get image list from 
    """
    dir_list = os.listdir(path)
    return dir_list

def dic_to_json(dic, path):
    path = path + ""
    with open("/home/nsl50/Tanvir/python_basic/json_extraction/sample.json", "w", encoding="utf-8") as outfile:
        json.dump(dic, outfile, ensure_ascii=False, indent = 4)

def name_change(path):
    path = path + '/*.jpg'
    current_files = glob.glob(path)
    for i, filename in enumerate(current_files):
        x = filename.split(".jpg")
        os.rename(filename, x[0] + '_aug.jpg')

if __name__ == '__main__':
    json_of_all_image = json_to_dictionary('/home/nsl50/Tanvir/python_basic/json_extraction/merged_data.json')
    list_of_image_name = get_image_list('/home/nsl50/Tanvir/python_basic/json_extraction/Augmentated_Image')
    Augmented_dictionary = {}
    for i in json_of_all_image:
        if json_of_all_image[i]['filename'] in list_of_image_name:
            x = i.split('.jpg')
            y = json_of_all_image[i]["filename"].split('.jpg')
            json_of_all_image[i]["filename"] = y[0] + '_aug.jpg'
            Augmented_dictionary.update({ x[0] + "_aug.jpg" + x[1]: json_of_all_image[i]})
    dic_to_json(Augmented_dictionary)
    name_change('/home/nsl50/Tanvir/python_basic/json_extraction/Augmentated_Image')



