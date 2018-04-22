#coding=utf-8
# #demo from http://blog.csdn.net/xiaosebi1111/article/details/48653675
import numpy as np
# #解决pycharm报错方法 https://www.linuxidc.com/Linux/2018-03/151117.htm
# import matplotlib as mpl
# mpl.use('TkAgg')
# from matplotlib.ticker import MultipleLocator, FuncFormatter
# #http://blog.csdn.net/luminganan/article/details/51322234 安装方法
# import matplotlib.pyplot as pl

# 暂时只能进行对均匀分布做LHS抽样
# :param D:参数个数
# :param bounds:参数对应范围（list）
# :param size:拉丁超立方层数
# :return:样本数据


def getSample(D, bounds, size):
    result = np.empty([size, D])
    temp = np.empty([size])
    d = 1.0 / size

    for i in range(D):
        for j in range(size):
            temp[j] = np.random.uniform(
                low=j * d, high=(j + 1) * d, size = 1)[0]

        np.random.shuffle(temp)

        for j in range(size):
            result[j, i] = temp[j]

    # 对样本数据进行拉伸
    b = np.array(bounds)
    lower_bounds = b[:,0]
    upper_bounds = b[:,1]
    if np.any(lower_bounds > upper_bounds):
        print '范围出错'
        return None

    #   sample * (upper_bound - lower_bound) + lower_bound
    np.add(np.multiply(result,
                       (upper_bounds - lower_bounds),
                       out=result),
           lower_bounds,
           out=result)
    return result
