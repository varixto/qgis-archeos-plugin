# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/pyarchinit/.qgis/python/plugins/pyarchinit/modules/gui/Ui_pyarchinitConfig.ui'
#
# Created: Thu Jan 28 21:25:50 2010
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog_Config(object):
    def setupUi(self, Dialog_Config):
        Dialog_Config.setObjectName("Dialog_Config")
        Dialog_Config.setWindowModality(QtCore.Qt.NonModal)
        Dialog_Config.setEnabled(True)
        Dialog_Config.resize(450, 279)
        Dialog_Config.setMinimumSize(QtCore.QSize(450, 279))
        Dialog_Config.setMaximumSize(QtCore.QSize(450, 279))
        Dialog_Config.setCursor(QtCore.Qt.PointingHandCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/iconConn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Config.setWindowIcon(icon)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_Config)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(Dialog_Config)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 351, 218))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_Database = QtGui.QComboBox(self.layoutWidget)
        self.comboBox_Database.setEnabled(True)
        self.comboBox_Database.setMouseTracking(False)
        self.comboBox_Database.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_Database.setAcceptDrops(False)
        self.comboBox_Database.setEditable(True)
        self.comboBox_Database.setDuplicatesEnabled(False)
        self.comboBox_Database.setFrame(True)
        self.comboBox_Database.setObjectName("comboBox_Database")
        self.comboBox_Database.addItem("")
        self.comboBox_Database.addItem("")
        self.gridLayout.addWidget(self.comboBox_Database, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_Host = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Host.setObjectName("lineEdit_Host")
        self.gridLayout.addWidget(self.lineEdit_Host, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_Port = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Port.setObjectName("lineEdit_Port")
        self.gridLayout.addWidget(self.lineEdit_Port, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_DBname = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_DBname.setObjectName("lineEdit_DBname")
        self.gridLayout.addWidget(self.lineEdit_DBname, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_User = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_User.setObjectName("lineEdit_User")
        self.gridLayout.addWidget(self.lineEdit_User, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.lineEdit_Password = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_Password.setText("\'\'")
        self.lineEdit_Password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.gridLayout.addWidget(self.lineEdit_Password, 5, 1, 1, 1)
        self.pushButton_save = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_save.setCheckable(False)
        self.pushButton_save.setAutoDefault(True)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 6, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 381, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.pushButton_crea_database = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_crea_database.setObjectName("pushButton_crea_database")
        self.gridLayout_3.addWidget(self.pushButton_crea_database, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.pushButton_crea_layer = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_crea_layer.setObjectName("pushButton_crea_layer")
        self.gridLayout_3.addWidget(self.pushButton_crea_layer, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.pushButton_crea_db_sqlite = QtGui.QPushButton(self.layoutWidget1)
        self.pushButton_crea_db_sqlite.setObjectName("pushButton_crea_db_sqlite")
        self.gridLayout_3.addWidget(self.pushButton_crea_db_sqlite, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog_Config)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Config)
        Dialog_Config.setTabOrder(self.comboBox_Database, self.lineEdit_Host)
        Dialog_Config.setTabOrder(self.lineEdit_Host, self.lineEdit_Port)
        Dialog_Config.setTabOrder(self.lineEdit_Port, self.lineEdit_DBname)
        Dialog_Config.setTabOrder(self.lineEdit_DBname, self.lineEdit_User)
        Dialog_Config.setTabOrder(self.lineEdit_User, self.lineEdit_Password)

    def retranslateUi(self, Dialog_Config):
        Dialog_Config.setWindowTitle(QtGui.QApplication.translate("Dialog_Config", "Impostazioni del sistema", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Config", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_Database.setItemText(0, QtGui.QApplication.translate("Dialog_Config", "postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_Database.setItemText(1, QtGui.QApplication.translate("Dialog_Config", "sqlite", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_Config", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_Host.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog_Config", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_Port.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_Config", "DBname", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_DBname.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_Config", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_User.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog_Config", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("Dialog_Config", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog_Config", "Parametri di connessione", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog_Config", "Installa il database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_crea_database.setText(QtGui.QApplication.translate("Dialog_Config", "Installa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog_Config", "Installa il db geografico su Postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_crea_layer.setText(QtGui.QApplication.translate("Dialog_Config", "Installa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog_Config", "Installa il db geografico su sqlite", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_crea_db_sqlite.setText(QtGui.QApplication.translate("Dialog_Config", "Installa", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog_Config", "Installazione layers", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc