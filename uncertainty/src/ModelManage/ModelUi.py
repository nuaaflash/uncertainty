# -*- coding: utf-8 -*-

import wx
import NavTree
import ShowPanel
import import_file

class ModelPanel(wx.Panel):
    
    def __init__(self, parent = None):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, 
                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.InitUI()
        
    def InitUI(self):
        self.btnPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, 
                                 wx.DefaultSize, wx.TAB_TRAVERSAL)
        tabSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btnPanel.SetSizer(tabSizer)
        
        self.button1 = wx.Button(self.btnPanel, wx.ID_ANY, u"模型设置", 
                                 wx.DefaultPosition, wx.DefaultSize, 0)
#         self.button1.SetBitmap(wx.Bitmap('icon/btn_show1.tga'))
        self.button1.Bind(wx.EVT_LEFT_DOWN, self.ClickModelManage)
        tabSizer.Add(self.button1, 0, wx.ALL, 5)

        self.button2 = wx.Button(self.btnPanel, wx.ID_ANY, u"参数设置", 
                                 wx.DefaultPosition, wx.DefaultSize, 0)
        tabSizer.Add(self.button2, 0, wx.ALL, 5)

        self.button3 = wx.Button(self.btnPanel, wx.ID_ANY, u"数据导入",
                                 wx.DefaultPosition, wx.DefaultSize, 0)
        tabSizer.Add(self.button3, 0, wx.ALL, 5)

        self.button4 = wx.Button(self.btnPanel, wx.ID_ANY, u"MyButton", 
                                 wx.DefaultPosition, wx.DefaultSize, 0)
        tabSizer.Add(self.button4, 0, wx.ALL, 5)
        
        self.displayPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, 
                                     wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.navTree = NavTree.NavTree(self.displayPanel)
        self.showPanel = ShowPanel.ShowPanel(self.displayPanel)
        hBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        hBoxSizer.Add(self.navTree, 1, wx.ALL | wx.EXPAND, 5)
        hBoxSizer.Add(self.showPanel, 4, wx.EXPAND | wx.ALL, 5)
        self.displayPanel.SetSizer(hBoxSizer)
        
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)
        vBoxSizer.Add(self.btnPanel, 1, wx.EXPAND | wx.ALL, 5)
        vBoxSizer.Add(self.displayPanel, 8, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(vBoxSizer)
#         self.Layout()
#         vBoxSizer.Fit(self)
        
        
    def ClickModelManage(self, event):
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:
            import_file.insert_blob(project='一元非线性回归', _dir=dlg.GetPath()) #文件夹路径  
              
        dlg.Destroy()
        