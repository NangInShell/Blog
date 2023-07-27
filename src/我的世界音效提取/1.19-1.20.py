import os
import json
import shutil

# 定义输入文件和输出文件夹
input_json_file = r"D:\minecraft1.19\.minecraft\assets\indexes\1.19.json"
output_folder = r"D:\minecraft1.19\.minecraft\assets\indexes\output_folder"

# 读取JSON文件
with open(input_json_file, "r") as f:
    data = json.load(f)

# 遍历每个哈希值和文件信息
for key, value in data["objects"].items():
    if ".ogg" in key:
        print(key, value)

        # 获取文件的哈希值
        hash_value = value["hash"]
        # 获取哈希值前两位和剩余的部分
        hash_folder = hash_value[:2]
        # 获取文件的路径
        file_path = os.path.join(r"D:\minecraft1.19\.minecraft\assets\objects", hash_folder, hash_value)
        print(file_path)
        # 按照key的路径创建文件夹
        os.makedirs(os.path.join(output_folder, key.rsplit("/", 1)[0]), exist_ok=True)
        # 复制文件到对应文件夹并且修改文件名为key的文件名
        shutil.copy(file_path, os.path.join(output_folder, key))

print("文件复制完成！")
