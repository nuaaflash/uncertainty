# -*- coding: utf-8 -*
from __future__ import division
import numpy
def cal_avg_vi(Esi):
    ans = numpy.mean(Esi, axis=0)
    return ans.T


def cal_cov_mat(Esi):
    # print 'Esi:'
    # print Esi
    avg_vi = cal_avg_vi(Esi)
    # print '均向量'
    # print avg_vi
    shape_v = Esi.shape
    m = shape_v[0]
    em = numpy.mat(numpy.full((m, 1), 1))
    print m
    print 1/(m-1)
    ret_mat = 1 / (m - 1) * (Esi - em * avg_vi.T).T * (Esi - em * avg_vi.T)
    # print '协方差矩阵:'
    # print ret_mat
    return ret_mat


def Mahalanobis_1(Esi, Er_k, avg_vi, cov_mat):
    ret = (Er_k - avg_vi).T * cov_mat.I * (Er_k - avg_vi)
    return ret


def Mahalanobis_2(Esi, Er):
    avg_vi = cal_avg_vi(Esi)
    cov_mat = cal_cov_mat(Esi)
    shape_v = Er.shape
    di = 0
    for i in range(shape_v[0]):
        Er_k = Er[i].T
        di_k = Mahalanobis_1(Esi, Er_k, avg_vi, cov_mat)
        di = di + di_k
    return numpy.sqrt(di)