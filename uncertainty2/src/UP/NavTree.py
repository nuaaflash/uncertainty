# -*- coding: utf-8 -*-

import wx
import config
import Sql
import mysql.connector
import ShowNotebook

class NavTree(wx.TreeCtrl):

    def __init__(self, parent=None):

        wx.TreeCtrl.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition,
                             wx.DefaultSize, wx.TR_DEFAULT_STYLE)

        db_config = config.datasourse
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            args = ()
            cursor.execute(Sql.model_d_Sql, args)
            record = cursor.fetchall()
        except mysql.connector.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

        root = self.AddRoot('选择模型实验')
        tree = [[0] * len(record)] * len(record)
        i = 0
        node1 = self.AppendItem(root, "model_test_1")
        node2 = self.AppendItem(root, "model_test_2")
        for par in record:
            tree[i] = self.AppendItem(node1, par[0])
            i += 1
        """双击选择模型"""
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.SelectModel)

    def SelectModel(self, event):
        item = self.GetSelection()
        select_name = self.GetItemText(item)
        """不是根节点再进行数据库操作"""
        if self.RootItem != item:
            db_config = config.datasourse
            try:
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor()
                cursor.execute((Sql.get_model_Sql + " '" + select_name + "';"))
                record = cursor.fetchall()
            except mysql.connector.Error as e:
                print(e)
            finally:
                cursor.close()
                conn.close()

            """"得到分布类型"""""
            dtype = record[0][3]
            print(dtype)
            """"得到分布参数"""
            par = record[0][2]
            args = par.split(" ")
            for i in args:
                print(i)
            """"参数名称"""""
            # parname = record[0][4]
            # print(parname)
            """""更新UPSP"""
            showNotebook = ShowNotebook.ShowNotebook()



            showNotebook.ShowArg(record)