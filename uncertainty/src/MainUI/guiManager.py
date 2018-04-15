# -*- coding: utf-8 -*-

import loginFrame
import MainUI

class GuiManager():
    def __init__(self, UpdateUI):
        self.UpdateUI = UpdateUI

    def GetFrame(self, type, params):
        frame = self.CreateFrame(type, params)
        return frame

    def CreateFrame(self, type, params):
        if type == 0:
            return loginFrame.LoginFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
        elif type == 1:
            return MainUI.PlatformForUncertainly(parent=None, id=type, 
                                                 UpdateUI=self.UpdateUI, params=params)