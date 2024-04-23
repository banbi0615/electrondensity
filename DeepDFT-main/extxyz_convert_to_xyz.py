import lzma
import os
from ase.io import read, write


data_dir = r'D:\s2ef_train_200K\s2ef_train_200K'
raw_data_dir = os.path.join(data_dir, 'raw')
processed_data_dir = os.path.join(data_dir, 'processed')
# 循环处理从0到36的文件
for i in range(37):  # 因为range是不包括结束值的，所以用37来包括编号36
    input_filename = os.path.join(data_dir, f'{i}.extxyz.xz')  # 压缩的输入文件名
    intermediate_filename = os.path.join(data_dir, f'{i}.extxyz')  # 解压后的文件名
    output_filename = os.path.join(data_dir, f'{i}.xyz')  # 最终的XYZ文件名

    # 解压.xz文件
    with lzma.open(input_filename, 'rb') as compressed_file:
        with open(intermediate_filename, 'wb') as decompressed_file:
            decompressed_file.write(compressed_file.read())

    # 读取解压后的extXYZ文件并转换为XYZ格式
    atoms = read(intermediate_filename)
    write(output_filename, atoms)

    # 可选: 删除中间的extXYZ文件以节省空间
    import os
    os.remove(intermediate_filename)
