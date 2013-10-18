# -*- coding: utf-8 -*-

# General pyside guideline from somewhere: 
# Subclass everything and then do things with the new subclasses. 

from PySide.QtCore import *
from PySide.QtGui import *

import cardpackhand as cph
import game as g
import rules as r
import player
import file_ops as fops

import sys




#  _     _            _     _            _      
# | |__ | | __ _  ___| | __(_) __ _  ___| | __  ____
# | '_ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ / |___ \
# | |_) | | (_| | (__|   < | | (_| | (__|   <    __) |
# |_.__/|_|\__,_|\___|_|\__/ |\__,_|\___|_|\_\  |__ <
#                        |__/  __ _ _  _(_)     ___) |
#  aka. functions all         / _` | || | |    |____/
#       over the place        \__, |\_,_|_|
#                             |___/
              
#hax         
actionhelper = ""

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

        self.dealer_label = QLabel("Dealer's hand:")
        self.player_label = QLabel("Player's hand:")

        vbox = QVBoxLayout()

        vbox.addWidget(self.dealer_label)
        vbox.addLayout(self.dealer_hand_layout)
        vbox.addWidget(self.player_label)
        vbox.addLayout(self.player_hand_layout)


        self.setLayout(vbox)

    def set_dealer_hand_label(self,hand):
        self.dealer_label.setText("Dealer's hand value: " + str(hand))
        self.dealer_label.repaint()

    def set_player_hand_label(self, hand):
        self.player_label.setText("Player's hand value: " + str(hand))
        self.player_label.repaint()

    def update_cards(self, game):
        dealer_hand = game.dealer.hand_list[0]
        self.set_dealer_hand_label(str(r.value(dealer_hand))) 

        plr = game.players[0] # GUI is single plr
        plr_hand = plr.hand_list[plr.current_hand]
        self.set_player_hand_label(str(r.value(plr_hand)))
        self.repaint()

        for card in dealer_hand.card_stack:
            self.dealer_hand_layout.addWidget(CardLabel(card))

        for card in plr_hand.card_stack:
            self.player_hand_layout.addWidget(CardLabel(card))

        self.show()


class StatusArea(QWidget):
    def __init__(self): 
        super(StatusArea, self).__init__()

        self.player_status = QLabel("Player status: ")
        self.dealer_status = QLabel("Dealer status: ")

        vbox = QVBoxLayout()

        vbox.addWidget(self.player_status)
        vbox.addWidget(self.dealer_status)

        self.setLayout(vbox)

    def set_dealer_status(self, status):
        self.dealer_status.setText("Dealer status: " + status)
        self.dealer_status.repaint()

    def set_player_status(self, status):
        self.player_status.setText("Player status: " + status)
        self.player_status.repaint()

    def update_status(self, game):
        dealer_hand = game.dealer.hand_list[0]
        self.set_dealer_status(str(dealer_hand) + ' (' + str(r.value(dealer_hand)) + ')') 

        plr = game.players[0] # GUI is single plr
        plr_hand = plr.hand_list[plr.current_hand]
        self.set_player_status(str(plr_hand) + ' (' + str(r.value(plr_hand)) + ')')

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
        # First get us to the right view. 
        sender = self.sender()
        sender.parent().stack.setCurrentIndex(1)
        game_area = sender.parent().stack.widget(1) # This single line took me like 2.5 hours to figure out. 
                                                    # ^ I had trouble getting hold of the game_area handle.
        # Replicate what main.py does with gui magic. 
        # Dirty...
        game = g.Game(game_area) # I desperately need a handle to that game_area.
        #game = globalgame
        game.GUI = True

        for i in xrange(game.rules.number_of_packs):
            game.init_pack()
        game.shuffle_pack()

        game.create_players() # Deadline in 4.5 hours, i might make it to the end of the function.
        
        play_next_round = True
        while (play_next_round):
            game.play_round()
            # players are saved at the end of each round in game.py

            play_next_round = ui.play_next_round()


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
        players = fops.read_players()

        for plr in players:
            statsstring += plr.name + "'s Stats: \n"
            statsstring += str(plr.stats)
        
        d = QMessageBox()
        d.setText(statsstring)
        d.exec_()



    # Game related functions 


        pass



    def hit(self):
        print "hitting"
        global actionhelper
        actionhelper = "h"


    def double(self):
        print "doubling"
        global actionhelper
        actionhelper = "d"

    def stand(self):
        print "standing"
        global actionhelper
        actionhelper = "s"

    def next_round(self):
        print "next round start please."
        global actionhelper
        actionhelper = "n"

    def quit_to_menu(self):
        sender = self.sender()
        sender.parent().parent().setCurrentIndex(0)

    def exit_program(self):
        sys.exit()

