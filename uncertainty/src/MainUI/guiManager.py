# -*- coding: utf-8 -*-

import loginFrame
import MainUI

class GuiManager():
    def __init__(self, UpdateUI):
        self.UpdateUI = UpdateUI

    def GetFrame(self, ftype, params):
        frame = self.CreateFrame(ftype, params)
        return frame

    def CreateFrame(self, ftype, params):
        if ftype == 0:
            return loginFrame.LoginFrame(parent=None, id=ftype, UpdateUI=self.UpdateUI)
        elif ftype == 1:
            return MainUI.PlatformForUncertainly(parent=None, id=ftype, 
                                                 UpdateUI=self.UpdateUI, params=params)