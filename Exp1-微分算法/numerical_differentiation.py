import numpy as np
import matplotlib.pyplot as plt
from sympy import tanh, symbols, diff, lambdify

def f(x):
    """计算函数值 f(x) = 1 + 0.5*tanh(2x)
    
    参数：
        x: 标量或numpy数组，输入值
    
    返回：
        标量或numpy数组，函数值
    """
    # TODO: 实现函数 f(x) = 1 + 0.5*tanh(2x)
    return 1 + 0.5 * np.tanh(2 * x)

def get_analytical_derivative():
    """使用sympy获取解析导数函数
    
    返回：
        可调用函数，用于计算导数值
    """
    # TODO: 使用sympy计算解析导数并返回可调用的函数
    x = symbols('x')
    fx = 1 + 0.5 * tanh(2 * x)
    dfx = diff(fx, x)
    dfx_func = lambdify(x, dfx, 'numpy')
    return dfx_func

def calculate_central_difference(x, f):
    """使用中心差分法计算数值导数
    
    参数：
        x: numpy数组，要计算导数的点
        f: 可调用函数，要求导的函数
    
    返回：
        numpy数组，x[1:-1]处的导数值
    """
    # TODO: 实现中心差分法计算导数
    h = x[1] - x[0]
    return (f(x[2:]) - f(x[:-2])) / (2 * h)

def richardson_derivative_all_orders(x, f, h, max_order=3):
    """使用Richardson外推法计算不同阶数的导数值
    
    参数：
        x: 标量，要计算导数的点
        f: 可调用函数，要求导的函数
        h: 浮点数，初始步长
        max_order: 整数，最大外推阶数
    
    返回：
        列表，不同阶数计算的导数值
    """
    # TODO: 实现Richardson外推法计算不同阶数的导数值
    D = []
    for k in range(max_order):
        hk = h / (2 ** k)
        D.append((f(x + hk) - f(x - hk)) / (2 * hk))
    # Richardson extrapolation
    for m in range(1, max_order):
        for k in range(max_order - 1, m - 1, -1):
            D[k] = (4 ** m * D[k] - D[k - 1]) / (4 ** m - 1)
    return D

def create_comparison_plot(x, x_central, dy_central, dy_richardson, df_analytical):
    """创建对比图，展示导数计算结果和误差分析
    
    参数：
        x: numpy数组，所有x坐标点
        x_central: numpy数组，中心差分法使用的x坐标点
        dy_central: numpy数组，中心差分法计算的导数值
        dy_richardson: numpy数组，Richardson方法计算的导数值
        df_analytical: 可调用函数，解析导数函数
    """
    # 创建四个子图
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))

    # 1. 导数对比图
    ax1.plot(x, df_analytical(x), label='Analytical derivative', color='k')
    ax1.plot(x_central, dy_central, 'o', label='Central difference', markersize=3)
    ax1.plot(x_central, dy_richardson, 'x', label='Richardson extrapolation', markersize=3)
    ax1.set_title('Derivative Comparison')
    ax1.legend()
    ax1.set_xlabel('x')
    ax1.set_ylabel("f'(x)")

    # 2. 误差分析图（对数坐标）
    error_central = np.abs(dy_central - df_analytical(x_central))
    error_richardson = np.abs(dy_richardson - df_analytical(x_central))
    ax2.semilogy(x_central, error_central, label='Central diff error')
    ax2.semilogy(x_central, error_richardson, label='Richardson error')
    ax2.set_title('Error Analysis (log scale)')
    ax2.legend()
    ax2.set_xlabel('x')
    ax2.set_ylabel('Absolute error')

    # 3. Richardson外推不同阶数误差对比图（对数坐标）
    h = x[1] - x[0]
    x0 = 0.0
    df_true0 = df_analytical(x0)
    orders = 4
    errors = []
    for k in range(orders):
        Dk = richardson_derivative_all_orders(x0, f, h, max_order=k+1)[-1]
        errors.append(np.abs(Dk - df_true0))
    ax3.semilogy(range(1, orders+1), errors, 'o-')
    ax3.set_xlabel('Richardson order')
    ax3.set_ylabel('Error')
    ax3.set_title('Richardson Error by Order')

    # 4. 步长敏感性分析图（双对数坐标）
    hs = np.logspace(-5, -1, 20)
    err_central = []
    err_rich = []
    for h_ in hs:
        D_c = (f(x0 + h_) - f(x0 - h_)) / (2 * h_)
        D_r = richardson_derivative_all_orders(x0, f, h_, max_order=2)[-1]
        err_central.append(np.abs(D_c - df_true0))
        err_rich.append(np.abs(D_r - df_true0))
    ax4.loglog(hs, err_central, label='Central difference')
    ax4.loglog(hs, err_rich, label='Richardson extrapolation')
    ax4.set_xlabel('Step size h')
    ax4.set_ylabel('Error')
    ax4.set_title('Step Size Sensitivity')
    ax4.legend()

    plt.tight_layout()
    plt.show()

def main():
    """运行数值微分实验的主函数"""
    # TODO: 设置实验参数
    
    # TODO: 获取解析导数函数
    
    # TODO: 计算中心差分导数
    
    # TODO: 计算Richardson外推导数
    
    # TODO: 绘制结果对比图
    # 设置实验参数
    x = np.linspace(-2, 2, 201)
    h = x[1] - x[0]

    # 获取解析导数函数
    df_analytical = get_analytical_derivative()

    # 计算中心差分导数
    dy_central = calculate_central_difference(x, f)
    x_central = x[1:-1]

    # 计算Richardson外推导数（取max_order=2）
    dy_richardson = []
    for xi in x_central:
        dy_richardson.append(richardson_derivative_all_orders(xi, f, h, max_order=2)[-1])
    dy_richardson = np.array(dy_richardson)

    # 绘制结果对比图
    create_comparison_plot(x, x_central, dy_central, dy_richardson, df_analytical)

if __name__ == '__main__':
    main()
