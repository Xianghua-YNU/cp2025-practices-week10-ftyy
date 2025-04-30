import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt
import os

def main():
    try:
        # 1. 获取数据文件路径（使用相对路径）
        data_file = os.path.join(os.path.dirname(__file__), 'Velocities.txt')  # 假设数据文件名为data.txt

        # 2. 读取数据（使用numpy.loadtxt）
        data = np.loadtxt(data_file, delimiter='\t')  # 假设数据以逗号分隔
        t = data[:, 0]  # 时间列
        v = data[:, 1]  # 速度列

        # 3. 计算总距离（使用numpy.trapz）
        total_distance = np.trapz(v, t)
        print(f"总运行距离: {total_distance:.2f} 米")

        # 4. 计算累积距离（使用cumulative_trapezoid）
        distance = cumulative_trapezoid(v, t, initial=0)

        # 5. 绘制图表
        plt.figure(figsize=(10, 6))
        plt.plot(t, v, 'b-', label='Velocity (m/s)')
        plt.plot(t, distance, 'r--', label='Distance (m)')
        plt.title('Velocity and Distance vs Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s) / Distance (m)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("错误：找不到数据文件")
        print("请确保数据文件存在于正确路径")

if __name__ == '__main__':
    main()