class GameArea(QWidget):
    def __init__(self): 
        super(GameArea, self).__init__()

        self.initUI()


        # For testing purposes: 
        # # We can now add cards to the table like this
        # self.card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(4, "heart")))
        # # card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(5, "gay")))
        # self.card_area.dealer_hand_layout.addWidget(CardLabel(cph.Card(45, "dragon")))

        # self.card_area.player_hand_layout.addWidget(CardLabel(cph.Card(3, "lol")))
        # # card_area.player_hand_layout.addWidget(CardLabel(cph.Card(6, "asdf")))


    def initUI(self):
        # Major areas / components
        self.ctl = ActionController(self)
        self.card_area = CardArea()
        self.status = StatusArea()
        self.action = ""

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

        # Test
        #hit_button.clicked.connect(self.get_action)

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
    #   self.show()  




    def update_area(self, game):
        # Update labels
        self.status.update_status(game)
        self.card_area.update_cards(game)
        self.card_area.dealer_label.repaint()
        self.card_area.player_label.repaint()

        # Remove any cards

        # Draw cards


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


# class GetPlayerDialog(QInputDialog):
#     def __init__(self): 
#         super(GetPlayerDialog, self).__int__()

def get_players_for_game(players):
    # Prepare for the same code reading _experience_ as in ui.py, except now
    # with confusing Qt GUI stuff. 

    a = ""
    if not players:
        # players = [] # Was redundant because not players already makes sure that players == []
      
        # Create player dialog
        while a == "":
            a, ok = QInputDialog.getText(None, "New Player", "Enter name for new player: ")
            if not ok: sys.exit()

        #Append created player and return
        players.append(player.Player(a))
        fops.save_players(players)

        print 
        return players
    else: 
        print "Players were found, should be a list here."
        # available_string = "Available players: " + ''.join(' ', players)
        plrs_string = ""
        for plr in players:
            plrs_string += plr.name + ', '


        while a == "":
            # Y U NOT WORK FOR ME ?!?!?
            # dlg = QInputDialog()
            # dlg.setCancelButtonText("Create New Player")
            # dlg.setOkButtonText("adsfddsadfsds")
            # dlg.setOption(QInputDialog.NoButtons)
            # dlg.repaint()
            # dlg.setTextValue(players[0].name)
            # dlg.NoButtons
            # a, choose = dlg.getText(None, "Choose player", plrs_string + "\n\n Enter player name: ")

            # This is why we can't have nice things ^

            # Dialog for getting a player name.

            duplicate_player = False # Unused for now. 
            name = ""
            while name == "":
                choose, name = get_player_name_dialog(plrs_string)

            if not choose:
                try: 
                    for plr in players:
                        if plr.name == name:
                            duplicate_player = True
                            raise Exception("Duplicate Player Exception")
                            
                except Exception: # yeahhh serious business error handling. 
                    print "Duplicate players will not be created."
                    sys.exit()    # Originally i was planning to implement 
                                  # Nice errors for cards running out and 
                # Create player   # too small bets and whatnot. 
                new_plr = player.Player(name)
                players.append(new_plr)
                fops.save_players(players)
                selected = [new_plr]
                return selected

            else:
                # Choose player
                player_found = False
                for plr in players:
                    if plr.name == name:
                        new_plr = plr
                        player_found = True
                        break
                try:
                    if not player_found: raise Exception("Player not found.")
                except Exception:
                    print "Player not found. Exiting."
                    sys.exit()

                        # Only 1 player in gui version for now
                selected = [new_plr]
                return selected

        return players


def get_player_name_dialog(plrs_string):
        dl = QDialog()

        # Widgets for the dialog
        newplr = QPushButton("Create New Player")
        chooseplr = QPushButton("Choose Existing Player")
        line = QLineEdit()
        label = QLabel("Available Players: ")
        label2 = QLabel(plrs_string+ "\n")
        label2.setAlignment(Qt.AlignTop)
        label3 = QLabel("Enter player name:")

        hbox = QHBoxLayout()
        hbox.addWidget(newplr)
        hbox.addStretch(1)
        hbox.addWidget(chooseplr)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(label2)
        vbox.addStretch(1)
        vbox.addWidget(label3)
        vbox.addWidget(line)
        vbox.addLayout(hbox)

        dl.setLayout(vbox)

        name = QLabel() 
        line.textChanged.connect(name.setText)

        newplr.clicked.connect(dl.reject)
        chooseplr.clicked.connect(dl.accept)

        choose = dl.exec_()
        # 1 means we want to choose from existing players.
        # 0 means we create a new player with the name.


        return choose, name.text()  




def get_bet(player):
    ok, bet = QInputDialog().getInt(None, "Betting", "Enter Bet: ", 5, 0, 100, 5)
    if not ok: sys.exit() # they came here to play, right?
    return bet

def show_game(game): # Actually dealer's first card should be kept hidden,
                           # and only revealed when the round ends. 
    # Get the game area widget somehow... or create one?
    game.game_area.update_area(game)


def get_action():
    global actionhelper
    return actionhelper

    

 
if __name__ == '__main__':

    a = QApplication(sys.argv)
    stack = QStackedWidget()

    # w = MainWindow()

    game_area = GameArea()

    main_menu = MainMenu(stack)

    options_menu = OptionsMenu()

    stack.addWidget(main_menu)
    stack.addWidget(game_area)
    stack.addWidget(options_menu)
    # stack.setCurrentIndex()
    stack.show()

    a.exec_()
    sys.exit()

    