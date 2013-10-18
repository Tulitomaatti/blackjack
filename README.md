blackjack
=========

A simple blackjack card game with light statistics. All players are dealed 2 card in the beginning, the purpose is to get as close to 21 as possible without going over. King, Queen, and Jack count as 10 when calculating hand value. The player may request more cards or stop. A round will end when the dealer has a hand of at least 17 of value. 

Default minimum and maximum bets are 0 and 100 respectively. 


Installation & Usage
--------------------

* Install nose and pyside via pip. 
* run main.py to use the Text UI, or bjgui.py to use the GUI.


Known Bugs:
-----------

Text UI:

Entering an empty string as a bet causes str->float conversion to fail and crash the program


GUI:

* Round actions aren't working


Missing features:

* Soft Aces
* More than 1 player on GUI
* Prettification of Text UI was sacrificed in order to have something that resembles a GUI. 

