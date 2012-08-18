import random

suit_dic = {0:"Clubs", 1:"Diamonds", 2:"Hearts", 3:"Spades"}
face_dic = {0:"Ace", 10:"Jack", 11:"Queen", 12:"King"}
face_list = range(10,13)
suits = range(4)
ranks = range(13)
prompt = "Stand, double down or hit?\n"

class Deck(object):
    def __init__(self):
        self.deck = []

    def create_deck(self):
        for s in suits:
            for r in ranks:
                card = Card(s, r)
                deck.deck.append([card.get_suit(), card.get_rank()])

    def deal(self, cards_to_deal, hand_to_deal):
        for i in range(cards_to_deal):
            hand_to_deal.append(deck.deck.pop())

class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

class Hand(object):
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []

    def display_full_hand(self, input_hand):
        for i in range(len(input_hand)):
            a = input_hand[i]
            if a[1] in face_dic:
                print face_dic[a[1]], "of", suit_dic[a[0]]
            else:
                print a[1] + 1, "of", suit_dic[a[0]]
        print "-----------------------------------"

    def display_hand_no_pocket_card(self):
        # Hides the first card of the hand from view of the player
        print "Dealer's visible hand:"
        for i in range(1, len(self.dealer_hand)):
            a = self.dealer_hand[i]
            if a[1] in face_dic:
                print face_dic[a[1]], "of", suit_dic[a[0]]
            else:
                print a[1] + 1, "of", suit_dic[a[0]]
        print "-----------------------------------"

class Player(object):
    def __init__(self):
        self.bust = False
        self.blackjack = False
        self.gameover = False
        self.ace_value = None

    def determine_hand_value(self, player_hand):
        self.hand = []
        # By sorting the list the Ace value is calculated last, allowing for
        # the algorithm in set_ace_value to work. Changing the name of the
        # input hand is done to ensure that display_hand_no_pocket_card works
        # correctly instead of hiding the highest value card in the Dealer's
        # hand.
        counting_hand = player_hand
        counting_hand = counting_hand.sort(reverse = True)
        for i in range(len(counting_hand)):
            card = counting_hand[i]
            rank = card[1]
            if rank in face_list:
                value = 10
                self.hand.append(value)
            elif rank == 0:
                self.set_ace_value()
                self.hand.append(self.ace_value)
            else:
                value = rank + 1
                self.hand.append(value)
        return self.hand

    def set_ace_value(self):
        if sum(self.hand) + 11 <= 21:
            self.ace_value = 11
        else:
            self.ace_value = 1
        return self.ace_value

    def check_status(self, player_hand):
        if sum(self.hand) > 21:
            self.bust = True
        elif sum(self.hand) == 21:
            self.blackjack = True

    def game_over(self):
        if self.bust == True:
            self.gameover = True
            print "You went bust!"
        elif self.blackjack == True:
            self.gameover = True
            print "Blackjack!"
        return self.gameover


    def hit(self, player):
        deck.deal(1, player)

    def stand(self):
        self.gameover = True
        return self.gameover

    def double_down(self):
        game.pot = game.pot + chips.bet_size
        self.hit(player)
        self.stand()

class Dealer(Player):
    def __init__(self):
        super(Dealer, self).__init__()
        # Setting a default action for the Dealer makes the determine_action
        # method a little simpler
        self.action = "hit"

    def determine_action(self):
        if sum(self.hand) > 16:
        # The Dealer hits on soft 17. This method utilizes index() to search
        # for an Ace that is currently worth 11 points. If it finds one
        # no exception is raised, so the Dealer will hit; however, if a
        # ValueError is raised there is no Ace worth 11 points and the
        # Dealer will stand.
            if sum(self.hand) == 17:
                try:
                    self.hand.index(11)
                    self.action = "hit"
                except ValueError:
                    self.action = "stand"
        else:
            self.action = "hit"
        return self.action

    def execute(self):
        if self.gameover == False:
            self.determine_action()
            if self.action == "stand":
                self.stand
            elif self.action == "hit":
                self.hit(hands.dealer_hand)
                hands.display_hand_no_pocket_card()
                self.determine_hand_value(hands.dealer_hand)
                self.check_status(dealer.hand)
                self.game_over()
            return self.gameover
        else:
            pass

    def game_over(self):
        if self.bust == True:
            print "The dealer has gone bust."
            self.gameover == True
        elif self.blackjack == True:
            print "The dealer has blackjack."
            self.gameover == True
        return self.gameover

