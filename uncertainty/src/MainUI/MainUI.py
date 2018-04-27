# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from ModelManage import ModelUi


class PlatformForUncertainly(wx.Frame):
    
    def __init__(self, parent = None, id = -1, UpdateUI = None, params = {}):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title= u"不确定性智能仿真模型校准平台", 
                          pos=wx.DefaultPosition, size=wx.Size(1280, 720), 
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetIcon(wx.Icon('icon/lihf.ico', wx.BITMAP_TYPE_ICO))
        self.SetSizeHints((1280, 720), wx.DefaultSize)
        self.Maximize(True)
        self.UpdateUI = UpdateUI
        self.InitUI()
        
    def InitUI(self):
        
        px = wx.DisplaySize()
        self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, 
                                    wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizerforwholepanel = wx.BoxSizer(wx.VERTICAL)
        self.main_panel.SetSizer(bSizerforwholepanel)
        
        
        self.statusBar = wx.Notebook(self.main_panel, wx.ID_ANY, 
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        bSizerforwholepanel.Add(self.statusBar, 1, wx.EXPAND | wx.ALL, 5)
        
        self.model_panel = ModelUi.ModelPanel(self.statusBar)
        self.model_panel2 = ModelUi.ModelPanel(self.statusBar)
        self.model_panel3 = ModelUi.ModelPanel(self.statusBar)
#         self.model_panel4 = ModelUi.ModelPanel(self.statusBar)
        self.statusBar.AddPage(self.model_panel, u"UncertaintyModeling", True)
        self.statusBar.AddPage(self.model_panel2, u"不确定性建模", False)
        self.statusBar.AddPage(self.model_panel3, u"不确定性传播分析", False)
#         self.statusBar.AddPage(self.model_panel4, u"仿真验证分析", True)

        self.main_panel.Layout()
         
#         bSizerforwholepanel.Fit(self.main_panel)
        
        
class MainApp(wx.App):
    def OnInit(self):
        self.frame = PlatformForUncertainly()
        self.frame.Show()
        return True

def main():
    app = MainApp()
    app.MainLoop()

if __name__ == "__main__":
    main()