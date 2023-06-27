from PyQt5.QtCore  import QObject
from CheckPassword.CheckPasswordUI  import  Ui_Frame
from PyQt5.QtWidgets  import  QPushButton
class CheckPassword(QObject, Ui_Frame):
    def __init__(self, Frame):
        QObject.__init__(self)
        Ui_Frame.__init__(self)
        self.__frameContain = Frame
        self.setupUi(self.__frameContain)
        self.__lstButton = []
        self.__ShowButtonMatrix()

    def __ShowButtonMatrix(self):
        for i in range(0, 12):
            self.__lstButton.append(self.__CreateAbutton(i))
        
    def __CreateAbutton(self, value, isControlButton = False):
        
        button = QPushButton(self.__frameContain)
        button.setStyleSheet('background-color: rgb(255, 255, 255);border-style:solid;border-width:2px;border-color: rgb(52, 101, 164);border-radius:7px;font: 75 bold 32pt "Arial";color: rgb(52, 101, 164);')
        if(value == 0): 
            row = 3
            column = 1
            button.setText('0')
        else:
            value -= 1
            row = int(value / 3)
            column = value % 3
            if(value == 9):
                button.setText('C')
            elif(value == 10):
                row = 3
                column = 2
                button.setText("OK")
            else:
                
                button.setText(str(value + 1))
        button.setGeometry(column*90+(column+1)*10, row*90+(row+1)*10,90, 90)
        return button
    
   