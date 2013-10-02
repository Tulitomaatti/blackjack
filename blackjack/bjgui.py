# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        
        editor = QTextEdit()
        
        self.setCentralWidget(editor)

        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+6')
        exitAction.setStatusTip("I'll die if you click me.")
        exitAction.triggered.connect(self.close)

        self.statusBar()


        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)


        menubar = QMenuBar(None)
    #    menubar.setMenuRole(0)


 # #       self.menubar = self.menuBar()

 #        file_menu = menubar.addMenu('&Filde')
 #        file_menu.addAction(exitAction)

 

        menu = self.menuBar()
        filemenu = menu.addMenu('&File')

        #Prevent OS X from abducting the menu item:
        exitAction.setMenuRole(QAction.MenuRole.NoRole)

        filemenu.addAction(exitAction)
        foobarmenu = menu.addMenu('&Foobar')
        # menu.addMenu('&Quiche')
        
        


        self.setGeometry(100,500,400,300)
        self.show()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = MainWindow()
    a.exec_()
    sys.exit()

# # not stylish: 

# class MainWindow(QMainWindow):
#     def __init__(self): 
#         super(MainWindow, self).__init__()
#         self.initUI()

#     def initUI(self):
#         # menus 


#         exitAction = QAction(QIcon('lolcon.png'), '&ExAAAAit', self)

#         # note the +. it's not a -. 
#         exitAction.setShortcut('Ctrl+3')
#         exitAction.setStatusTip('DESTROY ME FOREVER')
#         exitAction.triggered.connect(self.close)

#         # For some reason this fails on os x if '&File' is used. 
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu('&FAILle')
#         fileMenu.addAction(exitAction)

#         # toolbar... with an imaage
#         self.toolbar = self.addToolBar('ExitNAU')
#         self.toolbar.addAction(exitAction)



#         # Do a status bar
#         self.statusBar().showMessage('AAAAA IMMA EXPLODAN!')
#         self.setGeometry(300,300,300,300)
#         self.setWindowTitle('I haz cheezestatusbras. and menu.')


#         # maybe add menus?<
#         # This works on os x. the self. is needed for some reason. 
#         self.help_menu = self.menuBar().addMenu('&File')

#         self.show()



# class MsgBox(QWidget):
#     def __init__(self): 
#         super(MsgBox, self).__init__()
#         self.initUI()

#     def initUI(self):
#         self.setGeometry(300,300,300,200)
#         self.setWindowTitle('Messageboxxxxx')
#         self.show()

#     def closeEvent(self, event):
#         self.center()
#         reply = QMessageBox.question(self, 'Messaaage', 'KILL ME NOW??!', QMessageBox.Yes | QMessageBox.Cancel | QMessageBox.No, QMessageBox.No)

#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()

#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()

#         qr.moveCenter(cp)
#         self.move(qr.topLeft())

# class TooltipExample(QWidget):
#     def __init__(self):
#         super(TooltipExample, self).__init__()

#         self.initUI()

#     def initUI(self):
#         QToolTip.setFont(QFont(u'SansSerif', 10))

#         self.setToolTip(u'lol helppitek<b>stiä</b>')

#         b = QPushButton(u'BUTHAAAN!', self)

#         b.setToolTip(u'BUTHAAN IS A BOTHAAAN!')

#         b.resize(b.sizeHint())
#         b.move(50, 50)

#         self.setGeometry(300,300, 250, 150)
#         self.setWindowTitle(u'Jee tooltippejä')
#         self.show()

# class QuitButton(QWidget):
#     def __init__(self): 
#         super(QuitButton, self).__init__()

#         self.initUI()

#     def initUI(self):
#         b = QPushButton('Quittaa', self)
#         b.clicked.connect(QCoreApplication.instance().quit)
#         b.resize(b.sizeHint())
#         b.move(20,100)

#         self.setGeometry(50,50, 500, 500)
#         self.setWindowTitle('QUITTERUU AAAAAA!!!!')
#         self.show()



# if __name__ == '__main__':

#     app = QApplication(sys.argv)
#   #  ex = TooltipExample()
#   #  ex2 = QuitButton()
#   #  ex3 = MsgBox()
#     ex4 = MainWindow()
#     app.exec_()
#     sys.exit()

# # w = QWidget()


# # w.resize(400,300)
# # w.setWindowTitle('yeahhhh')

# # vbox = QVBoxLayout()
# # l = QLabel('Lolz!')

# # vbox.addWidget(l)

# # w.setLayout(vbox)

# # w.show()


# # sys.exit(app.exec_())

# # Somecodelol.
# # class MainWindow(QWidget):
# #     def __init__(self):
# #         QWidget.__init__(self, None)

# #         vbox = QVBoxLayout()

# #         slidea = QSlider(Qt.Horizontal)
# #         slideb = QSlider(Qt.Horizontal)

# #         vbox.addWidget(slidea)
# #         vbox.addWidget(slideb)

# #      #   self.connect(slidea, SIGNAL("valueChanged(int)"), slideb, SLOT("setValue(int)"))


# #         slidea.valueChanged.connect(slideb.setValue)

# #         self.setLayout(vbox)

# if __name__ == '__main__':
#     application = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     application.exec_()
#     sys.exit()