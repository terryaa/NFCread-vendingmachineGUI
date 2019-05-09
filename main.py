import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize, QTimer, QEventLoop
from PyQt5.QtTest import QTest

# This is our window from QtCreator
import mainwindow_auto


# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    money=0
    timerScreen=QTimer()


    def pressedpushButton_1(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"1")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_2(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"2")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_3(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"3")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_4(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"4")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_5(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"5")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_6(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"6")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_7(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"7")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_8(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"8")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_9(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"9")
        QTest.qWait(10000)
        self.initialize()
    def pressedpushButton_0(self):
        self.lineEdit_money.setText(self.lineEdit_money.text()+"0")
        QTest.qWait(10000)
        self.initialize()

    def pressedreturnButton(self):
        self.lineEdit_money.setText("")

    def pressedInsert(self):
        self.money=int(self.lineEdit_money.text())
        self.lineEdit_money.setText("")

    def pressedInsertDone(self):
        self.lineEdit_money.setText(str(self.money+int(self.lineEdit_money.text())))



    def pressedEsse(self):
        if self.lineEdit_money.text() != '':
            money=int(self.lineEdit_money.text())
            if money >= 4500 :
                money=money-4500
                self.lineEdit_money.setText(str(money))
                self.lineEdit_notice.setText("Esse coming out..!")
            else :
                self.lineEdit_notice.setText("Not Enough Money")
        else :
            self.lineEdit_notice.setText("No Money")

        QTest.qWait(10000)
        self.initialize()

    def pressedMarlboro(self):
        if self.lineEdit_money.text() != '':
            money=int(self.lineEdit_money.text())
            if money >= 5000 :
                money=money-5000
                self.lineEdit_money.setText(str(money))
                self.lineEdit_notice.setText("Marlboro coming out..!")
            else :
                self.lineEdit_notice.setText("Not Enough Money")
        else :
            self.lineEdit_notice.setText("No Money")

        QTest.qWait(10000)
        self.initialize()
    def pressedBohem(self):
        if self.lineEdit_money.text() != '':
            money=int(self.lineEdit_money.text())
            if money >= 4800 :
                money=money-4800
                self.lineEdit_money.setText(str(money))
                self.lineEdit_notice.setText("Bohem Cigar coming out..!")
            else :
                self.lineEdit_notice.setText("Not Enough Money")
        else :
            self.lineEdit_notice.setText("No Money")

        QTest.qWait(10000)
        self.initialize()

    def pressedMevius(self):
        if self.lineEdit_money.text()!='' :
            money=int(self.lineEdit_money.text())
            if money >= 4500 :
                money=money-4500
                self.lineEdit_money.setText(str(money))
                self.lineEdit_notice.setText("Mevius coming out..!")
            else :
                self.lineEdit_notice.setText("Not Enough Money")
        else :
            self.lineEdit_notice.setText("No Money")

        QTest.qWait(10000)
        self.initialize()







    def initialize(self):
        self.lineEdit_notice.setText("Ready..!")






    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        self.pushButton_1.clicked.connect(lambda:self.pressedpushButton_1())
        self.pushButton_2.clicked.connect(lambda: self.pressedpushButton_2())
        self.pushButton_3.clicked.connect(lambda: self.pressedpushButton_3())
        self.pushButton_4.clicked.connect(lambda: self.pressedpushButton_4())
        self.pushButton_5.clicked.connect(lambda: self.pressedpushButton_5())
        self.pushButton_6.clicked.connect(lambda: self.pressedpushButton_6())
        self.pushButton_7.clicked.connect(lambda: self.pressedpushButton_7())
        self.pushButton_8.clicked.connect(lambda: self.pressedpushButton_8())
        self.pushButton_9.clicked.connect(lambda: self.pressedpushButton_9())
        self.pushButton_0.clicked.connect(lambda: self.pressedpushButton_0())

        self.pushButton_return.clicked.connect(lambda: self.pressedreturnButton())

        self.pushButton_select_esse.clicked.connect(lambda: self.pressedEsse())
        self.pushButton_select_marlboro.clicked.connect(lambda: self.pressedMarlboro())
        self.pushButton_selelct_bohem.clicked.connect(lambda: self.pressedBohem())
        self.pushButton_select_mevius.clicked.connect(lambda: self.pressedMevius())

        self.pushButton_insert.clicked.connect(lambda: self.pressedInsert())
        self.pushButton_insert_done.clicked.connect(lambda: self.pressedInsertDone())

        pixmap1=QPixmap('esse.jpeg')
        w=self.label_image_esse.width()
        h=self.label_image_esse.height()
        self.label_image_esse.setPixmap(pixmap1.scaled(w,h,Qt.KeepAspectRatio))

        pixmap2 = QPixmap('marlboro.jpeg')
        w = self.label_image_marlboro.width()
        h = self.label_image_marlboro.height()
        self.label_image_marlboro.setPixmap(pixmap2.scaled(w, h, Qt.KeepAspectRatio))

        pixmap3 = QPixmap('bohem_cigar.png')
        w = self.label_image_bohem.width()
        h = self.label_image_bohem.height()
        self.label_image_bohem.setPixmap(pixmap3.scaled(w, h, Qt.KeepAspectRatio))

        pixmap4 = QPixmap('mevius.png')
        w = self.label_image_mevius.width()
        h = self.label_image_mevius.height()
        self.label_image_mevius.setPixmap(pixmap4.scaled(w, h, Qt.KeepAspectRatio))

        pixmap5 = QPixmap('cigar.png')
        w = self.label_image_logo.width()
        h = self.label_image_logo.height()
        self.label_image_logo.setPixmap(pixmap5.scaled(w, h, Qt.KeepAspectRatio))



        self.initialize()







# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
