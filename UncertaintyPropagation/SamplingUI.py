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
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Argument", pos=wx.DefaultPosition,
                           size=wx.Size(230, 242), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"mu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        # 参数1
        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"sigma", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        # 参数2
        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"长度", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        bSizer1.Add(self.m_staticText5, 0, wx.ALL, 5)

        # 参数3
        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button1.Bind(wx.EVT_BUTTON, self.getArgs)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def getArgs(self, event):
        arg1 = float(self.m_textCtrl1.GetValue())
        arg2 = float(self.m_textCtrl2.GetValue())
        arg3 = int(self.m_textCtrl3.GetValue())

        mu = arg1  # mean and standard deviation
        sigma = arg2
        type = SamplingMethod.normal
        size = arg3
        parm = mu, sigma
        s = Context(RandomSampling()).GetResult(size, type, *parm)
        oursql.clear_sampling_result()
        oursql.insert_sampling_result(s)
        count, bins, ignored = plt.hist(s, 30, normed=True)
        plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth=2,
                 color='r')
        plt.show()
        return arg1, arg2, arg3
