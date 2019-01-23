#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, \
    QLabel, QComboBox, QCheckBox, QLineEdit, QListView, QMessageBox, QTableWidget, QAbstractItemView, QTableWidgetItem
from PyQt5.QtCore import QStringListModel, Qt

from calc_data import *
from fixed_data import SHISHEN_INFO, YUHUN_INCREASE, INCREASE_LIST


class Window(QWidget):
    def __init__(self):
        """

        :param self:
        """
        super().__init__()
        self.title = '御魂计算器'
        self.left = 10
        self.top = 10
        self.width = 1500
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # choose file
        self.file_path = None
        self.file_button = QPushButton("打开文件...", self)
        self.file_button.resize(480, 30)
        self.file_button.setCheckable(True)
        self.file_button.move(10, 10)
        self.file_button.clicked.connect(self.setFile)

        # initialize input

        # 式神
        self.label_shishen = QLabel(self)
        self.label_shishen.move(20, 50)
        self.label_shishen.setText("式神")
        self.shishen_box = QComboBox(self)
        all_shishen = []
        for shishen, data in SHISHEN_INFO.items():
            all_shishen.append(shishen)
        self.shishen_box.move(80, 37)
        self.shishen_box.resize(140, 50)
        self.shishen_box.addItem("选择你的式神")
        self.shishen_box.addItems(all_shishen)

        # 四件套
        self.label_main_yuhun = QLabel(self)
        self.label_main_yuhun.move(250, 50)
        self.label_main_yuhun.setText("四件套")
        self.main_yuhun_box = QComboBox(self)
        all_yuhun = []
        for yuhun, data in YUHUN_INCREASE.items():
            all_yuhun.append(yuhun)
        self.main_yuhun_box.move(300, 37)
        self.main_yuhun_box.resize(140, 50)
        self.main_yuhun_box.addItem("无")
        self.main_yuhun_box.addItems(all_yuhun)

        # 两件套
        self.label_minor_yuhun = QLabel(self)
        self.label_minor_yuhun.move(480, 50)
        self.label_minor_yuhun.setText("两件套")
        self.minor_yuhun_box = QComboBox(self)
        all_yuhun = []
        for increase in INCREASE_LIST:
            all_yuhun.append(increase)
        for yuhun, data in YUHUN_INCREASE.items():
            all_yuhun.append(yuhun)
        self.minor_yuhun_box.move(530, 37)
        self.minor_yuhun_box.resize(140, 50)
        self.minor_yuhun_box.addItem("无")
        self.minor_yuhun_box.addItems(all_yuhun)

        # 输出only
        self.label_attack_only = QLabel(self)
        self.label_attack_only.move(710, 50)
        self.attack_only_check = QCheckBox("仅限输出御魂", self)
        self.attack_only_check.move(730, 50)

        # 位置
        self.label_position_2 = QLabel(self)
        self.label_position_2.move(20, 90)
        self.label_position_2.setText("二号位主属性：")
        self.attack_2 = QCheckBox(u"攻击加成", self)
        self.attack_2.move(110, 87)
        self.defence_2 = QCheckBox(u"防御加成", self)
        self.defence_2.move(200, 87)
        self.health_2 = QCheckBox(u"生命加成", self)
        self.health_2.move(290, 87)
        self.speed = QCheckBox(u"速度", self)
        self.speed.move(380, 87)

        self.label_position_4 = QLabel(self)
        self.label_position_4.move(20, 130)
        self.label_position_4.setText("四号位主属性：")
        self.attack_4 = QCheckBox(u"攻击加成", self)
        self.attack_4.move(110, 127)
        self.defence_4 = QCheckBox(u"防御加成", self)
        self.defence_4.move(200, 127)
        self.health_4 = QCheckBox(u"生命加成", self)
        self.health_4.move(290, 127)
        self.res = QCheckBox(u"效果抵抗", self)
        self.res.move(380, 127)
        self.hit = QCheckBox(u"效果命中", self)
        self.hit.move(470, 127)

        self.label_position_6 = QLabel(self)
        self.label_position_6.move(20, 170)
        self.label_position_6.setText("六号位主属性：")
        self.attack_6 = QCheckBox(u"攻击加成", self)
        self.attack_6.move(110, 167)
        self.defence_6 = QCheckBox(u"防御加成", self)
        self.defence_6.move(200, 167)
        self.health_6 = QCheckBox(u"生命加成", self)
        self.health_6.move(290, 167)
        self.crit = QCheckBox(u"暴击", self)
        self.crit.move(380, 167)
        self.critdmg = QCheckBox(u"暴击伤害", self)
        self.critdmg.move(470, 167)

        # 目标
        self.target = QLabel(self)
        self.target.move(20, 210)
        self.target.setText("目标属性: ")
        self.target_box = QComboBox(self)
        all_target = ["速度", "攻击x爆伤", "生命x爆伤", "生命", "效果命中", "效果抵抗", "命中抵抗", "暴击"]
        self.target_box.move(100, 198)
        self.target_box.resize(130, 50)
        self.target_box.addItem("选择目标...")
        self.target_box.addItems(all_target)

        self.target_up = QLabel(self)
        self.target_up.move(20, 250)
        self.target_up.setText("上限")
        self.target_line_up = QLineEdit(self)
        self.target_line_up.move(80, 250)
        self.target_line_up.resize(100, 20)

        self.target_low = QLabel(self)
        self.target_low.move(20, 290)
        self.target_low.setText("下限")
        self.target_line_low = QLineEdit(self)
        self.target_line_low.move(80, 290)
        self.target_line_low.resize(100, 20)

        self.target_button = QPushButton(self)
        self.target_button.move(200, 250)
        self.target_button.setText("确认")
        self.target_button.resize(80, 60)
        self.target_button.clicked.connect(self.setRequest)

        self.target_text = QLabel(self)
        self.target_text.move(300, 200)

        self.target_text.setText("单击删除单个")
        self.clear_button = QPushButton(self)
        self.clear_button.move(380, 194)
        self.clear_button.setText("清除全部")
        self.clear_button.clicked.connect(self.clearRequest)

        self.target_list = []
        self.target_listView = QListView(self)
        self.target_listView.move(300, 225)
        self.target_listView.resize(200, 100)
        self.target_listView.clicked.connect(self.listView_clicked)

        # 有效属性选择
        self.effect = QLabel(self)
        self.effect.move(20, 350)
        self.effect.setText("有效属性选择：")
        self.gongji_check = QCheckBox(u"攻击加成", self)
        self.gongji_check.move(110, 347)
        self.shengming_check = QCheckBox(u"生命加成", self)
        self.shengming_check.move(200, 347)
        self.sudu_check = QCheckBox(u"速度", self)
        self.sudu_check.move(290, 347)
        self.baoji_check = QCheckBox(u"暴击", self)
        self.baoji_check.move(380, 347)
        self.baoshang_check = QCheckBox(u"暴击伤害", self)
        self.baoshang_check.move(110, 387)
        self.mingzhong_check = QCheckBox(u"效果命中", self)
        self.mingzhong_check.move(200, 387)
        self.dikang_check = QCheckBox(u"效果抵抗", self)
        self.dikang_check.move(290, 387)

        self.shuju_request_label = QLabel(self)
        self.shuju_request_label.move(480, 350)
        self.shuju_request_label.setText("有效属性: ")
        self.shuju_request_line = QLineEdit(self)
        self.shuju_request_line.move(550, 350)
        self.shuju_request_line.resize(60, 20)

        # 计算
        self.start_button = QPushButton(self)
        self.start_button.setText("开始运算")
        self.start_button.move(480, 390)
        self.start_button.resize(100, 50)
        self.start_button.clicked.connect(self.calculate)

        # 计算数据
        self.shishen_yuhun_set = QLabel(self)
        self.shishen_yuhun_set.move(20, 430)
        self.shishen_yuhun_set.setText("计算数据：")
        self.shishen_table = QTableWidget(self)
        self.shishen_table.setColumnCount(8)
        self.shishen_table.setHorizontalHeaderLabels(["御魂序号", "暴击", "攻击x爆伤", "生命", "生命x爆伤", "速度", "效果抵抗", "效果命中"])
        self.shishen_table.setRowCount(10)
        self.shishen_table.move(20, 470)
        self.shishen_table.resize(830, 400)

        # 已经计算好的式神
        self.ready_sets = []
        self.ready_sets_dict = dict()
        self.ready_set_label = QLabel(self)
        self.ready_set_label.setText("御魂序号: ")
        self.ready_set_label.move(900, 130)
        self.ready_set_line = QLineEdit(self)
        self.ready_set_line.move(960, 130)
        self.set_name_label = QLabel(self)
        self.set_name_label.setText("套装名称: ")
        self.set_name_label.move(900, 170)
        self.set_name_line = QLineEdit(self)
        self.set_name_line.move(960, 170)
        self.add_set_button = QPushButton(self)
        self.add_set_button.setText("记录")
        self.add_set_button.move(1120, 126)
        self.add_set_button.resize(60, 80)
        self.add_set_button.clicked.connect(self.add_set)

        self.listview_title = QLabel(self)
        self.listview_title.setText("套装：")
        self.listview_title.move(900, 210)
        self.sets_listview = QListView(self)
        self.sets_listview.move(960, 220)
        self.sets_listview.resize(300, 200)
        self.sets_listview.clicked.connect(self.sets_clicked)


        #显示套装
        self.show_set_label = QLabel(self)
        self.show_set_label.setText("御魂序号: ")
        self.show_set_label.move(900, 450)
        self.show_set_line = QLineEdit(self)
        self.show_set_line.move(960, 450)
        self.show_set_line.resize(180, 20)
        self.show_set_button = QPushButton(self)
        self.show_set_button.setText("显示")
        self.show_set_button.move(1200, 447)
        self.show_set_button.resize(90, 35)
        self.show_set_button.clicked.connect(self.showSet)

        self.show_set_table = QTableWidget(self)
        self.show_set_table.setColumnCount(6)
        self.show_set_table.setRowCount(6)
        self.show_set_table.setHorizontalHeaderLabels(["一号位", "二号位", "三号位", "四号位", "五号位", "六号位"])
        self.show_set_table.move(900, 500)
        self.show_set_table.resize(500, 300)
        self.show()

    def showSet(self):
        if self.show_set_line.text():
            yuhun_set = self.show_set_line.text().split(', ')
            if len(yuhun_set) == 6 and self.file_path:
                all_data = get_data(self.file_path)
                for yuhun in yuhun_set:
                    data = all_data[int(yuhun)]
                    i = 0
                    for name, num in data.items():
                        if name != "御魂ID" and name != "位置" and name != "御魂等级" and name != "御魂星级":
                            message = name + ": "+ str(num)
                            self.show_set_table.setItem(i, data["位置"] - 1, QTableWidgetItem(str(message)))
                            i += 1

    def sets_clicked(self, qModelIndex):
        clicked_set = self.ready_sets_dict[self.ready_sets[qModelIndex.row()]]
        message = "御魂序号：[" + ','.join(clicked_set) + "], 确认删除吗？"
        reply = QMessageBox.information(self, "确认删除？", message, QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            temp = self.ready_sets[qModelIndex.row()]
            self.ready_sets.remove(temp)
            slm = QStringListModel()
            slm.setStringList(self.ready_sets)
            self.ready_sets_dict.pop(temp, None)
            self.sets_listview.setModel(slm)

    def add_set(self):
        yuhun_set = self.ready_set_line.text()
        yuhun_set_name = self.set_name_line.text()
        if yuhun_set and yuhun_set_name and yuhun_set_name not in self.ready_sets:
            self.ready_sets_dict[yuhun_set_name] = yuhun_set.split(',')
            self.ready_sets.append(yuhun_set_name)
            slm = QStringListModel()
            slm.setStringList(self.ready_sets)
            self.sets_listview.setModel(slm)

    def calculate(self):
        if self.file_path:
            data = get_data(self.file_path)
            if data and self.shishen_box.currentText() != "选择你的式神"\
                    and self.shishen_box.currentText() != u"------SP------"\
                    and self.shishen_box.currentText() != u"-----SSR------"\
                    and self.shishen_box.currentText() != u"-----SR------" \
                    and self.shishen_box.currentText() != u"------R------" \
                    and self.shishen_box.currentText() != u"------N------" :
                t = time.time()
                # remove data in use
                for name, set in self.ready_sets_dict.items():
                    print(name + ":" + str(set) + "is in use")
                    for each in set:
                        data.pop(int(each), None)
                data_loc = get_data_loc(data)
                position_2 = []
                value_2 = []
                position_4 = []
                value_4 = []
                position_6 = []
                value_6 = []
                if self.attack_2.isChecked():
                    position_2.append("攻击加成")
                    value_2.append(55)
                if self.defence_2.isChecked():
                    position_2.append("防御加成")
                    value_2.append(55)
                if self.health_2.isChecked():
                    position_2.append("生命加成")
                    value_2.append(55)
                if self.sudu_check.isChecked():
                    position_2.append("速度")
                    value_2.append(57)
                if self.attack_4.isChecked():
                    position_4.append("攻击加成")
                    value_4.append(55)
                if self.defence_4.isChecked():
                    position_4.append("防御加成")
                    value_4.append(55)
                if self.health_4.isChecked():
                    position_4.append("生命加成")
                    value_4.append(55)
                if self.res.isChecked():
                    position_4.append("效果抵抗")
                    value_4.append(55)
                if self.hit.isChecked():
                    position_4.append("效果命中")
                    value_4.append(55)
                if self.attack_6.isChecked():
                    position_6.append("攻击加成")
                    value_6.append(55)
                if self.defence_6.isChecked():
                    position_6.append("防御加成")
                    value_6.append(55)
                if self.health_6.isChecked():
                    position_6.append("生命加成")
                    value_6.append(55)
                if self.crit.isChecked():
                    position_6.append("暴击")
                    value_6.append(55)
                if self.critdmg.isChecked():
                    position_6.append("暴击伤害")
                    value_6.append(89)

                effective_list = [self.baoshang_check.isChecked(), self.baoshang_check.isChecked(),
                                  self.gongji_check.isChecked(), self.sudu_check.isChecked(),
                                  self.shengming_check.isChecked(), self.dikang_check.isChecked(),
                                  self.mingzhong_check.isChecked()]

                effective_num = 0
                if self.shuju_request_line.text():
                    effective_num = int(self.shuju_request_line.text())
                filter_data_loc = filter_all(data_loc, position_2, value_2, position_4, value_4, position_6, value_6,
                                             effective_list, effective_num, self.attack_only_check.isChecked(), 0)
                yuhun_filter = {}
                if self.main_yuhun_box.currentText() != "无":
                    yuhun_filter[self.main_yuhun_box.currentText()] = 4
                if self.minor_yuhun_box.currentText() != "无":
                    if self.minor_yuhun_box.currentText() != self.main_yuhun_box.currentText():
                        yuhun_filter[self.minor_yuhun_box.currentText()] = 2
                    else:
                        yuhun_filter[self.main_yuhun_box.currentText()] = 6
                combo, num = form_all_combs(filter_data_loc, yuhun_filter)
                shishen_data = SHISHEN_INFO[self.shishen_box.currentText()]
                filter_rules = dict()
                for item in self.target_list:
                    yuhun_result = [x.strip() for x in item.split(',')]
                    yuhun_result[1] = yuhun_result[1][5:]
                    yuhun_result[2] = yuhun_result[2][4:]
                    temp = dict()
                    temp["up"] = float(yuhun_result[2])
                    temp["low"] = float(yuhun_result[1])
                    name = yuhun_result[0]
                    filter_rules[name] = temp
                yuhun_result = filter_combo(combo, shishen_data, filter_rules)
                self.shishen_table.setRowCount(len(yuhun_result))
                i = 0
                for item in yuhun_result:
                    xuhao = item[u"combo"]
                    baoji = item[u"暴击"]
                    gongbao = item[u"攻击x爆伤"]
                    shengming = item[u"总生命"]
                    shengbao = item[u"生命x爆伤"]
                    sudu = item[u"速度"]
                    dikang = item[u"式神抵抗"]
                    mingzhong = item[u"式神命中"]

                    self.shishen_table.setItem(i, 0, QTableWidgetItem(', '.join(str(e) for e in xuhao)))
                    self.shishen_table.setItem(i, 1, QTableWidgetItem(str(baoji)))
                    self.shishen_table.setItem(i, 2, QTableWidgetItem(str(gongbao)))
                    self.shishen_table.setItem(i, 3, QTableWidgetItem(str(shengming)))
                    self.shishen_table.setItem(i, 4, QTableWidgetItem(str(shengbao)))
                    self.shishen_table.setItem(i, 5, QTableWidgetItem(str(sudu)))
                    self.shishen_table.setItem(i, 6, QTableWidgetItem(str(dikang)))
                    self.shishen_table.setItem(i, 7, QTableWidgetItem(str(mingzhong)))
                    i += 1
                used_time = time.time() - t
                print("Calculating took: ", used_time, " seconds")

    def listView_clicked(self, qModelIndex):
        reply = QMessageBox.information(self, "确认删除？", "确认删除选定项吗", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            temp = self.target_list[qModelIndex.row()]
            self.target_list.remove(temp)
            slm = QStringListModel()
            slm.setStringList(self.target_list)
            self.target_listView.setModel(slm)

    def setRequest(self):
        text = self.target_box.currentText()
        low = self.target_line_low.text()
        up = self.target_line_up.text()
        if not low:
            low = '0'
        if not up:
            up = '30000'
        temp_string = text + ",low: " + low + ",up: " + up
        # have to be unique
        if temp_string in self.target_list:
            return
        if text == "选择目标...":
            return
        self.target_list.append(temp_string)
        slm = QStringListModel()
        slm.setStringList(self.target_list)
        self.target_listView.setModel(slm)

    def clearRequest(self):
        self.target_list = []
        slm = QStringListModel()
        slm.setStringList(self.target_list)
        self.target_listView.setModel(slm)
        return

    def setFile(self):
        if (self.file_button.isChecked()):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                      "All Files (*);;Python Files (*.py)", options=options)
            self.file_path = fileName
            self.file_button.setText(self.file_path)
        else:
            self.file_button.setText("打开文件...")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
