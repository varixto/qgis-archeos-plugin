# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/pyarchinit/.qgis/python/plugins/pyarchinit/modules/gui/pyarchinit_Periodo_fase_ui.ui'
#
# Created: Thu Jan 28 21:26:01 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 595)
        Dialog.setMinimumSize(QtCore.QSize(540, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/iconSite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_9 = QtGui.QGridLayout(Dialog)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_29 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.pushButton_connect = QtGui.QPushButton(Dialog)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.gridLayout_2.addWidget(self.pushButton_connect, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_first_rec = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/5_leftArrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon1)
        self.pushButton_first_rec.setObjectName("pushButton_first_rec")
        self.gridLayout.addWidget(self.pushButton_first_rec, 0, 0, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/4_leftArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon2)
        self.pushButton_prev_rec.setObjectName("pushButton_prev_rec")
        self.gridLayout.addWidget(self.pushButton_prev_rec, 0, 1, 1, 2)
        self.pushButton_next_rec = QtGui.QPushButton(Dialog)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/6_rightArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon3)
        self.pushButton_next_rec.setObjectName("pushButton_next_rec")
        self.gridLayout.addWidget(self.pushButton_next_rec, 0, 4, 1, 1)
        self.pushButton_last_rec = QtGui.QPushButton(Dialog)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/7_rightArrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon4)
        self.pushButton_last_rec.setObjectName("pushButton_last_rec")
        self.gridLayout.addWidget(self.pushButton_last_rec, 0, 5, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/newrec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon5)
        self.pushButton_new_rec.setObjectName("pushButton_new_rec")
        self.gridLayout.addWidget(self.pushButton_new_rec, 0, 6, 1, 1)
        self.pushButton_save = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/b_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon6)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 0, 7, 1, 1)
        self.pushButton_delete = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon7)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(70, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/new_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon8)
        self.pushButton_new_search.setObjectName("pushButton_new_search")
        self.gridLayout.addWidget(self.pushButton_new_search, 1, 4, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon9)
        self.pushButton_search_go.setObjectName("pushButton_search_go")
        self.gridLayout.addWidget(self.pushButton_search_go, 1, 5, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon10)
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.gridLayout.addWidget(self.pushButton_sort, 1, 6, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/view_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon11)
        self.pushButton_view_all.setObjectName("pushButton_view_all")
        self.gridLayout.addWidget(self.pushButton_view_all, 1, 7, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_42 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_42.setFont(font)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setObjectName("label_42")
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_43 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setMargin(0)
        self.label_43.setObjectName("label_43")
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_status = QtGui.QLabel(Dialog)
        self.label_status.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_status.setFont(font)
        self.label_status.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_status.setMouseTracking(False)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setMargin(0)
        self.label_status.setObjectName("label_status")
        self.gridLayout_4.addWidget(self.label_status, 1, 0, 1, 1)
        self.label_sort = QtGui.QLabel(Dialog)
        self.label_sort.setMinimumSize(QtCore.QSize(40, 0))
        self.label_sort.setSizeIncrement(QtCore.QSize(40, 0))
        self.label_sort.setBaseSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_sort.setFont(font)
        self.label_sort.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_sort.setMouseTracking(False)
        self.label_sort.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sort.setFrameShape(QtGui.QFrame.Box)
        self.label_sort.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sort.setMargin(0)
        self.label_sort.setObjectName("label_sort")
        self.gridLayout_4.addWidget(self.label_sort, 1, 1, 1, 1)
        self.label_34 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setMargin(0)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_27 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setMargin(0)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_rec_corrente = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.label_rec_corrente.setFont(font)
        self.label_rec_corrente.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_corrente.setMouseTracking(False)
        self.label_rec_corrente.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_corrente.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_corrente.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_corrente.setObjectName("label_rec_corrente")
        self.gridLayout_3.addWidget(self.label_rec_corrente, 0, 1, 1, 1)
        self.label_28 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setMargin(0)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_rec_tot = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.label_rec_tot.setFont(font)
        self.label_rec_tot.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_tot.setMouseTracking(False)
        self.label_rec_tot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_tot.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_tot.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_tot.setObjectName("label_rec_tot")
        self.gridLayout_3.addWidget(self.label_rec_tot, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_8 = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.comboBox_sito = QtGui.QComboBox(Dialog)
        self.comboBox_sito.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_sito.setFont(font)
        self.comboBox_sito.setMouseTracking(True)
        self.comboBox_sito.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_sito.setEditable(True)
        self.comboBox_sito.setMaxVisibleItems(99999)
        self.comboBox_sito.setMaxCount(2147483647)
        self.comboBox_sito.setFrame(False)
        self.comboBox_sito.setObjectName("comboBox_sito")
        self.comboBox_sito.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_sito, 0, 0, 3, 5)
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 3, 0, 1, 1)
        self.comboBox_periodo = QtGui.QComboBox(Dialog)
        self.comboBox_periodo.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_periodo.setFont(font)
        self.comboBox_periodo.setAutoFillBackground(False)
        self.comboBox_periodo.setEditable(True)
        self.comboBox_periodo.setMaxVisibleItems(15)
        self.comboBox_periodo.setMaxCount(15)
        self.comboBox_periodo.setObjectName("comboBox_periodo")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.comboBox_periodo.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_periodo, 4, 0, 1, 1)
        self.comboBox_fase = QtGui.QComboBox(Dialog)
        self.comboBox_fase.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_fase.setFont(font)
        self.comboBox_fase.setEditable(True)
        self.comboBox_fase.setObjectName("comboBox_fase")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.comboBox_fase.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_fase, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 5, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 3, 0, 1, 2)
        self.line_10 = QtGui.QFrame(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_10.setFont(font)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_6.addWidget(self.line_10, 4, 0, 2, 4)
        self.label_38 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.gridLayout_6.addWidget(self.label_38, 9, 0, 1, 1)
        self.lineEdit_cron_iniz = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cron_iniz.setFont(font)
        self.lineEdit_cron_iniz.setObjectName("lineEdit_cron_iniz")
        self.gridLayout_6.addWidget(self.lineEdit_cron_iniz, 10, 0, 1, 1)
        self.label_37 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_6.addWidget(self.label_37, 11, 0, 1, 1)
        self.label_14 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 11, 1, 1, 1)
        self.textEdit_descrizione_per = QtGui.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_descrizione_per.setFont(font)
        self.textEdit_descrizione_per.setObjectName("textEdit_descrizione_per")
        self.gridLayout_6.addWidget(self.textEdit_descrizione_per, 2, 0, 1, 4)
        self.lineEdit_cron_fin = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_cron_fin.setFont(font)
        self.lineEdit_cron_fin.setObjectName("lineEdit_cron_fin")
        self.gridLayout_6.addWidget(self.lineEdit_cron_fin, 10, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(38, 19, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 10, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 10, 3, 1, 1)
        self.label_13 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_per_estesa = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_per_estesa.setFont(font)
        self.lineEdit_per_estesa.setObjectName("lineEdit_per_estesa")
        self.gridLayout_8.addWidget(self.lineEdit_per_estesa, 0, 0, 1, 2)
        self.label_25 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_8.addWidget(self.label_25, 1, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(418, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "pyArchInit Gestione Scavi - Periodizzazione di scavo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Dialog", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(QtGui.QApplication.translate("Dialog", "Reload DB", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setToolTip(QtGui.QApplication.translate("Dialog", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setToolTip(QtGui.QApplication.translate("Dialog", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setToolTip(QtGui.QApplication.translate("Dialog", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setToolTip(QtGui.QApplication.translate("Dialog", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setToolTip(QtGui.QApplication.translate("Dialog", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setToolTip(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setToolTip(QtGui.QApplication.translate("Dialog", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setToolTip(QtGui.QApplication.translate("Dialog", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setToolTip(QtGui.QApplication.translate("Dialog", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setToolTip(QtGui.QApplication.translate("Dialog", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setToolTip(QtGui.QApplication.translate("Dialog", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Dialog", "DB Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("Dialog", "Ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("Dialog", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("Dialog", "record n.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_corrente.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Dialog", "record tot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_tot.setText(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sito.setItemText(0, QtGui.QApplication.translate("Dialog", "Inserisci un valore", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Sito", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(0, QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(1, QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(2, QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(3, QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(4, QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(5, QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(6, QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(7, QtGui.QApplication.translate("Dialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(8, QtGui.QApplication.translate("Dialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(9, QtGui.QApplication.translate("Dialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(10, QtGui.QApplication.translate("Dialog", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(11, QtGui.QApplication.translate("Dialog", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_periodo.setItemText(12, QtGui.QApplication.translate("Dialog", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(0, QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(1, QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(2, QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(3, QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(4, QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(5, QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(6, QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(7, QtGui.QApplication.translate("Dialog", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(8, QtGui.QApplication.translate("Dialog", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(9, QtGui.QApplication.translate("Dialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(10, QtGui.QApplication.translate("Dialog", "11", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(11, QtGui.QApplication.translate("Dialog", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(12, QtGui.QApplication.translate("Dialog", "13", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(13, QtGui.QApplication.translate("Dialog", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_fase.setItemText(14, QtGui.QApplication.translate("Dialog", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Fase", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Periodo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Descrizione ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("Dialog", "Cronologia ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_cron_iniz.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("Dialog", "Iniziale ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog", "Finale ", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_cron_fin.setText(QtGui.QApplication.translate("Dialog", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "Dati descrittivi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Dialog", "Estesa letterale ", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
