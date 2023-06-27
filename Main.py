from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore  import QObject
from MainScreen.MainScreenUI  import   Ui_MainWindow
from CheckPassword.CheckPassword  import CheckPassword
class Main(Ui_MainWindow, QObject):
    def __init__(self, mainWindows):
        Ui_MainWindow.__init__(self)
        QObject.__init__(self)
        self.setupUi(mainWindows)
        self.__checkPassword = CheckPassword(self.frame_showInputPassword)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main = Main(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())