# -*- coding: utf-8 -*-

import wx
from wx import aui
from wx import grid
import Import_file
import Run
import Sql

class ShowNotebook(aui.AuiNotebook):
    
    def __init__(self, parent = None):
        
        aui.AuiNotebook.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, 
                                 wx.DefaultSize, aui.AUI_NB_DEFAULT_STYLE)
        
    def NewProj(self, pProj = 0):
        self.show_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, 
                                   wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.AddPage(self.show_panel, u"新建项目", True, wx.NullBitmap)
        show_panel = self.show_panel
        show_panel.pid = pProj
        # show_panel 的布局，只有 scrollPanel 一个元素
        show_panel.bSizer = wx.BoxSizer(wx.VERTICAL)
        #为实现滚动条加入 scrollPanel
        show_panel.scrolledWindow = wx.ScrolledWindow(show_panel, wx.ID_ANY, 
                    wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
        show_panel.scrolledWindow.SetScrollRate(5, 5)
        scrollPanel = show_panel.scrolledWindow
        # scrollPanel 的布局，元素为显示的控件
        show_panel.gbSizer = wx.GridBagSizer(5, 5)
        show_panel.gbSizer.SetFlexibleDirection(wx.BOTH)
        show_panel.gbSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        
        show_panel.staticText1 = wx.StaticText(scrollPanel, wx.ID_ANY, u"项目名称：", 
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        show_panel.gbSizer.Add(show_panel.staticText1, wx.GBPosition(2, 4), 
                               wx.GBSpan(1, 1), wx.ALL, 5)
        
        show_panel.textCtrl1 = wx.TextCtrl(scrollPanel, wx.ID_ANY, wx.EmptyString, 
                                           wx.DefaultPosition, wx.Size(300,-1), 0)
        show_panel.gbSizer.Add(show_panel.textCtrl1, wx.GBPosition(2, 5), 
                               wx.GBSpan(1, 3), wx.ALL, 5)
        
        show_panel.staticText3 = wx.StaticText(scrollPanel, wx.ID_ANY, u"*此项目已存在", 
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        show_panel.staticText3.SetForegroundColour('red')
        show_panel.gbSizer.Add(show_panel.staticText3, wx.GBPosition(2, 8), 
                             wx.GBSpan(1, 1), wx.ALL, 5)
        show_panel.staticText3.Show(show=False)
        
        show_panel.staticText2 = wx.StaticText(scrollPanel, wx.ID_ANY, u"项目描述：", 
                                               wx.DefaultPosition, wx.DefaultSize, 0)
        show_panel.gbSizer.Add(show_panel.staticText2, wx.GBPosition(3, 4), 
                               wx.GBSpan(1, 1), wx.ALL, 5)
        
        show_panel.textCtrl2 = wx.TextCtrl(scrollPanel, wx.ID_ANY, wx.EmptyString, 
                    wx.DefaultPosition, wx.Size(500,100), wx.TE_MULTILINE | wx.TE_RICH)
        show_panel.gbSizer.Add(show_panel.textCtrl2, wx.GBPosition(3, 5), 
                               wx.GBSpan(3, 5), wx.ALL, 5)
        
        show_panel.button1 = wx.Button(scrollPanel, wx.ID_ANY, u"导入模型", 
                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.ClickImport, show_panel.button1)
        show_panel.gbSizer.Add(show_panel.button1, wx.GBPosition(5, 12), 
                               wx.GBSpan(1, 1), wx.ALL, 5)
        
        scrollPanel.SetSizer(show_panel.gbSizer)
        scrollPanel.Layout()
        show_panel.bSizer.Add(scrollPanel, 1, wx.EXPAND |wx.ALL, 5 )
        show_panel.SetSizer(show_panel.bSizer)
        show_panel.Layout()
    
    #点击导入模型事件
    def ClickImport(self, event):
        show_panel = self.GetCurrentPage()
        proj_name = show_panel.textCtrl1.GetValue()
        if proj_name == '':
            return
        proj_descr = show_panel.textCtrl2.GetValue()
        record = Sql.selectSql((proj_name, show_panel.pid), Sql.selectProj)
        if record != []:
            show_panel.staticText3.Show(show=True)
            show_panel.Layout()
            return
        show_panel.staticText3.Show(show=False)
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:
            proj = Import_file.insert_blob(proj_name, show_panel.pid, 
                                           proj_descr, dlg.GetPath())
            show_panel.textCtrl1.Disable() #导入成功后控件变为不可编辑
            show_panel.textCtrl2.Disable()
            show_panel.button1.Disable()
            self.GetParent().GetParent().navTree.updateTree()
            self.genInParams(proj, show_panel)
        dlg.Destroy()
    
    #导入成功后生成输入参数控件
    def genInParams(self, proj, show_panel):
        Run.read_blob(proj)
        params = Run.read_param(proj)
        scrollPanel = show_panel.scrolledWindow
        show_panel.staticText4 = wx.StaticText(scrollPanel, wx.ID_ANY, 
                                u"模型输入参数共" + str(len(params)) + u"个：", 
                                wx.DefaultPosition, wx.DefaultSize, 0)
        show_panel.gbSizer.Add(show_panel.staticText4, wx.GBPosition(7, 4), 
                               wx.GBSpan(1, 2), wx.ALL, 5)
        show_panel.staticText5 = wx.StaticText(scrollPanel, wx.ID_ANY, 
                                u"参数描述", wx.DefaultPosition, wx.DefaultSize, 0)
        show_panel.gbSizer.Add(show_panel.staticText5, wx.GBPosition(7, 4), 
                               wx.GBSpan(1, 2), wx.ALL, 5)
        show_panel.Layout()
