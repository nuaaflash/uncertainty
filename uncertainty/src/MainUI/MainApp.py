# -*- coding: utf-8 -*-

import wx
import guiManager

class MainAPP(wx.App):

    def OnInit(self):
        self.manager = guiManager.GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(0, {})
        self.frame.Show()
        return True

    def UpdateUI(self, ftype, params):
        self.frame.Destroy()
        self.frame = self.manager.GetFrame(ftype, params)
        self.frame.Show(True)

def main():
    app = MainAPP()
    app.MainLoop()

if __name__ == '__main__':
    main()