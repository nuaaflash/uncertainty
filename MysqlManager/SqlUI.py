# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import Oursql as oursql


###########################################################################
## Class MyFrame1
###########################################################################

class ShowResultOfSampling(wx.Frame):
    def __init__(self, parent, showset = 0, type = "" , method = "sampling_result"):
        results = oursql.show_sampling_result(showset,type,method)
        titletoshow =  "抽样方法:" + str(results[0][2]) +" 分布类型:" +  str(results[0][3])
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=titletoshow, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_grid11 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        # Grid
        self.m_grid11.CreateGrid(len(results), 2)
        self.m_grid11.EnableEditing(True)
        self.m_grid11.EnableGridLines(True)
        self.m_grid11.EnableDragGridSize(False)
        self.m_grid11.SetMargins(0, 0)

        # Columns
        self.m_grid11.EnableDragColMove(False)
        self.m_grid11.EnableDragColSize(True)
        self.m_grid11.SetColLabelSize(30)
        self.m_grid11.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.m_grid11.SetColLabelValue(0,"抽样编号")
        self.m_grid11.SetColLabelValue(1,"抽样数据")
        # self.m_grid11.SetColLabelValue(2,"抽样方法")
        # self.m_grid11.SetColLabelValue(3,"分布类型")

        # Rows
        self.m_grid11.EnableDragRowSize(True)
        self.m_grid11.SetRowLabelSize(80)
        self.m_grid11.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # 设置内容
        i = 0
        for row in results:
            self.m_grid11.SetCellValue(i,0,str(row[0]))
            self.m_grid11.SetCellValue(i,1,str(row[1]))
            # self.m_grid11.SetCellValue(i,2,str(row[2]))
            # self.m_grid11.SetCellValue(i,3,str(row[3]))
            i = i + 1

        # Label Appearance

        # Cell Defaults
        self.m_grid11.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gSizer1.Add(self.m_grid11, 0, wx.ALL, 3)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

# app = wx.App(False)
# frame = ShowResultOfSampling(None)
# frame.Show()
# app.MainLoop()
