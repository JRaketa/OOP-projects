import random
import time



class Card:
    """Class that represents a card of the card game.

    One card contains a value and a suit. That is similar to real cards like for
    poker. However, in this card game there are only numbers as values of the
    cards.

    Attributes:
        suit (str): a suit of the card. There are just four suits in the deck.
        value (int): a value of the card. This is an integer in range of (1, 1).

    Methods:
        show(): prints the value and the suit. The print format:
            [value] of [suit]. Example: 6 of Spades.
    """

    def __init__(self, suit, value):
        """Initialize the values of the instance attributes of the card instance
        of Card.

        Args:
            suit (str): a suit of the card. There are just four suits in the
            deck.
            value (int): a value of the card. This is an integer in range of
            (1, 1).
        """
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        """Suit that represents the card."""
        return self._suit

    @property
    def value(self):
        """Value that represents the card."""
        return self._value

    def show(self):
        """prints the value and the suit.

        The print format: [value] of [suit]. Example: 6 of Spades.
        """
        print(f"{self._value} of {self._suit}")


class Deck:
    """Class that represents the deck of the card game.

    The deck contains 36 cards as in a real card game. The deck is generated
    and shuffled randomly. When a player draw a card, the card is removed from
    the deck.

    Attributes:
        cards (list): a list that contains the cards of the card game.

    Methods:
        build(): generates a new list of the deck's cards. All cards are
            arranged from lower value to greater value.
        shuffle(): randomizes position of every card in the deck. The shuffled
            deck is used for the game.
        draw(): Remove the last card from the deck and returns it.
    """

    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self):
        """Initialized the instance attributes of the Deck's instance.

        Generates and shuffles the deck.

        Methods:
            build():generates a new list of the deck's cards. All cards are
                arranged from lower value to greater value.
            shuffle():randomizes position of every card in the deck. The shuffled
                deck is used for the game.
        """
        self._cards = []
        self.build()
        self.shuffle()

    @property
    def cards(self):
        """Represents all cards in the deck."""
        return self._cards

    def build(self):
        """Generates a new deck.

        All cards are arranged from lower value to greater value.
        """
        for i in range(1, 11):
            for suit in Deck.suits:
                self._cards.append(Card(suit, i))

    def shuffle(self):
        """Shuffles the deck.

        The shuffle based on replacement of a card with index i to a card with
        index rand. i is an index that runs from 35 to 0. rand is a random
        integer that is taken from the range (0, 35).
        """
        for i in range(len(self._cards)-1, 0, -1):
            rand = random.randint(0, len(self._cards)-1)
            self._cards[i], self._cards[rand] = self._cards[rand], self._cards[i]

    def draw(self):
        """Remove the last card from the deck and returns it."""
        return self._cards.pop()


class Player:
    """Class that represents a player of the card game.

    An instance of the class contains name of the player, his role in this game:
    a player can either human (you) or dealer (computer). Also, the instance
    contains a list cards that were taken by the player for one turn. After each
    turn the list is erased.

    Attributes:
        name (str): name of the player.
        is_dealer (bool): means the role of the player in this game. Default
            value is False that means the player is human (you).
        hand (list): a list of cards that were taken by the player this turn.

    Methods:
        draw (deck): takes one card from the deck and appends it to the player's
            hand.
            Args:
                deck (Deck): list of the cards left.
        show_hand(reveal_card): displays the player's hand.
            Args:
                reveal_card (bool): is used for dealer player. Default value
                    hides one of the dealer's cards when the dealer's hand is
                    printed.
        get_hand_value(): sum of all value from the player's hand.
        erase_hand(): returns an empty array as the player's hand.


    """

    def __init__(self, name, is_dealer=False):
        """Initialize the instance attributes of the Player's instance.

        Args:
            name (str): name of the player.
            is_dealer (bool): means the role of the player in this game. Default
                value is False that means the player is human (you).
        """
        self._name = name
        self._is_dealer = is_dealer
        self._hand = []

    @property
    def name(self):
        """Name of the player."""
        return self._name

    @property
    def is_dealer(self):
        """Is the player a dealer or not."""
        return self._is_dealer

    def draw(self, deck):
        """Takes one card from the deck and appends it to the player's hand.

           Args:
                deck (Deck): list of the cards left.
        """
        self._hand.append(deck.draw())
        return self

    def show_hand(self, reveal_card=False):
        """Displays the player's hand.

        Args:
            reveal_card (bool): is used for dealer player. Default value
                hides one of the dealer's cards when the dealer's hand is
                printed.
        """
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
        """Returns sum of all values from the player's hand."""
        value = 0
        for card in self._hand:
            value += card.value
        return value

    def erase_hand(self):
        """Returns an empty array as the player's hand."""
        self._hand = []



