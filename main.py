import random
from enum import Enum

# Importa o módulo random para embaralhar o deck
# Importa a classe Enum para criar enumeradores

# Enumeração para os naipes das cartas
class Suit(Enum):
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'

# Enumeração para os valores das cartas
class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    J = 11
    Q = 12
    K = 13
    A = 14

# Classe que representa um baralho de cartas
class Deck:
    def __init__(self):
        # Cria um deck de 52 cartas (uma para cada combinação de naipe e valor)
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self):
        # Embaralha as cartas no deck
        random.shuffle(self.cards)

    def deal(self, num_cards):
        # Distribui um número específico de cartas do deck
        return [self.cards.pop() for _ in range(num_cards)]

# Classe que representa uma carta
class Card:
    def __init__(self, suit, rank):
        self.suit = suit  # Naipes
        self.rank = rank  # Valores

    def __str__(self):
        # Retorna a representação da carta como string
        return f"{self.rank.name.capitalize()}{self.suit.value}"

# Classe que representa uma mão de cartas
class Hand:
    def __init__(self, cards):
        self.cards = cards  # Lista de cartas na mão

# Classe que representa um jogador
class Player:
    def __init__(self, name):
        self.name = name  # Nome do jogador
        self.hand = None  # Mão inicial do jogador (vazia)

    def draw(self, deck, num_cards):
        # Puxa um número específico de cartas do deck e atribui à mão do jogador
        self.hand = Hand(deck.deal(num_cards))

    def show_hand(self):
        # Exibe a mão do jogador no console
        print(f"{self.name}: {[str(card) for card in self.hand.cards]}")

# Classe que representa um jogador bot (herda de Player)
class Bot(Player):
    def __init__(self):
        super().__init__("Bot")  # Inicializa o bot com o nome "Bot"

# Classe que representa a mesa (herda de Player)
class Table(Player):
    def __init__(self):
        super().__init__("Table")  # Inicializa a mesa com o nome "Table"

# Classe que representa o jogo
class Game:
    def __init__(self):
        self.deck = Deck()  # Cria um novo baralho
        self.deck.shuffle()  # Embaralha o baralho
        self.player = Player("Player")  # Cria um jogador humano
        self.bot = Bot()  # Cria um bot
        self.table = Table()  # Cria uma mesa

    def play(self):
        # Executa uma rodada do jogo com 2 cartas para cada jogador e 5 para a mesa
        self.player.draw(self.deck, 2)
        self.bot.draw(self.deck, 2)
        self.table.draw(self.deck, 5)
        self.table.show_hand()
        self.player.show_hand()
        self.bot.show_hand()

    def play1(self):
        # Executa uma rodada do jogo com 2 cartas para cada jogador e 4 para a mesa
        self.player.draw(self.deck, 2)
        self.bot.draw(self.deck, 2)
        self.table.draw(self.deck, 4)
        self.table.show_hand()
        self.player.show_hand()
        self.bot.show_hand()

    def play2(self):
        # Executa uma rodada do jogo com 2 cartas para cada jogador e 3 para a mesa
        self.player.draw(self.deck, 2)
        self.bot.draw(self.deck, 2)
        self.table.draw(self.deck, 3)
        self.table.show_hand()
        self.player.show_hand()
        self.bot.show_hand()

    def determine_winner(self):
        # Determina o vencedor com base nas mãos
        if self.hand.rank_hand():
            print('player win')
        else:
            print("player lose")

def main():
    while True:
        print("=================================")
        print("Welcome to Casino Royale")
        print("Your best choice in luxury and gambling!")
        i = input('Place your bet: € ')

        game = Game()  # Cria uma nova instância do jogo
        game.play()  # Executa uma rodada do jogo

        n = input('What will you do?: ')
        if n == 'fold':
            print("Bot wins")
            print("You lost: € " + i)
        elif n == 'check':
            print("You won: € " + i)
        elif n == 'raise':
            m = input('€: ')
            g = int(m) + int(i)  # Soma as apostas
            print("You won: € " + str(g))

if __name__ == "__main__":
    main()  # Executa a função principal
