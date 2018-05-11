# -*- coding: utf-8 -*-
from functools import wraps

import wx
from wx import aui
import UPShowPanel
import UPSelectMethodPanel

""""装饰器实现单例模式 方便传参"""
def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance

@singleton
class UTNotebook(aui.AuiNotebook):

    def __init__(self, parent=None):

        aui.AuiNotebook.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition,
                                 wx.DefaultSize, aui.AUI_NB_DEFAULT_STYLE)

    def up_show(self):
        """ 在NoteBook里添加页面“试验设计” """
        self.show_panel = UPShowPanel.ShowPanel(self)
        self.AddPage(self.show_panel, u"试验设计", True, wx.NullBitmap)

    def ShowArg(self, record):

        self.show_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,
                                   wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.AddPage(self.show_panel, u"显示参数信息", True, wx.NullBitmap)
        show_panel = self.show_panel
        # show_panel 的布局，只有 scrollPanel 一个元素
        show_panel.bSizer = wx.BoxSizer(wx.VERTICAL)
        # 为实现滚动条加入 scrollPanel
        show_panel.scrolledWindow = wx.ScrolledWindow(show_panel, wx.ID_ANY,
                                                      wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        show_panel.scrolledWindow.SetScrollRate(5, 5)
        scrollPanel = show_panel.scrolledWindow
        # scrollPanel 的布局，元素为显示的控件
        show_panel.gbSizer = wx.GridBagSizer(5, 5)
        show_panel.gbSizer.SetFlexibleDirection(wx.BOTH)
        show_panel.gbSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)



        """"""

        show_panel.m_grid4 = wx.grid.Grid(show_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        # 利用record的大小动态建立表长度
        show_panel.m_grid4.CreateGrid(len(record), 4)
        show_panel.m_grid4.EnableEditing(True)
        show_panel.m_grid4.EnableGridLines(True)
        show_panel.m_grid4.EnableDragGridSize(False)
        show_panel.m_grid4.SetMargins(0, 0)

        # Columns
        show_panel.m_grid4.EnableDragColMove(False)
        show_panel.m_grid4.EnableDragColSize(True)
        show_panel.m_grid4.SetColLabelSize(30)
        show_panel.m_grid4.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        show_panel.m_grid4.SetColLabelValue(0, "模型名称")
        show_panel.m_grid4.SetColLabelValue(1, "参数名称")
        show_panel.m_grid4.SetColLabelValue(2, "分布类型")
        show_panel.m_grid4.SetColLabelValue(3, "分布参数")

        # Rows
        show_panel.m_grid4.EnableDragRowSize(True)
        show_panel.m_grid4.SetRowLabelSize(80)
        show_panel.m_grid4.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        show_panel.m_grid4.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

        """"设置内容"""
        i = 0
        for row in record:
            show_panel.m_grid4.SetCellValue(i, 0, str(row[0]))
            show_panel.m_grid4.SetCellValue(i, 1, str(row[1]))
            show_panel.m_grid4.SetCellValue(i, 2, str(row[2]))
            show_panel.m_grid4.SetCellValue(i, 3, str(row[3]))
            i = i + 1

        """"""

        show_panel.bSizer.Add(show_panel.m_grid4, 1, wx.ALL | wx.EXPAND, 5)

        scrollPanel.SetSizer(show_panel.gbSizer)
        scrollPanel.Layout()
        show_panel.bSizer.Add(scrollPanel, 1, wx.EXPAND | wx.ALL, 5)
        show_panel.SetSizer(show_panel.bSizer)
        show_panel.Layout()

    def up_select_method(self):
        """ 选择抽样方法 """
        print(self.kind)
        print(self.para)
        self.select_method_panel = UPSelectMethodPanel.SelectSamplingMethodPanel(self)  # 在这里传入参数
        self.select_method_panel.set_kind_and_para_and_name(self.kind,self.name,self.para)
        self.AddPage(self.select_method_panel, u"抽样方法", True, wx.NullBitmap)

    def up_test_plan(self):
        """ 实验方案生成展示 """
        print(self.name[0])
        self.plan_panel = UPShowPanel.ShowPlanPanel(self,name=self.name)
        # self.plan_panel.set_name(self.name)
        self.AddPage(self.plan_panel, u"实验方案", True, wx.NullBitmap)