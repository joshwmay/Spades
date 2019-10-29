from spades_functions import *
from spades_cards import Cards
import pandas as pd
import numpy as np
import math
import random
import time

class Discard(Cards):
    def __init__(self):
        Cards.__init__(self)

    def remove_card(self, player, card):
        """ Removes a card from a player's hand based on card arg"""
        for i in player:
            if i == card:
                return player.remove(card)

    def flog(self, cards):
        """ This method is to be used in determining an automated discard
        for a player taking the first turn

        Args:
            cards(class) - A class of instantiated cards
        Returns:
            p_hand(list of tuples) - The cards in a player's hand with
                                     the discard removed
            discard(tuple) - An enum_erator, face value, and suit for the
                             card discarded
            spades_break(int) - Either a 1 or 0, used for boolean purposes
            set_suit(str) - The suit to be used in determining winner for a hand

        Side Effects:
            Modifies various card attributes depending on player, their discard,
            spades_break, and determines set_suit
        """

        if cards.turn[0] == 1:
            p_hand = cards.p1
            p_bid = cards.p1_bid
            p_disc = cards.p1disc

        if cards.turn[0] == 2:
            p_hand = cards.p2
            p_bid = cards.p2_bid
            p_disc = cards.p2disc

        if cards.turn[0] == 3:
            p_hand = cards.p3
            p_bid = cards.p3_bid
            p_disc = cards.p3disc

        if cards.turn[0] == 4:
            p_hand = cards.p4
            p_bid = cards.p4_bid
            p_disc = cards.p4disc

        min_suit = cards.min_suit(p_hand)
        max_suit = cards.max_suit(p_hand)

        while cards.spades_break == 1:
            if p_bid == 0:
                for enum_, face, suit in p_hand:
                    if (suit != "Spades"
                    and face in cards.lows
                    or face in cards.mids):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

                for enum_, face, suit in p_hand:
                    if suit == max_suit and max_suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

                    elif face in cards.lows and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

            for enum_, face, suit in p_hand:
                if (face in cards.mids
                or face in cards.lows
                and suit != "Spades"):
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    cards.set_suit = p_disc[2]
                    return p_hand, p_disc, cards.spades_break, cards.set_suit

            if p_bid != 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if face in cards.highs and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit != "Spades"
                    and face in cards.lows
                    or face in cards.mids
                    or suit == min_suit):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit
                for enum_, face, suit in p_hand:
                    if suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

            for enum_, face, suit in p_hand:
                if suit != "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    cards.set_suit = p_disc[2]
                    return p_hand, p_disc, cards.spades_break, cards.set_suit

            for enum_, face, suit in p_hand:
                if suit == "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    cards.set_suit = p_disc[2]
                    return p_hand, p_disc, cards.spades_break, cards.set_suit



        while cards.spades_break == 0:
            if p_bid == 0:
                for enum_, face, suit in p_hand:
                    if suit == min_suit and face in cards.lows:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

                    elif suit == max_suit and face not in cards.highs:

                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

                        for enum_, face, suit in p_hand:
                            p_disc = (enum_, face, suit)
                            p_hand.remove(p_disc)
                            cards.spades_break = 0
                            cards.set_suit = p_disc[2]
                            return p_hand, p_disc, cards.spades_break, cards.set_suit

            if p_bid != 0:
                for enum_, face, suit in p_hand:
                    if suit == max_suit and face in cards.highs:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit

                    elif suit == min_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        cards.set_suit = p_disc[2]
                        return p_hand, p_disc, cards.spades_break, cards.set_suit
                for enum_, face, suit in p_hand:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    cards.set_suit = p_disc[2]
                    return p_hand, p_disc, cards.spades_break, cards.set_suit

        for enum_, face, suit in p_hand:
            if suit == "Spades":
                p_disc = (enum_, face, suit)
                p_hand.remove(p_disc)
                cards.spades_break = 0
                cards.set_suit = p_disc[2]
                return p_hand, p_disc, cards.spades_break, cards.set_suit

    def slog(self, cards):
        """ This method is to be used in determining an automated discard
        for a player taking the second turn

        Args:
            cards(class) - Cards class for a game of Spades

        Returns:
            p_hand(list of tuples) - The cards in a player's hand with the
                                     discard removed
            discard(tuple) - An enum_erator, face value, and suit for the card
                             discarded
            spades_break(int) - Either a 1 or 0, used for boolean purposes

        Side Effects:
            Modifies various card attributes depending on player, their discard
            and spades_break
        """
        if cards.turn[1] == 2:
            p_bid = cards.p2_bid
            p_hand = cards.p2
            p_disc = cards.p2disc

            mate_bid = cards.p4_bid
            first_disc = cards.p1disc

        elif cards.turn[1] == 3:
            p_bid = cards.p3_bid
            p_hand = cards.p3
            p_disc = cards.p3disc
            mate_bid = cards.p1_bid
            first_disc = cards.p2disc

        elif cards.turn[1] == 4:
            p_bid = cards.p4_bid
            p_hand = cards.p4
            p_disc = cards.p4disc
            mate_bid = cards.p2_bid
            first_disc = cards.p3disc

        elif cards.turn[1] == 1:
            p_bid = cards.p1_bid
            p_hand = cards.p1
            p_disc = cards.p1disc
            mate_bid = cards.p3_bid
            first_disc = cards.p4disc

        set_suit = cards.set_suit

        while cards.spades_break == 1:
            if p_bid != 0 and mate_bid == 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit == set_suit and enum_ > first_disc[0]):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                    elif suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            elif p_bid == 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit == set_suit
                    and enum_ < first_disc[0]
                    and suit == set_suit):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit != "Spades"
                    and suit == min_suit(p_hand)
                    or suit == max_suit(p_hand)):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit != "Spades"):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if suit == set_suit:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if suit != set_suit and suit != "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if suit == "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

        while cards.spades_break == 0:
            if p_bid != 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == set_suit and enum_ > first_disc[0]:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in sorted(p_hand):
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in sorted(p_hand):
                    if suit != set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == "Spades" and enum_ > first_disc[0]:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

            elif p_bid == 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == set_suit and enum_ < first_disc[0]:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit != set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
            for enum_, face, suit in p_hand:
                if suit == set_suit:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break
            for enum_, face, suit in p_hand:
                if suit != set_suit:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

    def tlog(self, cards):
        """ Used in determining an automated discard for player discarding third
        Args:
            cards(class) - Class of instantiated cards

        Returns:
            p_hand(list of tuples) - The cards in a player's hand with
                                     the discard removed
            discard(tuple) - An enum_erator, face value, and suit for
                             the card discarded
            spades_break(int) - Either a 1 or 0, used for boolean purposes

        Side Effects:
            Modifies various card attributes depending on player, their discard
            and spades_break
        """
        if cards.turn[2] == 1:
            p_hand = cards.p1
            p_bid = cards.p1_bid
            p_disc = cards.p1disc

            mate_bid = cards.p3_bid
            mate_disc = cards.p3disc

            opp_disc = cards.p4disc

        if cards.turn[2] == 2:
            p_hand =cards.p2
            p_bid = cards.p2_bid
            p_disc = cards.p2disc

            mate_bid = cards.p4_bid
            mate_disc = cards.p4disc

            opp_disc = cards.p1disc

        if cards.turn[2] == 3:
            p_hand = cards.p3
            p_bid = cards.p3_bid
            p_disc = cards.p3disc

            mate_bid = cards.p1_bid
            mate_disc = cards.p1disc

            opp_disc = cards.p2disc

        if cards.turn[2] == 4:
            p_hand = cards.p4
            p_bid = cards.p4_bid
            p_disc = cards.p4disc

            mate_bid = cards.p2_bid
            mate_disc = cards.p2disc

            opp_disc = cards.p3disc

        mate_suit = mate_disc[2]
        mate_enum_ = mate_disc[0]

        opp_enum_ = opp_disc[0]
        opp_suit = opp_disc[2]
        set_suit = cards.set_suit
        while cards.spades_break == 1:
            if (p_bid != 0
            and mate_enum_ < opp_enum_
            and set_suit == opp_suit):
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == set_suit and enum_ > opp_enum_:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    return p_hand, p_disc, cards.spades_break

            elif p_bid != 0 and mate_enum_ > opp_enum_:
                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            elif p_bid == 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit == set_suit
                    and enum_ < mate_enum_
                    or enum_ < opp_enum_):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if suit == set_suit:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if p_bid != 0 and suit == "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if suit != set_suit and suit != "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if suit == "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

        while cards.spades_break == 0:
            if (p_bid != 0
            and mate_enum_ < opp_enum_
            and set_suit == opp_suit):
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == set_suit and enum_ > opp_enum_:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
            elif (p_bid != 0
                 and mate_enum_ < opp_enum_
                 and opp_suit != set_suit):
                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

            elif p_bid != 0 and mate_enum_ > opp_enum_:
                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

            elif p_bid == 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit == set_suit
                    and enum_ < opp_enum_
                    or enum_ < mate_enum_):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                p_disc = (enum_, face, suit)
                p_hand.remove(p_disc)
                cards.spades_break = 0
                return p_hand, p_disc, cards.spades_break

    def four_log(self, cards):
        """ Determines an automated discard for a player taking the fourth turn

        Args:
            cards (class) - Class of cards to be used in a game of spades

        Returns:
            p_hand(list of tuples) - The cards in a player's hand with
                                     the discard removed
            discard(tuple) - An enum_erator, face value, and suit for the
                             card discarded
            spades_break(int) - Either a 1 or 0, used for boolean purposes
        Side Effects:
            Modifies various card attributes depending on player, their discard
            and spades_break
        """
        if cards.turn[3] == 1:
            p_hand = cards.p1
            p_bid = cards.p1_bid
            p_disc = cards.p1disc

            mate_bid = cards.p3_bid
            mate_disc = cards.p3disc
            opp_disc = cards.p2disc
            opp2_disc = cards.p4disc

        if cards.turn[3] == 2:
            p_hand = cards.p2
            p_bid = cards.p2_bid
            p_disc = cards.p2disc

            mate_bid = cards.p4_bid
            mate_disc = cards.p4disc
            opp_disc = cards.p1disc
            opp2_disc = cards.p3disc

        if cards.turn[3] == 3:
            p_hand = cards.p3
            p_bid = cards.p3_bid
            p_disc = cards.p3disc

            mate_bid = cards.p1_bid
            mate_disc = cards.p1disc

            opp_disc = cards.p2disc
            opp2_disc = cards.p4disc

        if cards.turn[3] == 4:
            p_hand = cards.p4
            p_bid = cards.p4_bid
            p_disc = cards.p4disc

            mate_bid = cards.p2_bid
            mate_disc = cards.p2disc
            opp_disc = cards.p1disc
            opp2_disc = cards.p3disc

        set_suit = cards.set_suit
        mate_suit = mate_disc[2]
        mate_enum_ = mate_disc[0]

        opp_enum_ = opp_disc[0]
        opp2_suit = opp2_disc[2]
        opp2_enum_ = opp2_disc[0]

        while cards.spades_break == 1:
            if (p_bid != 0
            and mate_enum_ < opp_enum_
            or mate_enum_ < opp2_enum_):
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit == set_suit
                    and enum_ > opp_enum_
                    and enum_ > opp2_enum_) :
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if (suit == set_suit
                    and enum_ < opp_enum_
                    and enum_ < opp2_enum_):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            elif p_bid != 0:
                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            elif (p_bid != 0
            and mate_enum_ > opp_enum_
            and mate_enum_ > opp_enum_
            or mate_suit == set_suit):
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == set_suit and enum_ < mate_enum_:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            elif p_bid == 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit == set_suit
                    and (enum_ < opp_enum_
                    or enum_ < mate_enum_
                    or enum_ < opp2_enum_)):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    if suit != set_suit and suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 1
                        return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                if suit == set_suit:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    return p_hand, p_disc, cards.spades_break
            for enum_, face, suit in p_hand:
                if suit != set_suit and suit != "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 1
                    return p_hand, p_disc, cards.spades_break
            for enum_, face, suit in p_hand:
                if suit != set_suit and suit == "Spades":
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

        while cards.spades_break == 0:
            if (p_bid != 0
            and mate_enum_ < opp_enum_
            or mate_enum_ < opp2_enum_):

                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if suit == set_suit and enum_ > opp_enum_:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

            elif (p_bid != 0
            and mate_enum_ > opp_enum_
            and mate_enum_ > opp2_enum_):

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

            elif p_bid == 0:
                for enum_, face, suit in sorted(p_hand, reverse = True):
                    if (suit == set_suit
                    and enum_ < opp_enum_
                    or enum_ < mate_enum_
                    or enum_ < opp2_enum_):
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit == set_suit:
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break

                for enum_, face, suit in p_hand:
                    if suit != "Spades":
                        p_disc = (enum_, face, suit)
                        p_hand.remove(p_disc)
                        cards.spades_break = 0
                        return p_hand, p_disc, cards.spades_break
                for enum_, face, suit in p_hand:
                    p_disc = (enum_, face, suit)
                    p_hand.remove(p_disc)
                    cards.spades_break = 0
                    return p_hand, p_disc, cards.spades_break

            for enum_, face, suit in p_hand:
                p_disc = (enum_, face, suit)
                p_hand.remove(p_disc)
                cards.spades_break = 0
                return p_hand, p_disc, cards.spades_break

    def player_disc(self, player, turn, cards):
        """
        This method is used to generate a discard for a player based on the
        turn they are taking

        Args:
            player(int) - The number of the player whose turn it is
            turn(int) - The number in the order the player is discarding
            spades_break(1/0) - Boolean value used to indicate when Spades are
                                eligible

        Returns:
            p_hand(list of tuples) - The cards left in a player's hand
            p_disc(tuple) - The card which the player discarded
            spades_break(1/0) - Used for boolean purposes
            set_suit - The suit used in determining a winner of 4 discards
        """
        if player == 2 and turn == 1:
            return self.flog(cards)
        elif player == 2 and turn == 2:
            return self.slog(cards)
        elif player == 2 and turn == 3:
            return self.tlog(cards)
        elif player == 2 and turn == 4:
            return self.four_log(cards)

        elif player == 3 and turn == 1:
            return self.flog(cards)
        elif player == 3 and turn == 2:
            return self.slog(cards)
        elif player == 3 and turn == 3:
            return self.tlog(cards)
        elif player == 3 and turn == 4:
            return self.four_log(cards)

        elif player == 4 and turn == 1:
            return self.flog(cards)
        elif player == 4 and turn == 2:
            return self.slog(cards)
        elif player == 4 and turn == 3:
            return self.tlog(cards)
        elif player == 4 and turn == 4:
            return self.four_log(cards)

    def comp_discards(self, cards):
        """
        Used in automating discards for computer players before the user discard

        Args:
            cards(class) - The current state of a given cards_class

        Returns:
            * Will return different attributes depending on turn including:
            cards.p2-cards.p4 (list of tuples) - Updated hand of cards for a CPU
                                                 player after discarding
            cards.set_suit (str) - The suit used needed for disc logic, and
                                   determining the winner for a set of discards
            cards.spades_break (int) - Boolean value (1/0) indicates if Spades
                                       are currently openly playable
            cards.p2disc-cards.p4disc (tuple) - The card a CPU player discarded

        Side Effects:
            Will alter various attributes of cards_class passed as arg based
            on cards.turn
        """
        if cards.turn[0] == 1:
            return
        if cards.turn[0] == 2:
            (cards.p2, cards.p2disc, cards.spades_break, cards.set_suit) = self.flog(cards)
            (cards.p3, cards.p3disc, cards.spades_break) = self.slog(cards)
            (cards.p4, cards.p4disc, cards.spades_break) = self.tlog(cards)
            return cards.p2, cards.p2disc, cards.p3, cards.p3disc, cards.p4,\
                   cards.p4disc, cards.spades_break, cards.set_suit
        elif cards.turn[0] == 3:
            (cards.p3, cards.p3disc, cards.spades_break, cards.set_suit) = self.flog(cards)
            (cards.p4, cards.p4disc, cards.spades_break) = self.slog(cards)
            return cards.p3, cards.p3disc, cards.p4, cards.p4disc,\
                   cards.spades_break, cards.set_suit
        elif cards.turn[0] == 4:
            (cards.p4, cards.p4disc, cards.spades_break, cards.set_suit) = self.flog(cards)
            return cards.p4, cards.p4disc, cards.spades_break, cards.set_suit

    def after_user_disc(self, cards, p1disc):
        """
        This function is used to automate discards for computer players,
        while accounting for the order of turns, and only returning discards
        up to the point of the users turn

        Args:
            cards(Class) - The cards class being used within a program
            discard(Class) - The Discard class used for logic in discards

        Returns:
            UPDATED ATTRIBUTES FOR:
            cards.spades_break - any cards_class state
            cards.p2           - if class.turn[0] == {1,3,4}
            cards.p2disc       - if class.turn[0] == {1,3,4}
            cards.p3           - if class.turn[0] == {1,4}
            cards.p3disc       - if class.turn[0] == {1,4}
            cards.p4           - if class.turn[0] == 1
            cards.p4disc       - if class.turn[0] == 1
            cards.set_suit     - if class.turn[0] == 1

        Side effects - Alters variables within cards_class
        """
        if cards.spades_break == 1 and p1disc[2] == "Spades":
            p1_sp = 0
        if cards.spades_break == 1 and p1disc[2] != "Spades":
            p1_sp = 1
        if cards.spades_break == 0:
            p1_sp = 0
        cards.p1disc = p1disc
        cards.spades_break = p1_sp
        cards.p1.remove(p1disc)
        if cards.turn[0] == 1:
            cards.set_suit = p1disc[2]
            (cards.p2, cards.p2disc, cards.spades_break) = self.slog(cards)
            (cards.p3, cards.p3disc, cards.spades_break) = self.tlog(cards)
            (cards.p4, cards.p4disc, cards.spades_break) = self.four_log(cards)
            return cards.p1, cards.p1disc, cards.p2, cards.p2disc, cards.p3,\
            cards.p3disc, cards.p4, cards.p4disc, cards.set_suit, cards.spades_break



        elif cards.turn[1] == 1:
            (cards.p2, cards.p2disc, cards.spades_break) = self.tlog(cards)
            (cards.p3, cards.p3disc, cards.spades_break) = self.four_log(cards)
            return\
            cards.p1, cards.p1disc, cards.p2, cards.p2disc, cards.p3,\
            cards.p3disc, cards.spades_break

        elif cards.turn[2] == 1:
            (cards.p2, cards.p2disc, cards.spades_break) = self.four_log(cards)
            return cards.p1, cards.p1disc, cards.p2, cards.p2disc,\
            cards.spades_break

        elif cards.turn[3] == 1:
            return cards.p1, cards.p1disc, cards.spades_break
