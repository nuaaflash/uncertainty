# -*- coding: utf-8 -*-

import wx
import wx.xrc
import wx.aui
# TODO 修改为你的path
from sys import path

path.append('..')
from SamplingMethod import *


###########################################################################
# Class SamplingDialog
###########################################################################


class SamplingDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"样本生成参数设置", pos=wx.DefaultPosition,
                           size=wx.Size(509, 309), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        ''' AuiNoteBook 标签页 begins '''
        self.m_auinotebook1 = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.aui.AUI_NB_DEFAULT_STYLE)
        ''' 正态分布 begins '''
        self.m_panel_normal = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText_normal_mu = wx.StaticText(self.m_panel_normal, wx.ID_ANY, u"Mu", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText_normal_mu.Wrap(-1)
        fgSizer2.Add(self.m_staticText_normal_mu, 0, wx.ALL, 5)

        self.m_textCtrl_normal_mu = wx.TextCtrl(self.m_panel_normal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        fgSizer2.Add(self.m_textCtrl_normal_mu, 0, wx.ALL, 5)

        self.m_staticText_normal_sigma = wx.StaticText(self.m_panel_normal, wx.ID_ANY, u"Sigma", wx.DefaultPosition,
                                                       wx.DefaultSize, 0)
        self.m_staticText_normal_sigma.Wrap(-1)
        fgSizer2.Add(self.m_staticText_normal_sigma, 0, wx.ALL, 5)

        self.m_textCtrl_normal_sigma = wx.TextCtrl(self.m_panel_normal, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        fgSizer2.Add(self.m_textCtrl_normal_sigma, 0, wx.ALL, 5)

        self.m_panel_normal.SetSizer(fgSizer2)
        self.m_panel_normal.Layout()
        fgSizer2.Fit(self.m_panel_normal)
        self.m_auinotebook1.AddPage(self.m_panel_normal, u"正态分布", True, wx.NullBitmap)
        ''' 正态分布 ends '''

        ''' 均匀分布 begins '''
        self.m_panel_uniform = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        fgSizer3 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText_uniform_low = wx.StaticText(self.m_panel_uniform, wx.ID_ANY, u"下界", wx.DefaultPosition,
                                                      wx.DefaultSize, 0)
        self.m_staticText_uniform_low.Wrap(-1)
        fgSizer3.Add(self.m_staticText_uniform_low, 0, wx.ALL, 5)

        self.m_textCtrl_uniform_low = wx.TextCtrl(self.m_panel_uniform, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                  wx.DefaultSize, 0)
        fgSizer3.Add(self.m_textCtrl_uniform_low, 0, wx.ALL, 5)

        self.m_staticText_uniform_high = wx.StaticText(self.m_panel_uniform, wx.ID_ANY, u"上界", wx.DefaultPosition,
                                                       wx.DefaultSize, 0)
        self.m_staticText_uniform_high.Wrap(-1)
        fgSizer3.Add(self.m_staticText_uniform_high, 0, wx.ALL, 5)

        self.m_textCtrl_uniform_high = wx.TextCtrl(self.m_panel_uniform, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                   wx.DefaultSize, 0)
        fgSizer3.Add(self.m_textCtrl_uniform_high, 0, wx.ALL, 5)

        self.m_panel_uniform.SetSizer(fgSizer3)
        self.m_panel_uniform.Layout()
        fgSizer3.Fit(self.m_panel_uniform)
        self.m_auinotebook1.AddPage(self.m_panel_uniform, u"均匀分布", False, wx.NullBitmap)
        ''' 均匀分布 ends '''

        ''' 指数分布 begins '''
        self.m_panel_exponential = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TAB_TRAVERSAL)
        fgSizer4 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText_exponential_theta = wx.StaticText(self.m_panel_exponential, wx.ID_ANY, u"theta",
                                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_exponential_theta.Wrap(-1)
        fgSizer4.Add(self.m_staticText_exponential_theta, 0, wx.ALL, 5)

        self.m_textCtrl_exponential_theta = wx.TextCtrl(self.m_panel_exponential, wx.ID_ANY, wx.EmptyString,
                                                        wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer4.Add(self.m_textCtrl_exponential_theta, 0, wx.ALL, 5)

        self.m_panel_exponential.SetSizer(fgSizer4)
        self.m_panel_exponential.Layout()
        fgSizer4.Fit(self.m_panel_exponential)
        self.m_auinotebook1.AddPage(self.m_panel_exponential, u"指数分布", False, wx.NullBitmap)
        ''' 指数分布 ends '''

        ''' 其他分布 begins '''
        self.m_panel_other = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        fgSizer41 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer41.SetFlexibleDirection(wx.BOTH)
        fgSizer41.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText_other_expression = wx.StaticText(self.m_panel_other, wx.ID_ANY, u"expression",
                                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_other_expression.Wrap(-1)
        fgSizer41.Add(self.m_staticText_other_expression, 0, wx.ALL, 5)

        self.m_textCtrl_other_expression = wx.TextCtrl(self.m_panel_other, wx.ID_ANY, wx.EmptyString,
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer41.Add(self.m_textCtrl_other_expression, 0, wx.ALL, 5)

        self.m_staticText_other_low = wx.StaticText(self.m_panel_other, wx.ID_ANY, u"low", wx.DefaultPosition,
                                                    wx.DefaultSize, 0)
        self.m_staticText_other_low.Wrap(-1)
        fgSizer41.Add(self.m_staticText_other_low, 0, wx.ALL, 5)

        self.m_textCtrl_other_low = wx.TextCtrl(self.m_panel_other, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        fgSizer41.Add(self.m_textCtrl_other_low, 0, wx.ALL, 5)

        self.m_staticText_other_high = wx.StaticText(self.m_panel_other, wx.ID_ANY, u"high", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.m_staticText_other_high.Wrap(-1)
        fgSizer41.Add(self.m_staticText_other_high, 0, wx.ALL, 5)

        self.m_textCtrl_other_high = wx.TextCtrl(self.m_panel_other, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        fgSizer41.Add(self.m_textCtrl_other_high, 0, wx.ALL, 5)

        self.m_panel_other.SetSizer(fgSizer41)
        self.m_panel_other.Layout()
        fgSizer41.Fit(self.m_panel_other)
        self.m_auinotebook1.AddPage(self.m_panel_other, u"其他分布", False, wx.NullBitmap)
        ''' 其他分布 ends '''

        bSizer1.Add(self.m_auinotebook1, 1, wx.EXPAND | wx.ALL, 5)
        ''' AuiNoteBook 标签页 ends '''

        ''' 样本容量 begins '''
        self.m_staticText_sampling_size = wx.StaticText(self, wx.ID_ANY, u"样本容量", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText_sampling_size.Wrap(-1)
        bSizer1.Add(self.m_staticText_sampling_size, 0, wx.ALL, 5)

        self.m_textCtrl_sampling_size = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                    0)
        bSizer1.Add(self.m_textCtrl_sampling_size, 0, wx.ALL, 5)
        ''' 样本容量 ends '''

        ''' 确定按钮 begins '''
        self.m_buttom_ok = wx.Button(self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_buttom_ok, 0, wx.ALL, 5)
        self.m_buttom_ok.Bind(wx.EVT_BUTTON, self.getArgs)
        ''' 确定按钮 ends '''

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def getArgs(self, event):
        ''' 调用函数将样本写入数据库 '''
        ''' 获取参数（暂不转换成数字） '''
        mu = self.m_textCtrl_normal_mu.GetValue()
        sigma = self.m_textCtrl_normal_sigma.GetValue()
        uniform_low = self.m_textCtrl_uniform_low.GetValue()
        uniform_high = self.m_textCtrl_uniform_high.GetValue()
        theta = self.m_textCtrl_exponential_theta.GetValue()
        expr = self.m_textCtrl_other_expression.GetValue()
        other_low = self.m_textCtrl_other_low.GetValue()
        other_high = self.m_textCtrl_other_high.GetValue()

        size = int(self.m_textCtrl_sampling_size.GetValue())    # 样本容量
        type = SamplingMethod.other     # 分布类型
        parm = 0.0, 0.0     # 参数
        strtgy = 0          # 策略编号

        if mu and sigma:
            print 'Client chose normal'
            type = SamplingMethod.normal
            parm = float(mu), float(sigma)
            strtgy = 1
        elif uniform_low and uniform_high:
            print 'Client chose uniform'
            type = SamplingMethod.uniform
            parm = float(uniform_low), float(uniform_high)
            strtgy = 1
        elif theta:
            print 'Client chose exponential'
            type = SamplingMethod.exponential
            parm = float(theta), 0.0
            strtgy = 1
        elif expr and other_low and other_high:
            print 'Client chose other'
            type = SamplingMethod.other
            parm = expr, float(other_low), float(other_high)
            strtgy = 3
        else:
            print 'Client did not choose anything!'

        s = strategy[strtgy].GetResult(size, type, *parm)
        oursql.clear_sampling_result()
        oursql.insert_sampling_result(s,"normal","random")
        count, bins, ignored = plt.hist(s, 30, normed=True)
        # plt.plot(bins, 4 * bins **3, linewidth=2,
        #         color='r')
        plt.show()
