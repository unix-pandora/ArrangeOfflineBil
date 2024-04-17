import crux
import parameters
import os


def get_dir_list(folder_path):
    directories_list = list()

    # 遍历文件夹路径中的所有目录
    for dir_name in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir_name)

        # 如果是目录，则加入集合
        if os.path.isdir(dir_path):
            directories_list.append(dir_path)

    print("\nget_directories_list: ", directories_list)
    return directories_list


def afford_element_list(media_pattern_type):
    ele_list = list()
    dirs_list = get_dir_list(parameters.original_directory)

    for i in dirs_list:
        result_dict = crux.crux_reception(media_pattern_type, i)
        result = dict(result_dict)
        ele_list.append(result)

    print("\nassign_ele_list: ", ele_list)
    return ele_list
