import os

def inject_to_file(content, text_path):
    # 如果content不是字符串类型，将其转换为字符串
    if not isinstance(content, str):
        content = str(content)

    # 检查文件是否存在，如果不存在则创建
    if not os.path.exists(text_path):
        open(text_path, "w").close()

    # 打开文件并追加内容
    with open(text_path, "w", encoding="utf-8") as file:
        file.write(content)



    