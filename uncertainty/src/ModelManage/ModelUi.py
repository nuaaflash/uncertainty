# -*- coding: utf-8 -*-

import wx
import NavPanel
import ShowPanel
import import_file

class ModelPanel(wx.Panel):
    
    def __init__(self, parent = None):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, 
                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.InitUI()
        
    def InitUI(self):
        tabSizer = wx.BoxSizer(wx.HORIZONTAL)
        

        self.button1 = wx.Button(self, wx.ID_ANY, u"模型设置", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        self.button1.SetBitmap(wx.Bitmap('icon/btn_show1.tga'))
        self.button1.Bind(wx.EVT_LEFT_DOWN, self.ClickModelManage)

        tabSizer.Add(self.button1, 0, wx.ALL, 5)

        self.button2 = wx.Button(self, wx.ID_ANY, u"参数设置", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        tabSizer.Add(self.button2, 0, wx.ALL, 5)

        self.button3 = wx.Button(self, wx.ID_ANY, u"数据导入", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        tabSizer.Add(self.button3, 0, wx.ALL, 5)

        self.button4 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition,
                                   wx.DefaultSize, 0)
        tabSizer.Add(self.button4, 0, wx.ALL, 5)
        
        self.navPanel = NavPanel.NavPanel(self)
        self.showPanel = ShowPanel.ShowPanel(self)
        hBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        hBoxSizer.Add(self.navPanel, 0, wx.ALL, 5)
        hBoxSizer.Add(self.showPanel, 0, wx.ALL, 5)
        
        
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)
        
        vBoxSizer.Add(tabSizer, 1, wx.EXPAND | wx.ALL, 5)
        vBoxSizer.Add(hBoxSizer, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(vBoxSizer)
        self.Layout()
        vBoxSizer.Fit(self)
        
        
    def ClickModelManage(self, event):
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:
            import_file.insert_blob(project='一元非线性回归', _dir=dlg.GetPath()) #文件夹路径  
              
        dlg.Destroy()
        