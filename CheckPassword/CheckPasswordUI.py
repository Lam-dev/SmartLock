# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckPassword.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(272, 480)
        self.label_showPass = QtWidgets.QLabel(Frame)
        self.label_showPass.setGeometry(QtCore.QRect(0, 14, 272, 73))
        self.label_showPass.setStyleSheet("font: 75 75px \"Ubuntu\";\n"
"color: rgb(32, 74, 135);\n"
"")
        self.label_showPass.setText("")
        self.label_showPass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_showPass.setObjectName("label_showPass")
        self.frame_ShowKeyBoard = QtWidgets.QFrame(Frame)
        self.frame_ShowKeyBoard.setGeometry(QtCore.QRect(0, 92, 272, 387))
        self.frame_ShowKeyBoard.setStyleSheet("background-color: rgba(0, 15, 177, 0);")
        self.frame_ShowKeyBoard.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ShowKeyBoard.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ShowKeyBoard.setObjectName("frame_ShowKeyBoard")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
