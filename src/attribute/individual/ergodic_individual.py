import os


def gain_file_set(folder_path):
    # 初始化集合
    files = set()

    # 遍历文件夹路径中的所有目录
    for dir_name in os.listdir(folder_path):
        dir_path = os.path.join(folder_path, dir_name)

        # 如果不是目录，则加入集合
        if os.path.isfile(dir_path):
            files.add(dir_path)

    print("\ngain_file_set:", files)
    return files
