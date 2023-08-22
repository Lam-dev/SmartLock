from PyQt5.QtCore  import QObject
from CheckPassword.CheckPasswordUI  import  Ui_Frame
from PyQt5.QtWidgets  import  QPushButton
from PyQt5.QtCore     import QPropertyAnimation, QTimer, pyqtSignal
from PyQt5 import       QtCore
from DatabaseAccess.TableEntities  import  *
class CheckPassword(QObject, Ui_Frame):
    SignalPasswordCorrect = pyqtSignal()
    def __init__(self, Frame):
        QObject.__init__(self)
        Ui_Frame.__init__(self)
        self.__frameContain = Frame
        self.setupUi(self.__frameContain)
        self.__lstButton = []
        self.__ShowButtonMatrix()
        self.__timerAnim = QTimer(self)
        self.__timerAnim.timeout.connect(self.StartAnimation)
        self.__timerAnim.start(2000)
        self.__paswordInput = ""
        self.__listPassword = PasswordRepo().GetListAllColumn('1=1')

    def StartAnimation(self):
        self.__timerAnim.stop()
        for btn in self.__lstButton:
            btn.StartAnimation()

    def __ShowButtonMatrix(self):
        for i in range(0, 12):
            btnObj = ButtonObj(i, self.frame_ShowKeyBoard)
            self.__lstButton.append(btnObj)
            btnObj.SignalButtonClicked.connect(self.__ButtonClicked)

    def __ButtonClicked(self, number):
        if(number <= 9):
            if(len(self.__paswordInput)< 6):
                self.__paswordInput += str(number)
                self.__ComparePassword()
                self.label_showPass.setText('*'*len(self.__paswordInput))
        elif(number == 10):
            self.__paswordInput= ''
            self.label_showPass.setText('*'*len(self.__paswordInput))

    def __ComparePassword(self):
        if(self.__listPassword[0].Password == self.__paswordInput):
            self.SignalPasswordCorrect.emit()
            print("password ok:", self.__paswordInput)

class ButtonObj(QObject):
    SignalButtonClicked =  pyqtSignal(int)
    def __init__(self, number, frame):
        QObject.__init__(self)
        self.__frameContain = frame
        self.__CreateAbutton(number)
        self.__number = number
        self.__button.clicked.connect(lambda:self.SignalButtonClicked.emit(self.__number))
        self.___currentPosition = None

    def StartAnimation(self):
        self.__animation.start()

    def __CreateAbutton(self, value, isControlButton = False):
        self.__button = QPushButton(self.__frameContain)
        self.__button.setStyleSheet('background-color: rgb(255, 255, 255);border-style:solid;border-width:2px;border-color: rgb(52, 101, 164);border-radius:7px;font: 75 bold 32pt "Arial";color: rgb(52, 101, 164);')
        if(value == 0): 
            row = 3
            column = 1
            self.__button.setText('0')
        else:
            value -= 1
            row = int(value / 3)
            column = value % 3
            if(value == 9):
                self.__button.setText('C')
            elif(value == 10):
                row = 3
                column = 2
                self.__button.setText("OK")
            else:
                
                self.__button.setText(str(value + 1))
        self.__button.setGeometry(-100, -100, 80, 80)
        self.__animation = QPropertyAnimation(self.__button, b"geometry")
        self.__animation.setDuration(300)
        self.__animation.setStartValue(QtCore.QRect(-100, -100, 80, 80))
        self.__animation.setEndValue(QtCore.QRect(column*80+(column+1)*8, row*80+(row+1)*8, 80, 80))
        self.__currentPosition = QtCore.QRect(column*80+(column+1)*8, row*80+(row+1)*8, 80, 80)

    def ChangePosition(self, geometry):
        self.__animation.setStartValue(self.__currentPosition)
        self.__animation.setEndValue(geometry)
        self.__currentPosition = geometry
