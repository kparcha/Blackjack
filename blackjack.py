import randomsuit_dic = {0:"clubs", 1:"diamonds", 2:"hearts", 3:"spades"}face_dic = {0:"ace", 10:"jack", 11:"queen", 12:"king"}face_list = range(10,13)suits = range(4)ranks = range(13)class Deck(object):    def __init__(self):        self.deck = []    def create_deck(self):        for s in suits:            for r in ranks:                card = Card(s, r)                deck.deck.append([card.get_suit(), card.get_rank()])    def deal(self, cards_in_hand):        for i in range(cards_in_hand):            hand.player_hand.append(deck.deck.pop())class Card(object):    def __init__(self, suit, rank):        self.suit = suit        self.rank = rank    def get_suit(self):        return self.suit    def get_rank(self):        return self.rankclass Hand(object):    def __init__(self):        self.player_hand = []    def display_player_hand(self):        for i in range(len(self.player_hand)):            a = self.player_hand[i]            if a[1] in face_dic:                print "You've been dealt the", face_dic[a[1]], "of", suit_dic[a[0]]            else:                print "You've been dealt the", a[1], "of", suit_dic[a[0]]class Dealer(object):    passclass Player(object):    def __init__(self):        self.bust = False        self.blackjack = False        self.gameover = False        self.hand_dic = {}    def check_status(self, player_hand):        for i in range(len(player_hand)):            card = player_hand[i]            rank = card[1]            if rank in face_list:                value = 10            elif rank == 0:                value = int(raw_input("Would you like your ace to represent 1" \                    " or 11? "))                #if value != 1 or 11:                #    print "Please enter 1 or 11."                # make this a loop            else:                value = rank            self.hand_dic[rank] = value        if sum(self.hand_dic.itervalues()) > 21:            self.bust = True        elif sum(self.hand_dic.itervalues()) == 21:            self.blackjack = True    def game_over(self):        if self.bust or self.blackjack == True:            self.gameover = True            #play_again = raw_input("Would you like to play again? ")            # if yes then start game again else stop        return self.gameover        print self.gameover    def hit(self):        deck.deal(1)    def stand(self):        gameover = Truedeck = Deck()hand = Hand()player = Player()deck.create_deck()random.shuffle(deck.deck)deck.deal(2)hand.display_player_hand()player.check_status(hand.player_hand)player.game_over()while player.gameover == False:    action = raw_input("Stand or hit?\n").lower()    if action == "stand":        player.stand()    if action == "hit":        player.hit()        hand.display_player_hand()        player.check_status(hand.player_hand)        player.game_over()