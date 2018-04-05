import wx
import wx.xrc
import wx.aui


###########################################################################
## Class MyFrame2
###########################################################################

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
						  size=wx.Size(228, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

		sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"Input the arguments"), wx.VERTICAL)

		self.m_staticText1 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Arg1", wx.DefaultPosition,
										   wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)
		sbSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

		self.m_textCtrl1 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
									   wx.DefaultSize, 0)
		sbSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)

		self.m_staticText2 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Arg2", wx.DefaultPosition,
										   wx.DefaultSize, 0)
		self.m_staticText2.Wrap(-1)
		sbSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

		self.m_textCtrl2 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
									   wx.DefaultSize, 0)
		sbSizer1.Add(self.m_textCtrl2, 0, wx.ALL, 5)

		self.m_button1 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize,
								   0)
		self.m_button1.Bind(wx.EVT_BUTTON, self.getArgs)
		sbSizer1.Add(self.m_button1, 0, wx.ALL, 5)

		self.SetSizer(sbSizer1)
		self.Layout()

		self.Centre(wx.BOTH)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def getArgs(self, event):
		arg1 = float(self.m_textCtrl1.GetValue())
		arg2 = float(self.m_textCtrl2.GetValue())
		print arg1, arg2
		return arg1, arg2


app = wx.App(False)
frame = MyFrame1(None)
frame.Show()
app.MainLoop()