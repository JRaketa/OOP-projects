import random
import time



class Card:

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    def show(self):
        print(f"{self._value} of {self._suit}")


class Deck:

    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]


    def __init__(self):
        self._cards = []
        self.build()
        self.shuffle()

    def build(self):
        for i in range(1, 11):
            for suit in Deck.suits:
                self._cards.append(Card(suit, i))

    def shuffle(self):
        for i in range(len(self._cards)-1, 0, -1):
            rand = random.randint(0, len(self._cards)-1)
            self._cards[i], self._cards[rand] = self._cards[rand], self._cards[i]

    def show(self):
        for card in self._cards:
            card.show()

    def draw(self):
        return self._cards.pop()


class Player:


    def __init__(self, name, is_dealer=False):
        self._name = name
        self._is_dealer = is_dealer
        self._hand = []

    @property
    def name(self):
        return self._name

    @property
    def is_dealer(self):
        return self._is_dealer

    def draw(self, deck):
        self._hand.append(deck.draw())
        return self

    def show_hand(self, reveal_card=False):
        if self._is_dealer == True:
            if reveal_card == True:
                for card in self._hand:
                    card.show()
            else:
                self._hand[0].show()
                print("X")
        else:
            for card in self._hand:
                card.show()

    def get_hand_value(self):
        value = 0
        for card in self._hand:
            value += card.value
        return value

    def erase_hand(self):
        self._hand = []



class Game:


    INSTRUCTION = """\n | Welcome to our version of the Blackjack Game |
=================================================================================
The goal is to get as close to 21 as possible, without going over 21.
Each card has a value and a suit. The values are added for the final result.

The game starts by dealing two cards to the player (you) and to the dealer.
You are playing against the dealer. On each turn, you must choose if you
would like to take another card or stand to stop the game and see if you won.

The game ends if the total value of the player's hand goes over 21,
and it continues until the player chooses to stand if the total value is below 21.

When the game ends or when the player choose to stand,
the total value of each hand is calculated.
The value that is closest to 21 without going over it wins the game.
If the values is over 21, the player or dealer automatically lose the game.
=================================================================================
"""


    def __init__(self, deck, player, dealer):
        self._deck = deck
        self._player = player
        self._dealer = dealer
        self.start_game()


    def start_game(self):
        print(Game.INSTRUCTION)
        turn = 1

        self._player.draw(self._deck).draw(self._deck)
        self._dealer.draw(self._deck).draw(self._deck)
        self.show_both()


        while True:
            if self.ask_choice() == 1:
                self._player.draw(self._deck)
                self.show_both()
            else:
                break


    def show_both(self, reveal_card=False):
        print(f"\n== Turn #{turn} ==\n")
        time.sleep(1)
        print("The Dealer's hand is:\n")
        time.sleep(1)
        self._dealer.show_hand(reveal_card)
        time.sleep(1)
        print("\nYour Hand is:\n")
        self._player.show_hand()


    def ask_choice(self):
        print("\nWhat do you want to do?")
        print("1 - Ask for another card")
        print("2 - Stand")
        choice = int(input("\nYour choice is: "))

        if choice == 1 or choice == 2:
            return choice
        else:
            print("You entered an invalid value, I assume you want to stand.")
            return 2






























deck = Deck()
player = Player("Jack")
dealer = Player("Jeaninne", True)
game = Game(deck, player, dealer)
