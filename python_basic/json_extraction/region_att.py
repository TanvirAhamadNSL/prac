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


def dic_to_json(dic):
    with open("/home/nsl50/Tanvir/python_basic/json_extraction/sample1.json", "w", encoding="utf-8") as outfile:
        json.dump(dic, outfile, ensure_ascii=False, indent=4)


def name_change(path):
    path = path + '/*.jpg'
    current_files = glob.glob(path)
    for i, filename in enumerate(current_files):
        x = filename.split(".jpg")
        os.rename(filename, x[0] + '_aug.jpg')


if __name__ == '__main__':
    json_of_all_image = json_to_dictionary('/home/nsl50/Tanvir/python_basic/json_extraction/sample.json')
    list_of_image_name = get_image_list('/home/nsl50/Tanvir/python_basic/json_extraction/Augmentated_Image')
    no_of_region = 0
    no_of_shape = 0
    for i in json_of_all_image:
        a = len(json_of_all_image[i]["regions"])
        #print(a)
        for j in range(a):
            # print(json_of_all_image[i]["regions"][j])
            # print(type(json_of_all_image[i]["regions"][j]))
            if len(json_of_all_image[i]["regions"][j]["shape_attributes"]) != 0:
                no_of_shape += 1

            if len(json_of_all_image[i]["regions"][j]["region_attributes"]) == 0:
                json_of_all_image[i]["regions"][j]["region_attributes"].update({"table_line": "line"})
                #print(len(json_of_all_image[i]["regions"][j]["shape_attributes"]))
            if len(json_of_all_image[i]["regions"][j]["region_attributes"]) != 0: 
                no_of_region += 1
    print(no_of_region)
    print(no_of_shape)
    dic_to_json(json_of_all_image)
    # name_change('/home/nsl50/Tanvir/python_basic/json_extraction/Augmentated_Image')
