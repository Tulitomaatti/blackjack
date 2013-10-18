# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *

import cardpackhand as cph
import game as g
import rules as r
import file_ops as f

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

        self.setFixedSize(100,150)


class CardArea(QFrame):
    def __init__(self): 
        super(CardArea, self).__init__()

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

        player_status = QLabel("Player status: ")
        dealer_status = QLabel("Dealer status: ")

        vbox = QVBoxLayout()

        vbox.addWidget(player_status)
        vbox.addWidget(dealer_status)

        self.setLayout(vbox)

# QMessageBox does this kind of stuff already
# class InfoDialog(QDialog):
#     def __init__(self, str=""): 
#         super(InfoDialog, self).__init__()
#         label = QLabel(str)
#         vbox = QVBoxLayout()
#         vbox.addWidget(label)
#         self.setLayout(vbox)
#         self.show()

class ActionController(QObject):
    def __init__(self, parent=None): 
        super(ActionController, self).__init__()
        self.parent = parent

    # Main menu stuff


    def main_menu(self):
        sender = self.sender()
        sender.parent().parent().setCurrentIndex(0)

    def new_game(self):
        sender = self.sender()
        # First get us to the right view. 
        sender.parent().stack.setCurrentIndex(1)

        

    def options(self):
        sender = self.sender()
        sender.parent().stack.setCurrentIndex(2)


    # options specific

    def show_rules(self):
        # Pop up a dialog with rules in it.
        rules = r.Rules()
        d = QMessageBox()
        d.setText(str(rules))
        d.exec_()
        
    def show_stats(self):
        # Two listviews with players -> player stats
        # would be a rather cool way. 

        # Or a spreadsheet format with players on rows, sortable by a stat.

        # For now: Print all stats to in a dialog.
        # Probably results in horrible things when the player list gets long enough. 
        # TODO: make the message area scrollable, with detailed_text or something else. 
        statsstring = ""
        players = f.read_players()

        for plr in players:
            statsstring += plr.name + "'s Stats: \n"
            statsstring += str(plr.stats)
        
        d = QMessageBox()
        d.setText(statsstring)
        d.exec_()



    # Game related functions 

    def hit(self):
        print "hitting"

    def double(self):
        print "doubling"

    def stand(self):
        print "standing"

    def next_round(self):
        print "next round start please."

    def quit_to_menu(self):
        sender = self.sender()
        sender.parent().parent().setCurrentIndex(0)

    def exit_program(self):
        sys.exit()

class GameArea(QWidget):
    def __init__(self): 
        super(GameArea, self).__init__()

        self.initUI()

        # We can now add cards to the table like this
        self.card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(4, "heart")))
        # card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(5, "gay")))
        self.card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(45, "dragon")))

        self.card_area.player_hand_layout.addWidget(CardLabel(cph.Card(3, "lol")))
        # card_area.player_hand_layout.addWidget(CardLabel(cph.Card(6, "asdf")))


    def initUI(self):
        # Major areas / components
        self.ctl = ActionController(self)
        self.card_area = CardArea()
        self.status = StatusArea()

        # Menus

        # Does GUI Code always end up looking this ugly? 
        # See OptionsMenu for a slightly more
        # stylish way to init gazillion buttons.

        # Buttons 
        hit_button = QPushButton("Hit")
        double_button = QPushButton("Double")
        stand_button = QPushButton("Stand")
        next_round_button = QPushButton("Play next round")
        quit_to_menu_button = QPushButton("Quit to Main menu")
        # split_button = QPushButton("Split", self)
        # insurance_button = QPushButton("Insurance", self)

        # Connects to action controller
        hit_button.clicked.connect(self.ctl.hit)
        double_button.clicked.connect(self.ctl.double)
        stand_button.clicked.connect(self.ctl.stand)
        next_round_button.clicked.connect(self.ctl.next_round)
        quit_to_menu_button.clicked.connect(self.ctl.quit_to_menu)

        # Create and set layouts for buttons and cards. 
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
        card_area_layout.addWidget(self.card_area)
        card_area_layout.addStretch(1)

      # quit_to_menu_button.hide()
        next_round_button.setEnabled(False)

        vbox = QVBoxLayout()

        vbox.addLayout(card_area_layout)
        vbox.addLayout(action_buttons_layout)
        vbox.addWidget(self.status)
        vbox.addLayout(menu_buttons_layout)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # Finalizing stuff.
        self.setGeometry(80, 80, 300, 300)
        self.setWindowTitle('Blackjack')
    #    self.show()  

class MainMenu(QWidget):
    def __init__(self, parent=None): 
        super(MainMenu, self).__init__()
        self.ctl = ActionController()
        self.stack = parent
        self.parent = parent

        header = QLabel("BLACKJACK")
        f = self.font()
        f.setPointSize(62)
        header.setFont(f)

        newgame_button = QPushButton("New Game", self)
        options_button = QPushButton("Options", self)
        exit_button = QPushButton("Exit", self)

        f.setPointSize(20)
        newgame_button.setFont(f)
        options_button.setFont(f)
        exit_button.setFont(f)

        newgame_button.clicked.connect(self.ctl.new_game)
        newgame_button.setShortcut("Ctrl+n")
        options_button.clicked.connect(self.ctl.options)
        options_button.setShortcut("Ctrl+o")
        exit_button.clicked.connect(self.ctl.exit_program)
        exit_button.setShortcut("Ctrl+x")

        vbox = QVBoxLayout()
        vbox.addWidget(header)
        vbox.addWidget(newgame_button)        
        vbox.addWidget(options_button)
        vbox.addWidget(exit_button)    

        self.setLayout(vbox)
        self.setWindowTitle('Blackjack')
    #   self.show()

class OptionsMenu(QWidget):
    def __init__(self): 
        super(OptionsMenu, self).__init__()
        self.ctl = ActionController()

        # options_stack = QStackedWidget(self)
        # Two edged sword: connecting buttons is trickier.

        rules_button = QPushButton("Show Rules", self)
        stats_button = QPushButton("Show Stats", self)
        back_button = QPushButton("Back", self)

        rules_button.clicked.connect(self.ctl.show_rules)
        stats_button.clicked.connect(self.ctl.show_stats)
        back_button.clicked.connect(self.ctl.main_menu)
        
        vbox = QVBoxLayout()
        vbox.addWidget(rules_button)
        vbox.addWidget(stats_button)
        vbox.addWidget(back_button)

        #options_stack.addWidget(vbox)

        # stackbox = QVBoxLayout()
        # stackbox.addWidget(options_stack)
        self.setLayout(vbox)

# Maybe later
# class RulesScreen(QWidget):
#     pass
# class StatsScreen(QWidget):
#     pass



class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__()

        #maybe init statusbar or something. 

        self.setCentralWidget(MainMenu())
        self.show()


if __name__ == '__main__':
    a = QApplication(sys.argv)
    stack = QStackedWidget()

    # w = MainWindow()

    main_menu = MainMenu(stack)
    game_area = GameArea()
    options_menu = OptionsMenu()

    stack.addWidget(main_menu)
    stack.addWidget(game_area)
    stack.addWidget(options_menu)
   # stack.setCurrentIndex()
    stack.show()

    a.exec_()
    sys.exit()
