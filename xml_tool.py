import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET


def merge_multiple_files(folder_name):
    merged_file_name = 'merged_file.xml'
    files = os.listdir(folder_name)
    merged_file = ElementTree()
    merged_file_element = Element('merged_file')
    print(len(files))
    for i in range(len(files)):
        path_pattern = folder_name + '/' + files[i]
        single_file_tree = ET.parse(path_pattern)
        root = single_file_tree.getroot()
        merged_file_element.append(root)
    print(merged_file.getroot())
    merged_file._setroot(merged_file_element)
    merged_file.write(merged_file_name)
    print('Merged file was saved to: ' + merged_file_name)
    return merged_file


def get_values_from_nodename(nodename, element_tree=None, file=None):
    file_with_values_name = "values.txt"
    if(file != None):
        tree = ET.parse(file)
        root = tree.getroot()
    elif(element_tree != None):
        root = element_tree.getroot()
    values = []
    subelements = root.getchildren()
    for i in range(len(subelements)):
        subelement = subelements[i]
        look_for_values(subelement, nodename, values)
    file_with_values = open(file_with_values_name, 'w')
    for item in values:
        file_with_values.write("%s\n" % item)
    print("Values saved to: " + file_with_values_name)
    return values


def look_for_values(root, nodename, values_list):
    if root.tag != nodename:
        subelements = root.getchildren()
        for i in range(len(subelements)):
            subelement = subelements[i]
            look_for_values(subelement, nodename, values_list)
    elif root.tag == nodename:
        values_list.append(root.text)

foldername = input("Folder: ")
nodename = input("Node: ")
print(get_values_from_nodename(nodename=nodename, element_tree=merge_multiple_files(foldername)))
