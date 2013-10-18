# -*- coding: utf-8 -*-

# Going through zetcode tutorials before doing anything real for the blackjack.

# For blackjack: 

# A QPixMap in a QLabel could be used for images/cards.
# label.setPixmap(pixmap)

# QPushButton for hit/stand/double connected to suitable actions.

# Dialog with a QLineEdit for getting new player names. 
# QListView for existing players

# Menus... for menus. Not much there anyways. 




from PySide.QtCore import *
from PySide.QtGui import *

import cardpackhand as cph
import game as g

import sys


class CardLabel(QLabel):
    def __init__(self, card): 
        super(CardLabel, self).__init__()


        self.labelstring =  str(card.number) + "\n" + str(card.suit) 
        self.setText(self.labelstring + "\n\n\n")

        f = self.font()
        f.setPointSize(20)
        p = QPalette()
        p.setColor(QPalette.Background, Qt.white)

        self.setAutoFillBackground(True)
        self.setFont(f)
        self.setPalette(p)

        self.setFrameStyle(QFrame.Box | QFrame.Raised)
        self.setLineWidth(2)

    #    self.setSizePolicy(QSizePolicy())
        self.setFixedSize(100,150)


class CardArea(QFrame):
    def __init__(self): 
        super(CardArea, self).__init__()


        foo = CardLabel(cph.Card(8, "spade"))

        self.dealer_hand_layout = QHBoxLayout()
        self.player_hand_layout = QHBoxLayout()
        self.dealer_hand_layout.setAlignment(Qt.AlignLeft)
        self.player_hand_layout.setAlignment(Qt.AlignLeft)

        dealer_label = QLabel("Dealer's hand:")
        player_label = QLabel("Player's hand:")

        vbox = QVBoxLayout()
        vbox.addWidget(dealer_label)
        vbox.addLayout(self.dealer_hand_layout)
        vbox.addWidget(player_label)
        vbox.addLayout(self.player_hand_layout)


        self.setLayout(vbox)


class StatusArea(QWidget):
    def __init__(self): 
        super(StatusArea, self).__init__()
        vbox = QVBoxLayout()
        player_status = QLabel("Player status: ")
        dealer_status = QLabel("Dealer status: ")

        vbox.addWidget(player_status)
        vbox.addWidget(dealer_status)

        self.setLayout(vbox)

class ActionController(object):
    def __init__(self, parent=None): 
        self.parent = parent

    def hit(self):
        print "hitting"

    def double(self):
        print "doubling"

    def stand(self):
        print "standing"

    def next_round(self):
        print "next round start please."

    def quit_to_menu(self):
        print "Quitting to main menu"

class GameArea(QWidget):
    def __init__(self): 
        super(GameArea, self).__init__()

        self.initUI()

    # def controller(self):
    #     sys.exit()

    def initUI(self):

        self.ctl = ActionController(self)
        card_area = CardArea()
        status = StatusArea()

        hit_button = QPushButton("Hit")
        double_button = QPushButton("Double")
        stand_button = QPushButton("Stand")
        next_round_button = QPushButton("Play next round")
        quit_to_menu_button = QPushButton("Quit to Main menu")
        # split_button = QPushButton("Split", self)
        # insurance_button = QPushButton("Insurance", self)

        hit_button.clicked.connect(self.ctl.hit)
        double_button.clicked.connect(self.ctl.double)
        stand_button.clicked.connect(self.ctl.stand)
        next_round_button.clicked.connect(self.ctl.next_round)
        quit_to_menu_button.clicked.connect(self.ctl.quit_to_menu)


        action_buttons_layout = QHBoxLayout()
        action_buttons_layout.addWidget(hit_button)
        action_buttons_layout.addWidget(double_button)
        action_buttons_layout.addWidget(stand_button)
        action_buttons_layout.addStretch(1)

        menu_buttons_layout = QHBoxLayout()
        menu_buttons_layout.addWidget(next_round_button)
        menu_buttons_layout.addWidget(quit_to_menu_button)
        menu_buttons_layout.addStretch(1)

        card_area_layout = QHBoxLayout()
        card_area_layout.addWidget(card_area)
        card_area_layout.addStretch(1)

    #    quit_to_menu_button.hide()
        next_round_button.setEnabled(False)


        vbox = QVBoxLayout()

        vbox.addLayout(card_area_layout)
        vbox.addLayout(action_buttons_layout)
        vbox.addWidget(status)
        vbox.addLayout(menu_buttons_layout)

        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(80, 80, 300, 300)


        # We can now add cards to the table 
        card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(4, "heart")))
        # card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(5, "gay")))
        card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(45, "dragon")))

        card_area.player_hand_layout.addWidget(CardLabel(cph.Card(3, "lol")))
        # card_area.player_hand_layout.addWidget(CardLabel(cph.Card(6, "asdf")))

        self.setWindowTitle('Blackjack')
        self.show()
        

