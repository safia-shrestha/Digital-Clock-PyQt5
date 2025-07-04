# Python PyQt5 Digital Clock
import sys #sys means system this module provides variables used and maintained by python interpreter 
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout  #widgets are building blockes of gui application 
from PyQt5.QtCore import QTimer,QTime,Qt 
#QtCore module provides functionality not related to gui components here is where we will get timer to keep track of the time 
# Qt is for alinement  
from PyQt5.QtGui import QFont,QFontDatabase 

class DigitalClock(QWidget): 
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self) #this label that displays the time 
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)


        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color:black;")

        font_id=QFontDatabase.addApplicationFont("C:\\Users\\ACER\\OneDrive\\Documents\\Home Python\\Digital Clock PyQt5\\DS-DIGIT.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family,150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time) 
        # with timer we need to trigger timeout signal every 1000 milliseconds  every sec that is and to handle that we take our timer 
        self.timer.start(1000)
#we need ttf file true type font 
        self.update_time()


    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP") #A=anteridium and P=Post meridian 
        self.time_label.setText(current_time)
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_()) #it is execute method


