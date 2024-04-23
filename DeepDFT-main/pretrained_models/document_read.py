import subprocess
import lz4
import os

# 定义模型路径和XYZ文件所在的目录
model_dir = "/root/autodl-tmp/DeepDFT-main/pretrained_models/qm9_schnet"
xyz_dir = "/root/autodl-tmp/s2ef_train_200K/s2ef_train_200K"
output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)

# 循环遍历所有XYZ文件
for i in range(37):  # 从0到36
    xyz_file = f"{xyz_dir}/{i}.xyz"
    output_dir_i = f'results/{i}'
    os.makedirs(output_dir_i, exist_ok=True)
    # 构建命令行命令，包括输出目录指定
    command = ["python", "predict_with_model.py", model_dir, xyz_file, "--output_dir", output_dir_i]

    # 调用subprocess运行命令
    result = subprocess.run(command, capture_output=True, text=True)

    # 打印输出结果（可选）
    print(f"Running prediction for {i}.xyz")
    print("Output:", result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)