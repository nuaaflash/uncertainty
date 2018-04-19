# coding=utf-8
# from http://www.doc88.com/p-215945997508.html

import numpy as np
import matplotlib.pyplot as plt

# :param x_low: 样本的下界
# :param x_high: 样本的上界
# :param y_max: 样本概率密度函数在[x_low, x_high]上的最大值
# :param expression: 样本的概率密度函数
# :param size: 样本大小
# :return: 样本数据


def interpret(expression, x):
	y = eval(expression)
	return y


def getSample(x_low, x_high, y_max, expression, size):
	result = np.empty([size])
	while size > 0:
		temp1 = np.random.uniform(x_low, x_high, 1)
		temp2 = np.random.uniform(0, y_max, 1)
		if temp2 < interpret(expression, temp1):
			result[size-1] = temp1
			size -= 1
	return result


if __name__ == '__main__':
	expr = '4 * x ** 3'
	low = 0.0
	high = 1.0
	size = 1000
	max = 3.0
	s = getSample(low, high, max, expr, size)
	count, bins, ignored = plt.hist(s, 30, normed=True)
	plt.plot(bins, 3 * bins ** 2, linewidth=2, color='r')
	plt.show()
