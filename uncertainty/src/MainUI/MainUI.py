# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx


class PlatformForUncertainly(wx.Frame):
    
    def __init__(self, parent = None, id = -1, UpdateUI = None, params = {}):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title= params['account'], pos=wx.DefaultPosition,
                          size=wx.Size(1280, 720), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.UpdateUI = UpdateUI
        self.InitUI()
        
    def InitUI(self):
        
        self.SetIcon(wx.Icon('icon/lihf.ico', wx.BITMAP_TYPE_ICO))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        
        self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        
        self.statusBar = wx.Notebook(self.main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        
        self.m_panel1forStatusbar = wx.Panel(self.statusBar, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                             wx.TAB_TRAVERSAL)
        
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