class Game:
    """Class where all game logic is done.

    Here there are conditions for win, lose or tie. Also, number of wins of each
    player is recorded. In the end of each turn the winner is chosen. Dealer
    (computer) can take only two cards within one turn, one of the cards is
    hidden as sign "X". Player (you) takes automatimatically two cards. But
    player can decide either take one more card or stand. Player can take as
    many cards as needed. When player decides to stand, total values of all
    cards of each player are calculated and the winner of the turn is chosen.
    The winner gets one point to his/her wins total number. If it is tie, no one
    gets the point. When the game is over, the winner of the game is chosen
    according to the wins number. The game is over when: 1) before next turn
    there are less than four cards in the deck. 2) There is no cards in the deck
    during a turn. In this two cases the winner of the turn is chosen according
    to the cards the players's hands.

    Attributes:
        deck (Deck): the deck of the card game that consists of 36 cards.
        player (Player): human player (you).
        dealer (Player): computer player.
        turn (int): number of the current turn. Starts with 1.
        count (list): contains numbers of wins of each player. For example:
        [n, m], here player won n times, dealer won m times.

    Methods:
        start_game(): here all the game logic is implemented.
        show_both(reveal_card): prints cards of all both players. By default
            one of the dealer's card is hidden.
            Args:
                reveal_card (bool): reveals all the dealer's cards.
        ask_choice(): Ask the player either to take one more card or stand.
        is_winner(player, dealer): checks if the player is winner. The player's
            hand must less than 22 and greater than dealer's hand.
            Args:
                player (Player): human player (you).
                dealer (Player): dealer (computer).
        is_tie(player, dealer): checks if the player's hand total value equals
            to dealer's hand total value.
            Args:
                player (Player): human player (you).
                dealer (Player): dealer (computer).
        print_count(player, dealer, game_count): prints total number of wins for
            each player. Example: Player (name1): n, Dealer(name2): m.
            Args:
                player (Player): human player (you).
                dealer (Player): dealer (computer).
                game_count (list): list with total numbers of each player's wins.
        is_deck_empty(deck): checks if the deck is empty.
            Args:
                deck (Deck): contains all cards left in the game.
        is_deck_almost_empty(deck): checks if there are less than four cards
            left in the deck.
            Args:
                deck (Deck):contains all cards left in the game.
        print_game_result(player, dealer, game_count): prints the winner, names
            of each player and points count.
            Args:
                player (Player): human player (you).
                dealer (Player): dealer (computer).
                game_count (list): list with total numbers of each player's wins.
    """


    INSTRUCTION = """\n | Welcome to our version of the Blackjack Game |
=================================================================================
The goal is to get as close to 21 as possible, without going over 21.
Each card has a value and a suit. The values are added for the final result.

The game starts by dealing two cards to the player (you) and to the dealer.
You are playing against the dealer. On each turn, you must choose if you
would like to take another card or stand to stop the game and see if you won.

When the game ends or when the player choose to stand,
the total value of each hand is calculated.
The value that is closest to 21 without going over it wins the game.
=================================================================================
"""


    def __init__(self, deck, player, dealer):
        """Initialize the instance attributes of the Game's instance.

        Args:
            deck (Deck): the deck of the card game that consists of 36 cards.
            player (Player): human player (you).
            dealer (Player): computer player.

        Methods:
            start_game(): a method that contains all the game's logic.
        """
        self._deck = deck
        self._player = player
        self._dealer = dealer
        self.turn = 1
        self.count = [0, 0]
        self.start_game()

    def start_game(self):
        """Here all the game logic is implemented.

        First the instruction of the game is printed but only ones. The first
        turn began. Next, each
        player draws two cards from the deck. Hand of each player is printed.
        One of the dealer's card is hidden as marker "X". The player has an option to draw
        one more card as many times as needed. If the player decide to stand,
        the winner of the turn is calculated. The winner gets one point. Next
        turn began. The game goes on until the deck is empty or almost empty
        (there are less than four cards in the deck). 'Deck is empty' is
        checked after every player draw. 'Deck is almost empty' is checked
        before each turn. When one of this 'empty' conditions is fulfilled, the
        game is over. Next, the winner is calculated.
        """
        print(Game.INSTRUCTION)

        while True:
            if self.is_deck_almost_empty(self._deck):
                self.print_game_result(self._player, self._dealer, self.count)
                break

            self._player.draw(self._deck).draw(self._deck)
            self._dealer.draw(self._deck).draw(self._deck)
            self.show_both()

            while True:
                if self.is_deck_empty(self._deck):
                    self.print_game_result(self._player, self._dealer, self.count)
                    break
                if self.ask_choice() == 1:
                    self._player.draw(self._deck)
                    self.show_both()
                else:
                    break

            self.show_both(True)
            is_winner = self.is_winner(self._player, self._dealer)
            is_tie = self.is_tie(self._player, self._dealer)
            if is_winner:
                self.count[0] += 1
                print("\nYou win!")
            if is_tie:
                print("\nIt's tie!")
            if not is_winner and not is_tie:
                self.count[1] += 1
                print("\nDealer won!")
            self._player.erase_hand()
            self._dealer.erase_hand()
            self.turn += 1
            self.print_count(self._player, self._dealer, self.count)

    def show_both(self, reveal_card=False):
        """Prints cards of all both players.

        By default one of the dealer's card is hidden.

        Args:
            reveal_card (bool): reveals all the dealer's cards.
        """
        print(f"\n== Turn #{self.turn} ==\n")
        print("The Dealer's hand is:\n")
        self._dealer.show_hand(reveal_card)
        print("\nYour Hand is:\n")
        self._player.show_hand()

    def ask_choice(self):
        """Ask the player either to take one more card or stand."""
        print("\nWhat do you want to do?")
        print("1 - Ask for another card")
        print("2 - Stand")
        choice = int(input("\nYour choice is: "))

        if choice == 1 or choice == 2:
            return choice
        else:
            print("You entered an invalid value, I assume you want to stand.")
            return 2

    def is_winner(self, player, dealer):
        """Checks if the player is winner.

        The player's hand must less than 22 and greater than dealer's hand.

        Args:
                player (Player): human player (you).
                dealer (Player): dealer (computer).
        """
        player_value = player.get_hand_value()
        dealer_value = dealer.get_hand_value()
        if dealer_value > 21 and player_value <= 21:
            return True
        elif dealer_value <= 21 and player_value <= 21 and player_value > dealer_value:
            return True
        else:
            return False

    def is_tie(self, player, dealer):
        """Checks if it is tie.

        Checks if the player's hand total value equals to dealer's hand total
        value.

        Args:
            player (Player): human player (you).
            dealer (Player): dealer (computer).
        """
        player_value = player.get_hand_value()
        dealer_value = dealer.get_hand_value()
        if player_value == dealer_value:
            return True
        else:
            return False

    def print_count(self, player, dealer, game_count):
        """Prints total number of wins for each player.

        Example: Player (name1): n, Dealer(name2): m.

        Args:
            player (Player): human player (you).
            dealer (Player): dealer (computer).
            game_count (list): list with total numbers of each player's wins.
        """
        print(f"Player ({player.name}): {game_count[0]}, Dealer ({dealer.name}): {game_count[1]}")
        print("\n--------------------------------")

    def is_deck_empty(self, deck):
        """Checks if the deck is empty.

        Args:
            deck (Deck): contains all cards left in the game.
        """
        if len(deck.cards) == 0:
            return True
        else:
            return False

    def is_deck_almost_empty(self, deck):
        """Checks if the deck is almost empty.

        Checks if there are less than four cards left in the deck.

        Args:
            deck (Deck):contains all cards left in the game.
        """
        if len(deck.cards) < 4:
            return True
        else:
            return False

    def print_game_result(self, player, dealer, game_count):
        """Prints the game result.

        Prints the winner, names of each player and points count.

        Args:
            player (Player): human player (you).
            dealer (Player): dealer (computer).
            game_count (list): list with total numbers of each player's wins.
        """
        print("\n--------------------------------\n")
        print("End of the game!\n")
        if game_count[0] > game_count[1]:
            print("Congrats! You win the game!\n")
            self.print_count(player, dealer, game_count)
        if game_count[0] < game_count[1]:
            print("Dealer won! But don't give up!\n")
            self.print_count(player, dealer, game_count)
        if game_count[0] == game_count[1]:
            print("It is tie! That was a hard play!\n")
            self.print_count(player, dealer, game_count)


deck = Deck()
player = Player("Jack")
dealer = Player("Jeaninne", True)
game = Game(deck, player, dealer)
