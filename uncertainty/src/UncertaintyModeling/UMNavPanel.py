# -*- coding: utf-8 -*-

import wx
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import config
import sql
import mysql.connector

class NavPanel(wx.Panel):
    
    def __init__(self, parent = None):
        
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, 
                          wx.DefaultSize, wx.TAB_TRAVERSAL)

        bSizer = wx.BoxSizer(wx.VERTICAL)

        self.m_treeCtrl4 = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TR_DEFAULT_STYLE)

        db_config = config.datasourse
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            args = ()
            cursor.execute(sql.modelSql, args)
            record = cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

        str = record[0][0]
        """左侧树状图"""
        root = self.m_treeCtrl4.AddRoot('模型')
        tree = [[0] * 10] * 10
        i = 0
        for model in record:
            tree[i] = self.m_treeCtrl4.AppendItem(root, model[0])
            i += 1
        #         os = self.m_treeCtrl4.AppendItem(root, str)
        #         pl = self.m_treeCtrl4.AppendItem(root, str)
        #         tk = self.m_treeCtrl4.AppendItem(root, '工具套件')
        #         self.m_treeCtrl4.AppendItem(os, 'Linux')
        #         self.m_treeCtrl4.AppendItem(os, 'FreeBSD')
        #         self.m_treeCtrl4.AppendItem(os, 'OpenBSD')
        #         self.m_treeCtrl4.AppendItem(os, 'NetBSD')
        #         self.m_treeCtrl4.AppendItem(os, 'Solaris')
        #         cl = self.m_treeCtrl4.AppendItem(pl, '编译语言')
        #         sl = self.m_treeCtrl4.AppendItem(pl, '脚本语言')
        #         self.m_treeCtrl4.AppendItem(cl, 'Java')
        #         self.m_treeCtrl4.AppendItem(cl, 'C++')
        #         self.m_treeCtrl4.AppendItem(cl, 'C')
        #         self.m_treeCtrl4.AppendItem(cl, 'Pascal')
        #         self.m_treeCtrl4.AppendItem(sl, 'Ruby')
        #         self.m_treeCtrl4.AppendItem(sl, 'Tcl')
        #         self.m_treeCtrl4.AppendItem(sl, 'PHP')
        #         self.m_treeCtrl4.AppendItem(sl, 'Python')
        #         self.m_treeCtrl4.AppendItem(tk, 'Qt')
        #         self.m_treeCtrl4.AppendItem(tk, 'MFC')
        #         self.m_treeCtrl4.AppendItem(tk, 'wxPython')
        #         self.m_treeCtrl4.AppendItem(tk, 'GTK+')
        #         self.m_treeCtrl4.AppendItem(tk, 'Swing')
        #         self.m_treeCtrl4.Bind(wx.EVT_TREE_SEL_CHANGED,
        #                        self.OnSelChanged, id=1)
        bSizer.Add(self.m_treeCtrl4, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer)
        self.Layout()
        bSizer.Fit(self)