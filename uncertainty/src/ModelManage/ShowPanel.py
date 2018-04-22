# -*- coding: utf-8 -*-

import wx
from wx import aui
from wx import grid

class ShowPanel(wx.Panel):
    
    def __init__(self, parent = None):
        
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, 
                          wx.DefaultSize, wx.TAB_TRAVERSAL)
        
        self.m_auinotebook1 = aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 500),
                                                 aui.AUI_NB_DEFAULT_STYLE)
        self.m_panel19 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_auinotebook1.AddPage(self.m_panel19, u"UncertaintyModeling", False, wx.NullBitmap)
        self.m_auinotebook1.DeletePage(self.m_auinotebook1.GetPageIndex(self.m_panel19))

        self.m_panel20 = wx.Panel(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid10 = grid.Grid(self.m_panel20, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
