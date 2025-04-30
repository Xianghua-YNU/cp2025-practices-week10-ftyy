import numpy as np

# 待积分函数（学生需自行定义）
def f(x):
    # 实现被积函数 f(x) = x^4 - 2x + 1
    return x**4 - 2*x + 1

# 定义积分区间和子区间数
a, b = 0, 2  # 积分区间
N = 100  # 子区间数（必须为偶数）


# 梯形法则积分函数（供参考比较用）
def trapezoidal(f, a, b, N):
    """
    梯形法数值积分
    :param f: 被积函数
    :param a: 积分下限
    :param b: 积分上限  
    :param N: 子区间数
    :return: 积分近似值
    """
    # 检查N是否为偶数
    if N % 2 != 0:
        raise ValueError("N must be an even number.")
    h = (b - a) / N  # 步长
    x = np.linspace(a, b, N + 1)  # 子区间节点
    y = f(x)  # 函数值
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:N]) + y[N])  # 梯形法则公式
    return integral


# Simpson法则积分函数（学生需完成）
def simpson(f, a, b, N):
    """
    Simpson法数值积分
    :param f: 被积函数
    :param a: 积分下限
    :param b: 积分上限
    :param N: 子区间数（必须为偶数）
    :return: 积分近似值
    """
    # 检查N是否为偶数
    if N % 2 != 0:
        raise ValueError("N must be an even number.")
    # 奇数索引（1,3,5,...,N-1）
    odd_sum = np.sum(y[1:N:2])
    # 偶数索引（2,4,6,...,N-2）
    even_sum = np.sum(y[2:N:2])
    h = (b - a) / N  # 步长
    x = np.linspace(a, b, N + 1)  # 子区间节点
    y = f(x)  # 函数值
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:N:2]) + 2 * np.sum(y[2:N-1:2]) + y[N])  # Simpson法则公式
    return integral
    

def main():
    a, b = 0, 2  # 积分区间
    exact_integral = 4.4  # 精确解

    for N in [100, 1000]:  # 不同子区间数
        # 调用积分函数并计算结果
        trapezoidal_result = trapezoidal(f, a, b, N)
        simpson_result = simpson(f, a, b, N)
        
        # 计算相对误差
        trapezoidal_error = abs(trapezoidal_result - exact_integral) / exact_integral
        simpson_error = abs(simpson_result - exact_integral) / exact_integral

        # 输出结果（模板已给出）
        print(f"N = {N}")
        print(f"梯形法则结果: {trapezoidal_result:.8f}, 相对误差: {trapezoidal_error:.2e}")
        print(f"Simpson法则结果: {simpson_result:.8f}, 相对误差: {simpson_error:.2e}")
        print("-" * 40)

if __name__ == '__main__':
    main()