if __name__ == '__main__':
    a = QApplication(sys.argv)
    w = GameArea()
    a.exec_()
    sys.exit()


# class Boxlayout(QWidget):
#     def __init__(self):
#         super(Boxlayout, self).__init__()
        
#         self.initUI()
        
#     def initUI(self):      
#         a = QListView(self)
#         model = QStandardItemModel()

#         for i in xrange(10):
#             item = QStandardItem()
#             item.setText('aaaa' + str(i) + 'asdf') 

#             item.setCheckable(True)

#             model.appendRow(item)

#         a.setModel(model)
        

#         self.show()







# simple signal.
    #     a = QPushButton('Butan 1', self)
    #     a.move(30,50)

    #     b = QPushButton('butan2', self)
    #     b.move(150,50)

       
     


    #     a.clicked.connect(self.buttonClicked)
    #     b.clicked.connect(self.buttonClicked)  



    #     self.show()

    # def buttonClicked(self):

    #     sender = self.sender()

    #     self.statusBar().showMessage(sender.text() + ' prebbes.') 




# # Simple way to handle key pressed event for a window:
#     def keyPressEvent(self, e):
#         if e.key() == Qt.Key_Escape:
#             self.close()

#more grid    
        # title = QLabel('Title')
        # author = QLabel('le maker')
        # review = QLabel('arvosteldus')

        # title_edit = QLineEdit()
        # author_edit = QLineEdit()
        # review_edit = QTextEdit()

        # grid = QGridLayout()
        # grid.setSpacing(10)

        # grid.addWidget(title, 1, 0)
        # grid.addWidget(title_edit, 1, 1)

        # grid.addWidget(author, 2, 0)
        # grid.addWidget(author_edit, 2, 1)

        # grid.addWidget(review, 3,0)
        # grid.addWidget(review_edit, 3,1, 5, 1)

        # self.setLayout(grid)

        # self.show()



# # Grid layotu
#         names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
#                 '4', '5', '6', '*', '1', '2', '3', '-',
#                 '0', '.', '=', '+']

#         grid = QGridLayout()

#         j = i = 0

#         pos = [(0, 0), (0, 1), (0, 2), (0, 3),
#                 (1, 0), (1, 1), (1, 2), (1, 3),
#                 (2, 0), (2, 1), (2, 2), (2, 3),
#                 (3, 0), (3, 1), (3, 2), (3, 3),
#                 (4, 0), (4, 1), (4, 2), (4, 3)]

#         for i in names:
#             button = QPushButton(i)
#             if j == 2:
#                 grid.addWidget(QLabel(''), 0, 2)
#             else: 
#                 grid.addWidget(button, pos[j][0], pos[j][1])
#             j += 1

#         self.setLayout(grid)
#         self.setWindowTitle('lol calculador')
#         self.show()

# box lyaout

        # butan = QPushButton('HITME')
        # diebutan = QPushButton('DIE PIE!')
        # mehbutan = QPushButton('meh :3')


        # diebutan.clicked.connect(QCoreApplication.instance().quit)


        # hbox = QHBoxLayout()

        # hbox.addStretch(1)
        # hbox.addWidget(butan)
        # hbox.addWidget(diebutan)

        # hbox2 = QHBoxLayout()
        # hbox2.addStretch(1)
        # hbox2.addWidget(mehbutan)
        # hbox2.addStretch(2)


        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox2)
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)


        # self.setLayout(vbox)

        # self.setGeometry(300,300,300,150)
        # self.show()








