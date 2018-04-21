# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid
import sys
sys.path.append("..")
sys.path.append("../MysqlManager")
import Oursql as oursql
import UncertaintyPropagation.SamplingUI as sui


###########################################################################
## Class PlatformForUncertainly
###########################################################################

class PlatformForUncertainly(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title= u"不确定性智能仿真模型校准平台", pos=wx.DefaultPosition,
                          size=wx.Size(1280, 720), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.icon = wx.Icon('img/timg (3).jpg', wx.BITMAP_TYPE_JPEG)
        self.SetIcon(self.icon)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        bSizerforwholeframe = wx.BoxSizer(wx.VERTICAL)

        self.m_panelfor = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerforwholepanel = wx.BoxSizer(wx.VERTICAL)

        self.statusBar = wx.Notebook(self.m_panelfor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel1forStatusbar = wx.Panel(self.statusBar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TAB_TRAVERSAL)
        bSizerforpanel1 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button3 = wx.Button(self.m_panel1forStatusbar, wx.ID_ANY, u"模型设置", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.m_button3.SetBitmap(wx.Bitmap('img/timg (3).jpg'))
        self.m_button3.Bind(wx.EVT_LEFT_DOWN, self.ClickModelManage)

        bSizerforpanel1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self.m_panel1forStatusbar, wx.ID_ANY, u"参数设置", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizerforpanel1.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self.m_panel1forStatusbar, wx.ID_ANY, u"数据导入", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizerforpanel1.Add(self.m_button8, 0, wx.ALL, 5)

        self.m_button9 = wx.Button(self.m_panel1forStatusbar, wx.ID_ANY, u"MyButton", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        bSizerforpanel1.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_panel1forStatusbar.SetSizer(bSizerforpanel1)
        self.m_panel1forStatusbar.Layout()
        bSizerforpanel1.Fit(self.m_panel1forStatusbar)
        self.statusBar.AddPage(self.m_panel1forStatusbar, u"模型管理", True)
        self.m_panel2forStatusbar = wx.Panel(self.statusBar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TAB_TRAVERSAL)
        bSizerforpanel2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button10 = wx.Button(self.m_panel2forStatusbar, wx.ID_ANY, u"数据预处理", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.m_button10.Bind(wx.EVT_LEFT_DOWN, self.ClickDataInit)
        bSizerforpanel2.Add(self.m_button10, 0, wx.ALL, 5)

        self.m_button15 = wx.Button(self.m_panel2forStatusbar, wx.ID_ANY, u"不确定性定义", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel2.Add(self.m_button15, 0, wx.ALL, 5)

        self.m_button16 = wx.Button(self.m_panel2forStatusbar, wx.ID_ANY, u"不确定性描述", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel2.Add(self.m_button16, 0, wx.ALL, 5)

        self.m_button17 = wx.Button(self.m_panel2forStatusbar, wx.ID_ANY, u"MyButton", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel2.Add(self.m_button17, 0, wx.ALL, 5)

        self.m_panel2forStatusbar.SetSizer(bSizerforpanel2)
        self.m_panel2forStatusbar.Layout()
        bSizerforpanel2.Fit(self.m_panel2forStatusbar)
        self.statusBar.AddPage(self.m_panel2forStatusbar, u"不确定性建模", False)
        self.m_panel3forStatusbar = wx.Panel(self.statusBar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TAB_TRAVERSAL)
        bSizerforpanel3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button18 = wx.Button(self.m_panel3forStatusbar, wx.ID_ANY, u"试验设计", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.m_button18.Bind(wx.EVT_LEFT_DOWN, self.ClickTestDesign)
        bSizerforpanel3.Add(self.m_button18, 0, wx.ALL, 5)

        self.m_button19 = wx.Button(self.m_panel3forStatusbar, wx.ID_ANY, u"抽样设置", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.m_button19.Bind(wx.EVT_LEFT_DOWN, self.SamplingSettings)
        bSizerforpanel3.Add(self.m_button19, 0, wx.ALL, 5)

        self.m_button20 = wx.Button(self.m_panel3forStatusbar, wx.ID_ANY, u"试验方案", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel3.Add(self.m_button20, 0, wx.ALL, 5)

        self.m_button21 = wx.Button(self.m_panel3forStatusbar, wx.ID_ANY, u"传播分析", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel3.Add(self.m_button21, 0, wx.ALL, 5)

        self.m_panel3forStatusbar.SetSizer(bSizerforpanel3)
        self.m_panel3forStatusbar.Layout()
        bSizerforpanel3.Fit(self.m_panel3forStatusbar)
        self.statusBar.AddPage(self.m_panel3forStatusbar, u"不确定性传播分析", False)
        self.m_panel4forStatusbar = wx.Panel(self.statusBar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TAB_TRAVERSAL)
        bSizerforpanel4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button22 = wx.Button(self.m_panel4forStatusbar, wx.ID_ANY, u"验证数据配置", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        self.m_button22.Bind(wx.EVT_LEFT_DOWN, self.ClickDataConfiguration)
        bSizerforpanel4.Add(self.m_button22, 0, wx.ALL, 5)

        self.m_button23 = wx.Button(self.m_panel4forStatusbar, wx.ID_ANY, u"特征提取", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel4.Add(self.m_button23, 0, wx.ALL, 5)

        self.m_button24 = wx.Button(self.m_panel4forStatusbar, wx.ID_ANY, u"验证准则", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel4.Add(self.m_button24, 0, wx.ALL, 5)

        self.m_button25 = wx.Button(self.m_panel4forStatusbar, wx.ID_ANY, u"验证分析", wx.DefaultPosition,
                                    wx.DefaultSize, 0)
        bSizerforpanel4.Add(self.m_button25, 0, wx.ALL, 5)

        self.m_panel4forStatusbar.SetSizer(bSizerforpanel4)
        self.m_panel4forStatusbar.Layout()
        bSizerforpanel4.Fit(self.m_panel4forStatusbar)
        self.statusBar.AddPage(self.m_panel4forStatusbar, u"仿真验证分析", False)

        self.m_panel5forStatusbar = wx.Panel(self.statusBar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TAB_TRAVERSAL)
        bSizerforpanel5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button171 = wx.Button(self.m_panel5forStatusbar, wx.ID_ANY, u"元模型管理", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        self.m_button171.Bind(wx.EVT_LEFT_DOWN, self.ClickMetamodelManage)
        bSizerforpanel5.Add(self.m_button171, 0, wx.ALL, 5)

        self.m_button181 = wx.Button(self.m_panel5forStatusbar, wx.ID_ANY, u"智能模型管理", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizerforpanel5.Add(self.m_button181, 0, wx.ALL, 5)

        self.m_button191 = wx.Button(self.m_panel5forStatusbar, wx.ID_ANY, u"校准准则", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizerforpanel5.Add(self.m_button191, 0, wx.ALL, 5)

        self.m_button201 = wx.Button(self.m_panel5forStatusbar, wx.ID_ANY, u"智能优化校准", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        bSizerforpanel5.Add(self.m_button201, 0, wx.ALL, 5)

        self.m_panel5forStatusbar.SetSizer(bSizerforpanel5)
        self.m_panel5forStatusbar.Layout()
        bSizerforpanel5.Fit(self.m_panel5forStatusbar)
        self.statusBar.AddPage(self.m_panel5forStatusbar, u"智能校准分析", False)

        bSizerforwholepanel.Add(self.statusBar, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel10 = wx.Panel(self.m_panelfor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_treeCtrl4 = wx.TreeCtrl(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TR_DEFAULT_STYLE)

        """左侧树状图"""
        root = self.m_treeCtrl4.AddRoot('程序员')
        os = self.m_treeCtrl4.AppendItem(root, '操作系统')
        pl = self.m_treeCtrl4.AppendItem(root, '编程语言')
        tk = self.m_treeCtrl4.AppendItem(root, '工具套件')
        self.m_treeCtrl4.AppendItem(os, 'Linux')
        self.m_treeCtrl4.AppendItem(os, 'FreeBSD')
        self.m_treeCtrl4.AppendItem(os, 'OpenBSD')
        self.m_treeCtrl4.AppendItem(os, 'NetBSD')
        self.m_treeCtrl4.AppendItem(os, 'Solaris')
        cl = self.m_treeCtrl4.AppendItem(pl, '编译语言')
        sl = self.m_treeCtrl4.AppendItem(pl, '脚本语言')
        self.m_treeCtrl4.AppendItem(cl, 'Java')
        self.m_treeCtrl4.AppendItem(cl, 'C++')
        self.m_treeCtrl4.AppendItem(cl, 'C')
        self.m_treeCtrl4.AppendItem(cl, 'Pascal')
        self.m_treeCtrl4.AppendItem(sl, 'Ruby')
        self.m_treeCtrl4.AppendItem(sl, 'Tcl')
        self.m_treeCtrl4.AppendItem(sl, 'PHP')
        self.m_treeCtrl4.AppendItem(sl, 'Python')
        self.m_treeCtrl4.AppendItem(tk, 'Qt')
        self.m_treeCtrl4.AppendItem(tk, 'MFC')
        self.m_treeCtrl4.AppendItem(tk, 'wxPython')
        self.m_treeCtrl4.AppendItem(tk, 'GTK+')
        self.m_treeCtrl4.AppendItem(tk, 'Swing')
        self.m_treeCtrl4.Bind(wx.EVT_TREE_SEL_CHANGED,
                       self.OnSelChanged, id=1)

        bSizer5.Add(self.m_treeCtrl4, 1, wx.ALL | wx.EXPAND, 5)

        self.m_auinotebook1 = wx.aui.AuiNotebook(self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                 wx.aui.AUI_NB_DEFAULT_STYLE)
        self.m_panel19 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_auinotebook1.AddPage(self.m_panel19, u"模型管理", False)
        self.m_auinotebook1.DeletePage(self.m_auinotebook1.GetPageIndex(self.m_panel19))

        self.m_panel20 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.m_auinotebook1.AddPage(self.m_panel20, u"不确定性建模", False)
        self.m_auinotebook1.DeletePage(self.m_auinotebook1.GetPageIndex(self.m_panel20))

        self.m_panel21 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer19 = wx.BoxSizer(wx.VERTICAL)

        self.m_auinotebook1.AddPage(self.m_panel21, u"不确定性传播分析", False)
        self.m_auinotebook1.DeletePage(self.m_auinotebook1.GetPageIndex(self.m_panel21))

        self.m_panel22 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer20 = wx.BoxSizer(wx.VERTICAL)

        self.m_auinotebook1.AddPage(self.m_panel22, u"仿真验证分析", True)
        self.m_auinotebook1.DeletePage(self.m_auinotebook1.GetPageIndex(self.m_panel22))

        self.m_panel23 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                  wx.TAB_TRAVERSAL)
        bSizer13 = wx.BoxSizer(wx.VERTICAL)
        self.m_auinotebook1.AddPage(self.m_panel23, u"智能校准分析", False)
        self.m_auinotebook1.DeletePage(self.m_auinotebook1.GetPageIndex(self.m_panel23))

        bSizer5.Add(self.m_auinotebook1, 4, wx.EXPAND | wx.ALL, 5)

        self.m_panel10.SetSizer(bSizer5)
        self.m_panel10.Layout()
        bSizer5.Fit(self.m_panel10)
        bSizerforwholepanel.Add(self.m_panel10, 4, wx.EXPAND | wx.ALL, 5)

        self.m_panelfor.SetSizer(bSizerforwholepanel)
        self.m_panelfor.Layout()
        bSizerforwholepanel.Fit(self.m_panelfor)
        bSizerforwholeframe.Add(self.m_panelfor, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizerforwholeframe)
        self.Layout()
        self.m_statusBar3 = self.CreateStatusBar(1, 0, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_panel1forStatusbar.Bind(wx.EVT_LEFT_DCLICK, self.m_panel1forStatusbarOnLeftDClick)
        self.m_panel2forStatusbar.Bind(wx.EVT_LEFT_DCLICK, self.m_panel2forStatusbarOnLeftDClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    """创建模型管理界面"""
    def CreateModelManagePanel(self):
        flag = True
        for i in range(0,self.m_auinotebook1.PageCount):
            if self.m_auinotebook1.GetPage(i) == self.m_panel19:
                flag = False
        if flag:
            self.m_panel19 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer17 = wx.BoxSizer(wx.VERTICAL)

            self.m_grid9 = wx.grid.Grid(self.m_panel19, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

            # Grid
            self.m_grid9.CreateGrid(5, 5)
            self.m_grid9.EnableEditing(True)
            self.m_grid9.EnableGridLines(True)
            self.m_grid9.EnableDragGridSize(False)
            self.m_grid9.SetMargins(0, 0)

            # Columns
            self.m_grid9.EnableDragColMove(False)
            self.m_grid9.EnableDragColSize(True)
            self.m_grid9.SetColLabelSize(30)
            self.m_grid9.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Rows
            self.m_grid9.EnableDragRowSize(True)
            self.m_grid9.SetRowLabelSize(80)
            self.m_grid9.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Label Appearance

            # Cell Defaults
            self.m_grid9.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
            bSizer17.Add(self.m_grid9, 1, wx.ALL | wx.EXPAND, 5)

            self.m_panel19.SetSizer(bSizer17)
            self.m_panel19.Layout()
            bSizer17.Fit(self.m_panel19)
            self.m_auinotebook1.AddPage(self.m_panel19, u"模型管理", False, wx.NullBitmap)
        else:
            self.m_panel19.Show()
        self.m_panel19.SetFocus()
        self.Refresh()
    """创建不确定性建模界面"""
    def CreateUncertaintyModelingPanel(self):
        flag = True
        for i in range(0, self.m_auinotebook1.PageCount):
            if self.m_auinotebook1.GetPage(i) == self.m_panel20:
                flag = False
        if flag:
            self.m_panel20 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
            bSizer18 = wx.BoxSizer(wx.VERTICAL)

            self.m_grid10 = wx.grid.Grid(self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

            # Grid
            self.m_grid10.CreateGrid(5, 5)
            self.m_grid10.EnableEditing(True)
            self.m_grid10.EnableGridLines(True)
            self.m_grid10.EnableDragGridSize(False)
            self.m_grid10.SetMargins(0, 0)

            # Columns
            self.m_grid10.EnableDragColMove(False)
            self.m_grid10.EnableDragColSize(True)
            self.m_grid10.SetColLabelSize(30)
            self.m_grid10.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Rows
            self.m_grid10.EnableDragRowSize(True)
            self.m_grid10.SetRowLabelSize(80)
            self.m_grid10.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Label Appearance

            # Cell Defaults
            self.m_grid10.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
            bSizer18.Add(self.m_grid10, 1, wx.ALL | wx.EXPAND, 5)

            self.m_panel20.SetSizer(bSizer18)
            self.m_panel20.Layout()
            bSizer18.Fit(self.m_panel20)
            self.m_auinotebook1.AddPage(self.m_panel20, u"不确定性建模", False, wx.NullBitmap)
        else:
            self.m_panel20.Show()
        self.m_panel20.SetFocus()
        self.Refresh()
    """创建不确定性传播"""
    def CreateUncertaintySpreadPanel(self):
        flag = True
        for i in range(0, self.m_auinotebook1.PageCount):
            if self.m_auinotebook1.GetPage(i) == self.m_panel21:
                flag = False
        if flag:
            self.m_panel21 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
            bSizer19 = wx.BoxSizer(wx.VERTICAL)

            self.m_grid11 = wx.grid.Grid(self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

            results = oursql.show_sampling_result()
            # Grid
            self.m_grid11.CreateGrid(len(results), 4)
            self.m_grid11.EnableEditing(True)
            self.m_grid11.EnableGridLines(True)
            self.m_grid11.EnableDragGridSize(False)
            self.m_grid11.SetMargins(0, 0)

            # Columns
            self.m_grid11.EnableDragColMove(False)
            self.m_grid11.EnableDragColSize(True)
            self.m_grid11.SetColLabelSize(30)
            self.m_grid11.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
            self.m_grid11.SetColLabelValue(0, "抽样编号")
            self.m_grid11.SetColLabelValue(1, "抽样数据")
            self.m_grid11.SetColLabelValue(2, "抽样方法")
            self.m_grid11.SetColLabelValue(3, "分布类型")

            # Rows
            self.m_grid11.EnableDragRowSize(True)
            self.m_grid11.SetRowLabelSize(80)
            self.m_grid11.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # 设置内容
            i = 0
            for row in results:
                self.m_grid11.SetCellValue(i, 0, str(row[0]))
                self.m_grid11.SetCellValue(i, 1, str(row[1]))
                self.m_grid11.SetCellValue(i, 2, str(row[2]))
                self.m_grid11.SetCellValue(i, 3, str(row[3]))
                i = i + 1

            # Label Appearance

            # Cell Defaults
            self.m_grid11.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
            bSizer19.Add(self.m_grid11, 1, wx.ALL | wx.EXPAND, 5)

            self.m_panel21.SetSizer(bSizer19)
            self.m_panel21.Layout()
            bSizer19.Fit(self.m_panel21)
            self.m_auinotebook1.AddPage(self.m_panel21, u"不确定性传播分析", False, wx.NullBitmap)
        else:
            self.m_panel21.Show()
        self.m_panel21.SetFocus()
        self.Refresh()
    """创建仿真验证分析"""
    def CreateSimulationVerificationPanel(self):
        flag = True
        for i in range(0, self.m_auinotebook1.PageCount):
            if self.m_auinotebook1.GetPage(i) == self.m_panel22:
                flag = False
        if flag:
            self.m_panel22 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
            bSizer20 = wx.BoxSizer(wx.VERTICAL)

            self.m_grid12 = wx.grid.Grid(self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

            # Grid
            self.m_grid12.CreateGrid(5, 5)
            self.m_grid12.EnableEditing(True)
            self.m_grid12.EnableGridLines(True)
            self.m_grid12.EnableDragGridSize(False)
            self.m_grid12.SetMargins(0, 0)

            # Columns
            self.m_grid12.EnableDragColMove(False)
            self.m_grid12.EnableDragColSize(True)
            self.m_grid12.SetColLabelSize(30)
            self.m_grid12.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Rows
            self.m_grid12.EnableDragRowSize(True)
            self.m_grid12.SetRowLabelSize(80)
            self.m_grid12.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Label Appearance

            # Cell Defaults
            self.m_grid12.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
            bSizer20.Add(self.m_grid12, 1, wx.ALL | wx.EXPAND, 5)

            self.m_panel22.SetSizer(bSizer20)
            self.m_panel22.Layout()
            bSizer20.Fit(self.m_panel22)
            self.m_auinotebook1.AddPage(self.m_panel22, u"仿真验证分析", True, wx.NullBitmap)
        else:
            self.m_panel22.Show()
        self.m_panel22.SetFocus()
        self.Refresh()
    """创建智能校准分析界面"""
    def CreateIntelligentalibrationPanel(self):
        flag = True
        for i in range(0, self.m_auinotebook1.PageCount):
            if self.m_auinotebook1.GetPage(i) == self.m_panel23:
                flag = False
        if flag:
            self.m_panel23 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
            bSizer13 = wx.BoxSizer(wx.VERTICAL)

            self.m_grid5 = wx.grid.Grid(self.m_panel23, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

            # Grid
            self.m_grid5.CreateGrid(5, 5)
            self.m_grid5.EnableEditing(True)
            self.m_grid5.EnableGridLines(True)
            self.m_grid5.EnableDragGridSize(False)
            self.m_grid5.SetMargins(0, 0)

            # Columns
            self.m_grid5.EnableDragColMove(False)
            self.m_grid5.EnableDragColSize(True)
            self.m_grid5.SetColLabelSize(30)
            self.m_grid5.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Rows
            self.m_grid5.EnableDragRowSize(True)
            self.m_grid5.SetRowLabelSize(80)
            self.m_grid5.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

            # Label Appearance

            # Cell Defaults
            self.m_grid5.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
            bSizer13.Add(self.m_grid5, 0, wx.ALL, 5)

            self.m_panel23.SetSizer(bSizer13)
            self.m_panel23.Layout()
            bSizer13.Fit(self.m_panel23)
            self.m_auinotebook1.AddPage(self.m_panel23, u"智能校准分析", False, wx.NullBitmap)
        else:
            self.m_panel23.Show()
        self.m_panel23.SetFocus()
        self.Refresh()

    def m_panel1forStatusbarOnLeftDClick(self, event):
        event.Skip()

    def m_panel2forStatusbarOnLeftDClick(self, event):
        event.Skip()

    def OnSelChanged(self, event):
        item = event.GetItem()
        self.display.SetLabel(self.tree.GetItemText(item))

    def ClickModelManage(self, event):
        self.CreateModelManagePanel()

    def ClickDataInit(self, event):
        self.CreateUncertaintyModelingPanel()

    def ClickTestDesign(self, event):
        self.CreateUncertaintySpreadPanel()

    def ClickDataConfiguration(self, event):
        self.CreateSimulationVerificationPanel()

    def ClickMetamodelManage(self, event):
        self.CreateIntelligentalibrationPanel()

    def SamplingSettings(self, event):
        frame = sui.SamplingDialog(None)
        frame.Show()

app = wx.App(False)
frame = PlatformForUncertainly(None)
frame.Show()
app.MainLoop()