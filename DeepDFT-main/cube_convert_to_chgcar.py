import numpy as np
from ase.io import read, write
import os

cube_file_dir="D:\\results"
path_dir="D:\\chgcar_from_cube"
structure_file_dir="D:\\s2ef_train_200K\\s2ef_train_200K"


def get_cube_data(cube_file):
    with open(cube_file, 'r') as f:
        cube_data = f.readlines()

    natoms = int(cube_data[2].split()[0])

    N = np.zeros((3))
    dV = np.zeros((3, 3))

    for i in range(3, 6):
        line = cube_data[i].split()
        N[i - 3] = int(line[0])
        for j in range(1, 4):
            dV[i - 3][j - 1] = float(line[j])

    dV *= 0.529177  # Convert from Bohr to Angstroms
    V = np.array([N[i] * dV[i] for i in range(3)])

    density_data = []
    for i in range(6 + natoms, len(cube_data)):
        density_data.extend([float(part) for part in cube_data[i].split()])

    N = np.array(N, dtype=int)
    grid = np.zeros((N[0], N[1], N[2], 3))
    density = np.zeros((N[0], N[1], N[2]))
    for i in range(N[0]):
        for j in range(N[1]):
            for k in range(N[2]):
                grid[i, j, k] = i * dV[0] + j * dV[1] + k * dV[2]
                density[i, j, k] = density_data[i + j + k]

    return grid, density, V

def write_CHGCAR(path, structure_file, cube_file,i):
    pw_path = path + '\\pw.in'
    cube_path = path + '\\si_rho.cube'
    chgcar_path = os.path.join(path, f'CHGCAR_{i}')

    write('temp_POSCAR', read(structure_file), format='vasp')

    grid, density, V = get_cube_data(cube_file)
    Nx, Ny, Nz = grid.shape[0], grid.shape[1], grid.shape[2]
    density *= np.linalg.det(V)

    with open('temp_POSCAR', 'r') as f:
        poscar_lines = f.readlines()

    with open(chgcar_path, 'w') as f:
        for i in range(len(poscar_lines)):
            f.write(poscar_lines[i])

        f.write('\n')

        f.write('  %s  %s  %s' % (Nx, Ny, Nz))
        f.write('\n')
        count = 0
        for k in range(Nz):
            for j in range(Ny):
                for i in range(Nx):
                    f.write('    %s' % density[i, j, k])
                    count += 1
                    if count % 10 == 0:
                        f.write('\n')

        f.write('\n')
    os.system("rm temp_POSCAR")
    return
# for i in range(37):
cube_file = "C:\\Users\\babel\\Desktop\\molden.cube"
structure_file = "D:\\xtb_output\\000010\\dsgdb9nsd_000010.extxyz"
# path = os.path.join(path_dir, str(i))
# if not os.path.exists(path):
#     os.makedirs(path)
write_CHGCAR('C:\\Users\\babel\\Desktop', structure_file, cube_file, 10)