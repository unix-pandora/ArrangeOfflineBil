import stash_material as stash

# 读取二进制文件的头部的指定范围内的字节内容
def get_bin_content(file_path):
    with open(file_path, "rb") as file:
        content = file.read(stash.header_scope_num)

        print("\nread_binary_content: ", content)
        return content