#!/usr/bin/env python  
#coding:utf-8  
""" 
  Author:  u"王浩" --<823921498@qq.com> 
  Purpose: u"文件夹选择对话框" 
  Created: 2014/8/26 
"""  
  
import wx
import import_file
  
  
###############################################################################  
class DirDialog(wx.Frame):  
    """"""  
  
    #----------------------------------------------------------------------  
    def __init__(self):  
        """Constructor"""  
        wx.Frame.__init__(self,None,-1,u"文件夹选择对话框")  
        b = wx.Button(self,-1,u"文件夹选择对话框")  
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)  
          
    #----------------------------------------------------------------------  
    def OnButton(self, event):  
        """"""  
        dlg = wx.DirDialog(self,u"选择文件夹",style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:
            import_file.insert_blob(project='一元非线性回归', _dir=dlg.GetPath()) #文件夹路径  
              
        dlg.Destroy() 
  
###############################################################################  
if __name__ == '__main__':  
    frame = wx.PySimpleApp()  
    app = DirDialog()  
    app.Show()  
    frame.MainLoop()  