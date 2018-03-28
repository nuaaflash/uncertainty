# -*- coding:utf-8 -*-
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter
import LHS
#抽样方法抽象类
class SamplingMethod(object):
    normal = 1
    uniform = 2
    def get_sampling(self, size, type, *parm):
        pass

#随机抽样方法子类
class RandomSampling(SamplingMethod):
    def get_sampling(self, size, type, *parm):
        if type == self.normal:
            return np.random.normal(parm[0],parm[1],size)

#拉丁超立方抽样方法子类
class LHSampling(SamplingMethod):
    def get_sampling(self, size, type, *parm):
        if type == self.uniform:
            print (parm[0])
            return LHS.getSample(parm[0], parm[1], size)


#具体策略类
class Context(object):

    def __init__(self,csuper):
        self.csuper = csuper

    def GetResult(self,size,type,*parm):
        return self.csuper.get_sampling(size, type, *parm)

if __name__ == '__main__':
    choose = 1

    while choose != 0:
        choose = input("1.正态分布的随机抽样\n2.均匀分布的LHS抽样\n(再次选择请关掉弹出的窗口)退出请按0:\n")

        strategy = {}
        strategy[1] = Context(RandomSampling())
        strategy[2] = Context(LHSampling())
        # test RS for normal
        if choose == 1:
            mu, sigma = 0, 0.1  # mean and standard deviation
            type = SamplingMethod.normal
            size = 1000
            s = strategy[1].GetResult(size, type, mu, sigma)
            count, bins, ignored = plt.hist(s, 30, normed=True)
            plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) *np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),linewidth = 2, color = 'r')
            plt.show()

        # test LHS for uniform
        if choose == 2:
            D = 2
            size = 30
            bounds = [[0, 90], [0, 90]]
            xs = (bounds[0][1] - bounds[0][0]) / size
            ys = (bounds[1][1] - bounds[1][0]) / size
            ax = plt.gca()
            plt.ylim(bounds[1][0] - ys, bounds[1][1] + ys)
            plt.xlim(bounds[0][0] - xs, bounds[0][1] + xs)
            plt.grid()
            ax.xaxis.set_major_locator(MultipleLocator(xs))
            ax.yaxis.set_major_locator(MultipleLocator(ys))
            type2 = SamplingMethod.uniform
            samples = strategy[2].GetResult(size, type2, D, bounds)
            XY = np.array(samples)
            X = XY[:, 0]
            Y = XY[:, 1]
            plt.scatter(X, Y)
            plt.show()
