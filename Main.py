import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory) and ((".DS_Store" not in directory) and ("Main" not in directory))]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2

#processes directories recursively and returns cat_list and dog_list with full paths to cat and dog pictures (respectively)
def process_dir(path, cat_list, dog_list):

    dir_list, file_list = get_dirs_and_files(path)

    #tests
    print("dir_list")
    print(dir_list)
    print("file_list")
    print(file_list , "\n")

    #base case
    if not dir_list: #if there are no more folders
        for file in file_list: #classify each image in current folder
            prob = classify_pic(path + '/' + file) #probability image is of dog
            if prob >= 0.5:
                dog_list.append(path + '/' + file)
            else:
                cat_list.append(path + '/' + file)
        return cat_list, dog_list

    #classifies each image using the function classify_pic
    for file in file_list: 
        if classify_pic(path + '/' + file) >= 0.5:
            dog_list.append(path + '/' + file)
        else:
            cat_list.append(path + '/' + file)

    #recursive call for each directory
    for dir in dir_list:
        process_dir(path + '/' + dir, cat_list, dog_list)

    return cat_list, dog_list


def main():
    start_path = '.' # current directory

    cat_list = []
    dog_list = []

    process_dir(start_path, cat_list, dog_list)
    
    #tests
    print(cat_list, "\n")
    print(dog_list)


main()

