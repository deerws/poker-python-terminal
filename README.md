### Casino Royale - Card Game Simulation
Welcome to Casino Royale, a Python-based card game simulator! This project is a simple implementation of a card game where you can play against a bot, place bets, and determine the winner based on the dealt cards.

🃏 **About the Project**

This project simulates a card game where:
->A deck of 52 cards is created and shuffled.
->The player and the bot are each dealt 2 cards.
->The table receives a variable number of cards (depending on the function called).
->The player can place bets, check, or fold.
->The winner is determined based on the cards in hand.

The code is developed in Python and uses concepts such as classes, enumerations, lists, and shuffling methods.

🚀 **How to Run the Project**

Prerequisites:
*Python 3.x installed on your system.
*Basic knowledge of command-line operations.
*Installation and Execution Steps
Clone the repository:

""bash
  git clone https://github.com/your-username/casino-royale.git
  cd casino-royale

Run the script:

""bash
  python casino_royale.py

Follow the on-screen instructions:

The game will start automatically.
You will be prompted to place a bet.
Choose between fold (surrender), check (check), or raise (increase the bet).

🎮 **How to Play**
Game Start:

The deck is shuffled.
The player and the bot are each dealt 2 cards.
The table receives a number of cards depending on the function called (play, play1, or play2).

Placing Bets:

Enter your bet amount when prompted.

Choose an action:

fold: Surrender the round (the bot wins).

check: Check the cards (the winner is determined based on the hands).

raise: Increase the bet (enter the additional amount).

Result:

The winner is displayed in the console.

The game can be restarted automatically.

🛠️ **Code Structure**
The code is organized into classes and methods for easy readability and maintenance:

Main Classes
Suit and Rank: Enumerations representing the suits and ranks of the cards.

Deck: Represents a deck of 52 cards.

Methods: shuffle() (shuffles the deck) and deal() (deals cards).

Card: Represents an individual card with a suit and rank.

Hand: Represents a hand of cards.

Player: Represents a player with a name and a hand of cards.

Methods: draw() (draws cards) and show_hand() (displays the hand).

Bot and Table: Classes that inherit from Player to represent the bot and the table.

Game: Controls the game logic.

Methods: play(), play1(), play2() (rounds with different numbers of cards on the table) and determine_winner() (determines the winner).

main(): The main function that starts the game and manages user interactions.

🧩 **Example Usage**
When you run the script, you will see something like this:

Copy
=================================
Welcome to Casino Royale
Your best choice in luxury and gambling!
Place your bet: € 100
Table: [A♦, K♠, Q♥, J♣, 10♦]
Player: [7♠, 9♥]
Bot: [5♦, 8♣]
What will you do?: check
You won: € 100


📝 **Future Improvements**

->Implement logic to determine the winner based on poker rules.
->Add more betting options and interactions.
->Improve the user interface (UI) with a graphical library like tkinter or pygame.


🙌 **Credits**
Developed by André Pinheiro Paes - CS Student (UFSC).
Inspired by classic card games like Poker and Blackjack.

Have fun playing! 🎉