# class abslayout(QWidget):
#     def __init__(self): 
#         super(abslayout, self).__init__()
#         self.initUI()

#     def initUI(self):
        
#         l1 = QLabel('coding', self)
#         l1.move(15,10)

#         l2 = QLabel('cooooding more', self)
#         l2.move(35,40)

#         l3 = QLabel('for koodarens', self)
#         l3.move(55,70)

#         self.setGeometry(300,300,250,150)
#         self.setWindowTitle('Absolute positioning.')
#         self.show()


 #   class MainWindow(QMainWindow):
#     def __init__(self): 
#         super(MainWindow, self).__init__()
#         self.initUI()

#     def initUI(self):
        
#         editor = QTextEdit()
        
#         self.setCentralWidget(editor)

#         exitAction = QAction('Exit', self)
#         exitAction.setShortcut('Ctrl+6')
#         exitAction.setStatusTip("I'll die if you click me.")
#         exitAction.triggered.connect(self.close)

#         self.statusBar()


#         toolbar = self.addToolBar('Exit')
#         toolbar.addAction(exitAction)


#         menubar = QMenuBar(None)
#     #    menubar.setMenuRole(0)


#  # #       self.menubar = self.menuBar()

#  #        file_menu = menubar.addMenu('&Filde')
#  #        file_menu.addAction(exitAction)

 

#         menu = self.menuBar()
#         filemenu = menu.addMenu('&File')

#         #Prevent OS X from abducting the menu item:
#         exitAction.setMenuRole(QAction.MenuRole.NoRole)

#         filemenu.addAction(exitAction)
#         foobarmenu = menu.addMenu('&Foobar')
#         # menu.addMenu('&Quiche')
        
        


#         self.setGeometry(100,500,400,300)
#         self.show()


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





        # gamebox = GameArea()
        # textbox = QTextEdit()



        # #menubar
        # menu = QMenuBar()

        # # menu on menubar
        # lolmenu = QMenu("Yeahhhhh", menu)
        # menu.addMenu(lolmenu)

        # # Define action
        # lolaction = QAction("Lolwat", self)
        # lolaction.setStatusTip("Some menu item you know?")
        # lolaction.triggered.connect(self.close)

        # # add action to a menu. 
        # lolitem = lolmenu.addAction(lolaction)
 
        
        # # create status bar
        # status = QStatusBar()
        # status.showMessage("Initial status message")
        
        # # Set the created stuff to main window. 
        # self.setMenuBar(menu)
        # self.setStatusBar(status)





        # hit_button = QPushButton("Hit")
        # double_button = QPushButton("Double")
        # stand_button = QPushButton("Stand")
        # split_button = QPushButton("Split")
        # insurance_button = QPushButton("Insurance")

        # # Make a layout for buttons
        # buttons_layout = QHBoxLayout()
        # buttons_layout.addWidget(hit_button)
        # buttons_layout.addWidget(double_button)
        # buttons_layout.addWidget(stand_button)
        # # split & insurance not implemented yet.

        # player_status = QLabel("Player status: ")
        # dealer_status = QLabel("Dealer status: ")




        # player_status = QLabel("Player status: ")
        # dealer_status = QLabel("Dealer status: ")

        # # Make layout for game area
        # vbox = QVBoxLayout()
        # vbox.addLayout(buttons_layout)
        # vbox.addWidget


        # self.setLayout(vbox)

        # self.show()




        # # # Layouts
        # split = QHBoxLayout()
        # split.addWidget(textbox)
        # split.addWidget(gamebox)
    

        # self.setLayout(split)
        # self.show()

        # Init shit

#         menu = self.menuBar()
#         filemenu = menu.addMenu('&File')

#         #Prevent OS X from abducting the menu item:
#         exitAction.setMenuRole(QAction.MenuRole.NoRole)

#         filemenu.addAction(exitAction)
#         foobarmenu = menu.addMenu('&Foobar')
#         # menu.addMenu('&Quiche')
        


# if __name__ == '__main__':
#     application = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     application.exec_()
#     sys.exit()