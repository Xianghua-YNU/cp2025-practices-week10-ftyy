import numpy as np
import matplotlib.pyplot as plt

def q3a(T):
    """
    计算 3-alpha 反应速率中与温度相关的部分 q / (rho^2 Y^3)
    输入: T - 温度 (K)
    返回: 速率因子 (erg * cm^6 / (g^3 * s))
    """
    # TODO: 在此实现3-α反应速率计算
    # 提示：
    # 1. 将温度转换为以 10^8 K 为单位
    # 2. 注意处理温度为零的特殊情况
    # 3. 使用公式：q_{3α} = 5.09×10^11 ρ^2 Y^3 T_8^(-3) exp(-44.027/T_8)
    if T <= 0:
        return 0  # 温度为零或负值时速率为零
    T_8 = T / 1.0e8  # 转换为以 10^8 K 为单位的温度
    return 5.09e11 * T_8**-3 * np.exp(-44.027 / T_8)
    pass

def plot_rate(filename="rate_vs_temp.png"):
    """绘制速率因子随温度变化的 log-log 图"""
    # TODO: 在此实现绘图函数
    # 提示：
    # 1. 使用 np.logspace 生成温度数据点
    # 2. 计算对应的速率值
    # 3. 使用 plt.loglog 绘制双对数图
    # 4. 添加适当的标签和标题
    temperatures = np.logspace(7, 10, 500)  # 从 10^7 到 10^10 K 的温度范围
    rates = [q3a(T) for T in temperatures]

    plt.figure(figsize=(8, 6))
    plt.loglog(temperatures, rates, label=r"$q_{3\alpha} / (\rho^2 Y^3)$")
    plt.xlabel("Temperature $T$ (K)")
    plt.ylabel("Rate Factor (erg cm$^6$ / g$^3$ s)")
    plt.title("3-alpha Reaction Rate vs Temperature")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig(filename)
    plt.show()
    pass

if __name__ == "__main__":
    # 计算并打印 nu 值
    print("   温度 T (K)    :   ν (敏感性指数)")
    print("--------------------------------------")

    temperatures_K = [1.0e8, 2.5e8, 5.0e8, 1.0e9, 2.5e9, 5.0e9]
    h = 1.0e-8  # 扰动因子

    for T0 in temperatures_K:
        q_T0 = q3a(T0)
        q_T0_h = q3a(T0 * (1 + h))  # 计算 T0 + h*T0 的速率
        if q_T0 > 0:
            dq_dT = (q_T0_h - q_T0) / (h * T0)  # 数值微分
            nu = (T0 / q_T0) * dq_dT  # 计算敏感性指数
        else:
            nu = 0  # 如果 q 为零，敏感性指数定义为零
        print(f"{T0:>12.2e} : {nu:>10.4f}")

    plot_rate()

    # TODO: 实现温度敏感性指数的计算
    # 提示：
    # 1. 对每个温度点计算 q3a
    # 2. 使用前向差分计算导数
    # 3. 计算敏感性指数 nu
    # 4. 注意处理特殊情况（如 q = 0）

    # TODO: 调用绘图函数展示结果
