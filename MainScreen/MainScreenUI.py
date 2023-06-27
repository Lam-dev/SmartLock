# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_showCamera = QtWidgets.QLabel(self.centralwidget)
        self.label_showCamera.setGeometry(QtCore.QRect(6, 6, 399, 263))
        self.label_showCamera.setText("")
        self.label_showCamera.setObjectName("label_showCamera")
        self.frame_showInputPassword = QtWidgets.QFrame(self.centralwidget)
        self.frame_showInputPassword.setGeometry(QtCore.QRect(418, 0, 384, 480))
        self.frame_showInputPassword.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_showInputPassword.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_showInputPassword.setObjectName("frame_showInputPassword")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
