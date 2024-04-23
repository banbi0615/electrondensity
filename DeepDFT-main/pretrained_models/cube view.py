from ase.io import read

# 读取 .cube 文件
atoms = read('D://prediction.cube')

# 查看原子信息
print(atoms)


from ase.visualize import view

view(atoms)
from ase.io.cube import read_cube_data

# 读取电子密度数据
data, atoms = read_cube_data('D://prediction.cube')

# 例如，显示一个电子密度切面
import matplotlib.pyplot as plt
import numpy as np

# 选择一个沿 z 轴的切面
z_slice = data[:, :, data.shape[2] // 2]

plt.imshow(z_slice.T, cmap='inferno', origin='lower', extent=(0, max(atoms.cell.lengths()[:2]), 0, max(atoms.cell.lengths()[:2])))
plt.colorbar(label='Electron density')
plt.xlabel('x (Å)')
plt.ylabel('y (Å)')
plt.show()
