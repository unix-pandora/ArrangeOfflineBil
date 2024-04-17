import os
import re
import stash_material as stash

def filter_elements(file_set):
    filtered_list = list()
    m4s_pattern = stash.m4s_pattern

    for ele in file_set:
        extension = get_last_element(ele)
        print("extension:", extension)

        if re.search(m4s_pattern, extension):
            filtered_list.append(ele)
        elif extension == stash.video_info_ext:
            filtered_list.append(ele)         

    print("\nfiltered_list:", filtered_list)
    return filtered_list


def get_last_element(string):
    # 按地址分隔符进行截取，得到一个数组
    path_parts = os.path.split(string)
    # 数组中的最后一个元素
    return path_parts[1]
