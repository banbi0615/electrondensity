import pandas as pd
import os
import shutil
import random

# 设置文件路径
csv_path = "E:\\qmof_databaseALL\\qmof.csv"
chgcar_source_dir = "E:\\QMOF\\QMOF_gz"
xyz_target_dir = "E:\\QMOFmedium\\xyz"
chgcar_target_dir = "E:\\QMOFmedium\\chgcar_lz4"

# 读取CSV文件
df = pd.read_csv(csv_path)

# 获取XYZ源目录中所有文件
xyz_files = os.listdir(xyz_target_dir)
xyz_files = set(xyz_files)  # 为了快速查找，转换成集合

# 准备列表，用于存储有有效CHGCAR.gz文件的XYZ文件
valid_files = []

# 遍历DataFrame，查找每个cif文件对应的CHGCAR.gz文件是否存在
for index, row in df.iterrows():
    cif_base = row['qmof_id']
    chgcar_base = row['name']
    xyz_file = cif_base + '.xyz'
    chgcar_file = chgcar_base + '_CHGCAR.gz'

    # 检查xyz文件是否存在以及对应的CHGCAR.gz文件是否存在
    if xyz_file in xyz_files and os.path.exists(os.path.join(chgcar_source_dir, chgcar_file)):
        valid_files.append(chgcar_file)



    selected_files = valid_files


# 检查并创建目标目录
if not os.path.exists(chgcar_target_dir):
    os.makedirs(chgcar_target_dir)

# 复制文件
for chgcar_file in selected_files:

    shutil.copy2(os.path.join(chgcar_source_dir, chgcar_file), os.path.join(chgcar_target_dir, chgcar_file))

print("文件复制完成。共复制了 {} 组文件。".format(len(selected_files)))
