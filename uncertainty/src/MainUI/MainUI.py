# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import sys
sys.path.append('C:/Users/Zhang Wanpeng/Desktop/uncertainty/uncertainty/src/ModelManage')
import ModelUi
sys.path.append('C:/Users/Zhang Wanpeng/Desktop/uncertainty/uncertainty/src/UncertaintyPropagation')
import  UncertaintyPropagationUi
sys.path.append('C:/Users/Zhang Wanpeng/Desktop/uncertainty/uncertainty/src/VerificationAnalysis')
import  VerificationAnalysisUi
sys.path.append('C:/Users/Zhang Wanpeng/Desktop/uncertainty/uncertainty/src/UncertaintyModeling')
import  UncertaintyModelingUi
sys.path.append('C:/Users/Zhang Wanpeng/Desktop/uncertainty/uncertainty/src/IntelligentCalibration')
import  IntelligentCalibrationUi

class PlatformForUncertainly(wx.Frame):
    
    def __init__(self, parent = None, id = -1, UpdateUI = None, params = {}):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title= u"不确定性智能仿真模型校准平台", 
                          pos=wx.DefaultPosition, size=wx.Size(1280, 720), 
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.UpdateUI = UpdateUI
        self.InitUI()
        self.Centre(wx.BOTH)
        
    def InitUI(self):
        
        self.SetIcon(wx.Icon('icon/lihf.ico', wx.BITMAP_TYPE_ICO))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        
    #    self.main_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition,wx.DefaultSize, wx.TAB_TRAVERSAL)
        
        self.statusBar = wx.Notebook(self, wx.ID_ANY,wx.DefaultPosition, wx.DefaultSize, 0)
        self.model_panel = ModelUi.ModelPanel(self.statusBar)
        self.model_panel2 = UncertaintyModelingUi.UncertaintyModelingPanel(self.statusBar)
        self.model_panel3 = UncertaintyPropagationUi.UncertaintyPropagationPanel(self.statusBar)
        self.model_panel4 = VerificationAnalysisUi.VerificationAnalysisPanel(self.statusBar)
        self.model_panel5 = IntelligentCalibrationUi.IntelligentCalibrationPanel(self.statusBar)
        """添加各个tab页"""
        self.statusBar.AddPage(self.model_panel, u"UncertaintyModeling", True)
        self.statusBar.AddPage(self.model_panel2, u"不确定性建模", True)
        self.statusBar.AddPage(self.model_panel3, u"不确定性传播分析", True)
        self.statusBar.AddPage(self.model_panel4, u"仿真验证分析", True)
        self.statusBar.AddPage(self.model_panel5, u"智能校准分析", True)
        
        bSizerforwholepanel = wx.BoxSizer(wx.VERTICAL)
        bSizerforwholepanel.Add(self.statusBar, 1, wx.EXPAND | wx.ALL, 5)
#          
        self.SetSizer(bSizerforwholepanel)
        self.Layout()
        """状态栏"""
        self.m_statusBar3 = self.CreateStatusBar(1, wx.EXPAND, wx.ID_ANY)
 #       bSizerforwholepanel.Fit(self.main_panel)
        
        
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