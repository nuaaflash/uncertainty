# -*- coding: utf-8 -*-

import wx
from wx import aui
from wx import grid
from wx import lib
from functools import wraps

import Sql

# """"装饰器实现单例模式 方便在NAV界面更新SHOW界面"""
# def singleton(cls):
#     instances = {}
#
#     @wraps(cls)
#     def getinstance(*args, **kw):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kw)
#         return instances[cls]
#
#     return getinstance
#
# @singleton
class ShowPanel(wx.Panel):

    def __init__(self, parent = None):

        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition,
                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))

        bSizer8 = wx.BoxSizer(wx.VERTICAL)
        """"""

        self.m_grid4 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid4.CreateGrid(5, 4)
        self.m_grid4.EnableEditing(True)
        self.m_grid4.EnableGridLines(True)
        self.m_grid4.EnableDragGridSize(False)
        self.m_grid4.SetMargins(0, 0)

        # Columns
        self.m_grid4.EnableDragColMove(False)
        self.m_grid4.EnableDragColSize(True)
        self.m_grid4.SetColLabelSize(30)
        self.m_grid4.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.m_grid4.SetColLabelValue(0, "模型名称")
        self.m_grid4.SetColLabelValue(1, "参数名称")
        self.m_grid4.SetColLabelValue(2, "分布类型")
        self.m_grid4.SetColLabelValue(3, "分布参数")

        # Rows
        self.m_grid4.EnableDragRowSize(True)
        self.m_grid4.SetRowLabelSize(80)
        self.m_grid4.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.m_grid4.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)


        """"""
        bSizer8.Add(self.m_grid4, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer8)
        self.Layout()
        bSizer8.Fit(self)

    def set_name(self,name):
        self.name = name