class Chips(object):
    def __init__(self):
        self.value = 200
        self.bet_size = None

    def bet(self):
        self.bet_size = raw_input("How much would you like to bet? ")
        while self.bet_size.isdigit() == False:
            print "Please enter a number."
            self.bet_size = raw_input("How much would you like to bet? ")
        self.value = self.value - int(self.bet_size)
        game.pot = game.pot + int(self.bet_size)
        return self.bet_size
        return self.value
        return game.pot

class Game(object):
    def __init__(self):
        self.play = True
        self.pot = 0
        self.result = None

    def new_round(self):
        if player.gameover == True:
            play_again = raw_input("Would you like to play again? ").lower()
            if play_again.startswith("y") == True:
                self.play = True
            elif play_again.startswith("y") == False:
                self.play = False
            return self.play

    def compare_hands(self, player_hand, dealer_hand):
        player.determine_hand_value(hands.player_hand)
        dealer.check_status(hands.dealer_hand)
        player_value = sum(player.hand)
        dealer_value = sum(dealer.hand)
        print "The dealer's hand is worth %r points." % dealer_value
        print "The player's hand is worth %r points." % player_value
        if player.blackjack == True and dealer.blackjack == False:
            print "The player wins."
            self.result = "win_blackjack"
        elif dealer.bust == True:
            print "The player wins."
            self.result = "win"
        elif player_value > dealer_value and player.bust == False:
            print "The player wins."
            self.result = "win"
        elif dealer.blackjack == True and player.blackjack == False:
            print "The house wins."
            self.result = "loss"
        elif dealer_value > player_value and dealer.bust == False:
            print "The house wins."
            self.result = "loss"
        elif player.bust == True:
            print "The house wins."
            self.result = "loss"
        elif dealer_value == player_value:
            print "The two sides tied. Push."
            self.result = "push"
        dealer.gameover = True
        player.gameover = True
        return self.result

    def pay_out(self):
        if self.result == "win":
            chips.value = chips.value + 2*self.pot
            self.pot = 0
        elif self.result == "win_blackjack":
            chips.value = int(chips.value + int(2.5*float(self.pot)))
            self.pot = 0
        elif self.result == "loss":
            self.pot = 0

# Game loop
game = Game()
chips = Chips()
while game.play == True:
    deck = Deck()
    hands = Hand()
    player = Player()
    dealer = Dealer()
    print "You have %d chips." % chips.value
    chips.bet()
    deck.create_deck()
    random.shuffle(deck.deck)
    deck.deal(2, hands.player_hand)
    deck.deal(2, hands.dealer_hand)
    hands.display_hand_no_pocket_card()
    hands.display_full_hand(hands.player_hand)
    player.determine_hand_value(hands.player_hand)
    player.check_status(player.hand)
    player.game_over()
    dealer.determine_hand_value(hands.dealer_hand)
    dealer.check_status(dealer.hand)
    dealer.game_over()
    while player.gameover == False or dealer.gameover == False:
        if player.gameover == False:
            action = raw_input(prompt).lower()
            if action.startswith("s"):
                player.stand()
                dealer.determine_hand_value(hands.dealer_hand)
                dealer.check_status(dealer.hand)
                dealer.execute()
            elif action.startswith("h"):
                player.hit(hands.player_hand)
                hands.display_full_hand(hands.player_hand)
                player.determine_hand_value(hands.player_hand)
                player.check_status(player.hand)
                player.game_over()
                if player.bust == False and dealer.gameover == False:
                    dealer.determine_hand_value(hands.dealer_hand)
                    dealer.check_status(dealer.hand)
                    dealer.execute()
            elif action.startswith("d"):
                player.double_down()
                dealer.determine_hand_value(hands.dealer_hand)
                dealer.check_status(dealer.hand)
                dealer.execute()
        elif player.bust == True:
            dealer.stand()
        elif player.blackjack == True and dealer.gameover == False:
            dealer.determine_hand_value(hands.dealer_hand)
            dealer.check_status(dealer.hand)
            dealer.execute()
        elif dealer.bust == True:
            break
        elif player.gameover == True:
            dealer.determine_hand_value(hands.dealer_hand)
            dealer.check_status(dealer.hand)
            dealer.execute()
    print "Dealer's full hand:"
    hands.display_full_hand(hands.dealer_hand)
    print "Your final hand:"
    hands.display_full_hand(hands.player_hand)
    game.compare_hands(hands.player_hand, hands.dealer_hand)
    game.pay_out
    if chips.value == 0:
        print "Sorry, you ran out of money!"
        break
    game.new_round()

