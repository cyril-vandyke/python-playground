# structure.py
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PlayerSelection(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        self.playerList = ["Andrew","Cyril","Flank","Grant","Shane","Weston"]        
        self.p1_group = QButtonGroup(self)
        self.p2_group = QButtonGroup(self)
        self.p3_group = QButtonGroup(self)
        self.p4_group = QButtonGroup(self)
        self.groupList = [self.p1_group,self.p2_group,self.p3_group,self.p4_group]

        p1label = QLabel("Player 1")
        p2label = QLabel("Player 2")
        p3label = QLabel("Player 3")
        p4label = QLabel("Player 4")

        for i in range(0,4):
            for j in range(len(self.playerList)):
                var = QRadioButton(self.playerList[j])
                self.groupList[i].addButton(var)
                layout.addWidget(var, 1+j, i)
                
        layout.addWidget(p1label, 0,0)
        layout.addWidget(p2label, 0,1)
        layout.addWidget(p3label, 0,2)
        layout.addWidget(p4label, 0,3)

        self.p1_group.buttonClicked['QAbstractButton *'].connect(self.button_clicked1)
        self.p2_group.buttonClicked['QAbstractButton *'].connect(self.button_clicked2)
        self.p3_group.buttonClicked['QAbstractButton *'].connect(self.button_clicked3)
        self.p4_group.buttonClicked['QAbstractButton *'].connect(self.button_clicked4)
        self.setLayout(layout)

    def button_clicked(self, button, fileName):
        f = open(fileName,'w')
        f.write(button.text())
        f.close()

    def button_clicked1(self, button):
        self.button_clicked(button,"p1.txt")
    def button_clicked2(self, button):
        self.button_clicked(button,"p2.txt")
    def button_clicked3(self, button):
        self.button_clicked(button,"p3.txt")
    def button_clicked4(self, button):
        self.button_clicked(button,"p4.txt")

       


app = QApplication(sys.argv)
dialog = PlayerSelection()
dialog.setWindowTitle("Player Selector")
dialog.setWindowIcon(QIcon('icon.png'))
dialog.show()
app.exec_()