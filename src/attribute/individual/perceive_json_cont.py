import json
import chardet


def gain_json_outcome(file_path)->dict:
    # 检测文件编码
    with open(file_path, "rb") as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
        encoding = result["encoding"]
        print("encoding ", encoding)

    # 根据编码打开文件并读取内容
    with open(file_path, "r", encoding=encoding, errors="ignore") as file:
        clean_content = file.read()
        print("\nclean_content: ", clean_content)

        data = json.loads(clean_content)
        print("\ngain_json_outcome: ", data)

    return data
