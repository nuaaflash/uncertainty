#coding=utf-8
import wx
# 导入wxPython中的通用Button
import wx.lib.buttons as wxButton

class LoginFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, UpdateUI=None):
        wx.Frame.__init__(self, parent, id, title='登录界面', size=(320, 200))

        self.UpdateUI = UpdateUI
        self.InitUI() # 绘制UI界面

    def InitUI(self):
        panel = wx.Panel(self)
        
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, True)

        accountLabel = wx.StaticText(panel, -1, '账号', pos=(20, 25))
        accountLabel.SetForegroundColour('#0a74f7')
        accountLabel.SetFont(font)
        self.accountInput = wx.TextCtrl(panel, -1, u'', pos=(80, 25), size=(180, -1))
        self.accountInput.SetForegroundColour('gray')
        self.accountInput.SetFont(font)

        
        passwordLabel = wx.StaticText(panel, -1, '密码', pos=(20, 70))
        passwordLabel.SetForegroundColour('#0a74f7')
        passwordLabel.SetFont(font)
        self.passwordInput = wx.TextCtrl(panel, -1, u'', pos=(80, 70), size=(180, -1), style=wx.TE_PASSWORD)
        self.passwordInput.SetFont(font)

        sureButton = wx.Button(panel, -1, u'登录', pos=(20, 110), size=(120, 40))
        sureButton.SetBackgroundColour('#0a74f7')
        sureButton.SetForegroundColour('white')
        self.Bind(wx.EVT_BUTTON, self.loginFunction, sureButton) # 为【确定Button】绑定事件

        cancleButton = wx.Button(panel, -1, u'取消', pos=(160, 110), size=(120, 40))
        cancleButton.SetBackgroundColour('black')
        cancleButton.SetForegroundColour('#ffffff')
        self.Bind(wx.EVT_BUTTON, self.cancleEvent, cancleButton)


    def loginFunction(self, event):
        account = self.accountInput.GetValue()
        password = self.passwordInput.GetValue()
        params = {"account":account}
        self.Destroy()
        print '接收到用户的输入：', params
        self.UpdateUI(1, params) #更新UI-Frame
        
    def cancleEvent(self, event):
        wx.Exit()
