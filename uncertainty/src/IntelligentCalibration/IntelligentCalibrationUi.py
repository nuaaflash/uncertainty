# -*- coding: utf-8 -*-

import wx
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import ICNavPanel
import ICShowPanel
#import import_file

"""智能校准分析Panel类"""
class IntelligentCalibrationPanel(wx.Panel):
    
    def __init__(self, parent = None):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition,wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.InitUI()
        
    def InitUI(self):
        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        tabSizer = wx.BoxSizer(wx.HORIZONTAL)

        """添加菜单按钮"""
        self.button1 = wx.Button(self.m_panel5, wx.ID_ANY, u"元模型管理", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        self.button1.SetBitmap(wx.Bitmap('icon/btn_show1.tga'))
        self.button1.Bind(wx.EVT_LEFT_DOWN, self.ClickModelManage)
        tabSizer.Add(self.button1, 0, wx.ALL, 5)
        self.button2 = wx.Button(self.m_panel5, wx.ID_ANY, u"智能模型管理", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        tabSizer.Add(self.button2, 0, wx.ALL, 5)
        self.button3 = wx.Button(self.m_panel5, wx.ID_ANY, u"校准准则", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        tabSizer.Add(self.button3, 0, wx.ALL, 5)
        self.button4 = wx.Button(self.m_panel5, wx.ID_ANY, u"智能优化校准", wx.DefaultPosition,
                                 wx.DefaultSize, 0)
        tabSizer.Add(self.button4, 0, wx.ALL, 5)

        self.m_panel5.SetSizer(tabSizer)
        self.m_panel5.Layout()
        tabSizer.Fit(self.m_panel5)
        bSizer.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel6 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.navPanel = ICNavPanel.NavPanel(self.m_panel6)
        bSizer4.Add(self.navPanel, 1, wx.EXPAND | wx.ALL, 5)

        self.showPanel = ICShowPanel.ShowPanel(self.m_panel6)
        bSizer4.Add(self.showPanel, 3, wx.EXPAND | wx.ALL, 5)

        self.m_panel6.SetSizer(bSizer4)
        self.m_panel6.Layout()
        bSizer4.Fit(self.m_panel6)
        bSizer.Add(self.m_panel6, 4, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer)
        self.Layout()
        bSizer.Fit(self)
        
        
    def ClickModelManage(self, event):
        print("11")
        