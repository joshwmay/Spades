from spades_functions import *
import pandas as pd
import math
import random

class Cards:
    """
    This class creates various attributes for a round of spades,
    and establishes the object frame work necessary to be used in logic
    and other facets of a
    game of spades
    """

    def __init__(self):
        self.started = 0

        self.p1disc = 0
        self.p2disc = 0
        self.p3disc = 0
        self.p4disc = 0

        self.p1_discs = []
        self.p2_discs = []
        self.p3_discs = []
        self.p4_discs = []

        self.team1_wins = 0
        self.team2_wins = 0

        self.team1_bags = 0
        self.team2_bags = 0

        self.team1_score = 0
        self.team2_score = 0

        self.p1wins = 0
        self.p2wins = 0
        self.p3wins = 0
        self.p4wins = 0

        self.round = 1

        self.deck = self.set_deck()

        self.winner = 0
        self.game_winner = 0

        self.highs = ["Jack","Queen","King","Ace"]
        self.mids = [7,8,9,10]
        self.lows = [2,3,4,5,6]

        self.spades_break = 1
        self.set_suit = None

        self.turn = self.deck[0]
        p1 = self.deck[1]
        self.p1 = p1
        self.c1 = p1[0]
        self.c2 = p1[1]
        self.c3 = p1[2]
        self.c4 = p1[3]
        self.c5 = p1[4]
        self.c6 = p1[5]
        self.c7 = p1[6]
        self.c8 = p1[7]
        self.c9 = p1[8]
        self.c10 = p1[9]
        self.c11 = p1[10]
        self.c12 = p1[11]
        self.c13 = p1[12]

        # We use a randomly generated shell of cards for a user's hand
        # and then create the user, and self.p1 becomes the cardObject owner
        # but the cards must be moved to the discards containers

        self.p1_bid = int(self.deck[2])

        self.p2 = self.deck[3]
        self.p2_bid = int(self.deck[4])


        self.p3 = self.deck[5]
        self.p3_bid = int(self.deck[6])


        self.p4 = self.deck[7]
        self.p4_bid = int(self.deck[8])

        self.team1 = self.p1, self.p3
        self.team2 = self.p2, self.p4

        self.team1_bids = self.p1_bid, self.p3_bid
        self.team2_bids = self.p2_bid, self.p4_bid

        self.suits = {"Hearts", "Clubs", "Diamonds", "Spades"}

        self.score_frame = pd.DataFrame({"Bids":[self.p1_bid, self.p2_bid, \
                    self.p3_bid, self.p4_bid,"nan"],"Wins":[0, 0, 0, 0, 0],\
                    "Bags":[0, 0, 0, 0, 0], "Score":[0,0,0,0,0], \
                    "Rd1":[0,0,0,0,0], "Rd2":[0,0,0,0,0], "Rd3":[0,0,0,0,0],\
                    "Rd4":[0,0,0,0,0], "Rd5":[0,0,0,0,0], "Rd6":[0,0,0,0,0],\
                    "Rd7":[0,0,0,0,0], "Rd8":[0,0,0,0,0], "Rd9":[0,0,0,0,0],\
                    "Rd10":[0,0,0,0,0],"Rd11":[0,0,0,0,0], "Rd13":[0,0,0,0,0]},
                    index = ["Player 1", "Player 2", "Player 3", "Player 4",\
                    "Winner"])

    def set_deck(self):
        """
        Creates a bundle that includes a new deck of shuffled
        cards and logically automated computer bids
        """
        self.deck = initialize_spades(spades_deal(shuffled(spades_deck())))
        return self.deck

    def reset_all(self, cards):
        """
        Resets necessary attributes of cards_class intended to be used
        after a round of 13 discards from each player has occurred
        """
        cards.started = 0

        cards.p1_discs = []
        cards.p2_discs = []
        cards.p3_discs = []
        cards.p4_discs = []

        cards.p1wins = 0
        cards.p2wins = 0
        cards.p3wins = 0
        cards.p4wins = 0

        cards.round = 1

        cards.deck = self.set_deck()

        cards.p1disc = None
        cards.p2disc = None
        cards.p3disc = None
        cards.p4disc = None

        cards.winner = None
        cards.game_winner = None

        cards.spades_break = 1
        cards.set_suit = None

        cards.turn = cards.deck[0]
        p1 = cards.deck[1]
        cards.p1 = p1
        cards.c1 = p1[0]
        cards.c2 = p1[1]
        cards.c3 = p1[2]
        cards.c4 = p1[3]
        cards.c5 = p1[4]
        cards.c6 = p1[5]
        cards.c7 = p1[6]
        cards.c8 = p1[7]
        cards.c9 = p1[8]
        cards.c10 = p1[9]
        cards.c11 = p1[10]
        cards.c12 = p1[11]
        cards.c13 = p1[12]

        cards.p1_bid = int(cards.deck[2])

        cards.p2 = cards.deck[3]
        cards.p2_bid = int( cards.deck[4])

        cards.p3 = cards.deck[5]
        cards.p3_bid = int(cards.deck[6])

        cards.p4 = cards.deck[7]
        cards.p4_bid = int(cards.deck[8])

        cards.team1 = cards.p1, cards.p3
        cards.team2 = cards.p2, cards.p4

        cards.team1_bids = cards.p1_bid, cards.p3_bid
        cards.team2_bids = cards.p2_bid, cards.p4_bid

        return cards.started, cards.p1_discs, cards.p2_discs, cards.p3_discs,\
        cards.p4_discs, cards.p1wins, cards.p2wins, cards.p3wins, cards.p4wins,\
        cards.round, cards.deck, cards.p1disc, cards.p2disc, cards.p3disc,\
        cards.p4disc, cards.winner, cards.game_winner, cards.spades_break,\
        cards.set_suit, cards.turn, cards.p1, cards.c1, cards.c2, cards.c3,\
        cards.c4, cards.c5, cards.c6, cards.c7, cards.c8, cards.c9, cards.c10,\
        cards.c11, cards.c12, cards.c13, cards.p1_bid, cards.p2, cards.p2_bid,\
        cards.p3,  cards.p3_bid,  cards.p4, cards.p4_bid, cards.team1,\
        cards.team2, cards.team1_bids, cards.team2_bids
    def hearts(self, p_hand):
        """ This method counts hearts, and will help in logic for discards """
        count = counter(p_hand)
        return count[0]

    def clubs(self, p_hand):
        """ This method counts clubs, and will help in logic for discards """
        count = counter(p_hand)
        return count[1]

    def diamonds(self, p_hand):
        """ This method counts diamonds, and will help in logic for discards """
        count = counter(p_hand)
        return count[2]

    def spades(self, p_hand):
        """ This method counts spades, and will help in logic for discards """
        count = counter(p_hand)
        return count[3]

    def max_suit(self, p_hand):
        """
        This method determines the suit with the most cards in a given hand
        """
        hearts = self.hearts(p_hand)
        clubs = self.clubs(p_hand)
        diamonds = self.diamonds(p_hand)
        spades = self.spades(p_hand)
        if(hearts >= clubs and hearts >= diamonds and hearts >= spades):
            return "Hearts"
        elif(clubs >= hearts and clubs >= diamonds and clubs >= spades):
            return "Clubs"
        elif(diamonds >= hearts and diamonds >= clubs and diamonds >= spades):
            return "Diamonds"
        elif(spades >= hearts and spades >= clubs and spades >= diamonds):
            return "Spades"

    def min_suit(self, p_hand):
        """ Determines the suit with the least cards in a given hand """
        hearts = self.hearts(p_hand)
        clubs = self.clubs(p_hand)
        diamonds = self.diamonds(p_hand)
        spades = self.spades(p_hand)
        if(hearts <= clubs and hearts <= diamonds and hearts <= spades):
            return "Hearts"
        elif(clubs <= hearts and clubs <= diamonds and clubs <= spades):
            return "Clubs"
        elif(diamonds <= hearts and diamonds <= clubs and diamonds <= spades):
            return "Diamonds"
        elif(spades <= hearts and spades <= clubs and spades <= diamonds):
            return "Spades"

class Score(Cards):
    def __init__(self):
        Cards.__init__(self)
        self.cards.__init__()
        self.score = 0
        self.bags = bags
        self.team = team

    def __str__(self):
        return str(self.score)

    def get_score(self):
        """ Attains scores """
        team_score = self.score
        if self.team.successed_nil():
            team_score += 100
        elif self.team.failed_nil():
            team_score -= 100

        if self.team.made_bid():
            team_score += (self.team.bid * 10)
        else:
            team_score -= (self.team.bid * 10)

        if self.bags.has_gone_over():
            team_score -= 100

        self.score = team_score
        return self.score

    def update_score(self, board):
        """ Updates team scores """
        if self.team.number == 1:
            board.team1_score = self.score
        else:
            board.team2_score = self.score

    def has_winning_score(self, game_score):
        """ Determines if a score is 'winning' """
        return self.score >= game_score
