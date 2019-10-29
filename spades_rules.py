"""
This module is intended to create rules for a game of Spades,
account for scoring within the game, and ensure the game flows without
erroneous discards
"""
from spades_functions import *
from spades_cards import Cards
import pandas as pd
import numpy as np
import math
import random

class Rules(Cards):
    def __init__(self):
        Cards.__init__(self)
    def game_winner(self, cards, num):
        """ This method determines whether a team has won or not """
        if (cards.team1_score == cards.team1_score
            and cards.team1_score > num):
            return None
        elif cards.team1_score > num:
            cards.game_winner = cards.team1
            return cards.game_winner
        elif cards.team1_score > num:
            cards.game_winner = cards.team2
            return cards.game_winner

    def add_frame(self, n, df, p1_disc, p2_disc, p3_disc, p4_disc, winner):
        """
        This method is used to update a data frame with a new column,
        while accounting for the winner
        """
        p_handle = "Player "+ str(winner)
        rd_handle = "Rd" + str(n)

        df[rd_handle]['Player 1'] = p1_disc
        df[rd_handle]['Player 2'] = p2_disc
        df[rd_handle]['Player 3'] = p3_disc
        df[rd_handle]['Player 4'] = p4_disc
        df[rd_handle]['Winner'] = winner
        df["Wins"][p_handle] += 1
        return df

    def add_rnd_calc(self, df):
        """
        This method is to be used at the end of a round for calculating scores
        for both teams
        """
        for num in range(1,4):
            if num == 3:
                return df
            elif num == 1:
                mate = 3
            elif num == 2:
                mate = 4

            wins = df["Wins"]["Player " + str(num)]
            bids = df["Bids"]["Player " + str(num)]
            bags = wins - bids

            mate_wins = df["Wins"]["Player " + str(mate)]
            mate_bids = df["Bids"]["Player " + str(mate)]
            mate_bags = mate_wins - mate_bids

            team_wins = wins + mate_wins
            team_bids = bids + mate_bids
            team_bags = bags + mate_bags

    def round_frame(self):
        """
        This method is to be used in conjunction with acquired attributes gained
        during round, to return a score dataframe for an individual round
        """
        self.round_frame = add_frame(self.round, self.score_frame, \
                            self.p1_disc, self.p2_disc, self.p3_disc,\
                            self.p4_disc, self.winner)
        return self.round_frame

    def winner_(self, cards, p1disc, p2disc, p3disc, p4disc, set_suit):
        """ This method determines the winner based on 4 discards
        It's contingent upon the discard params being in player order 1234
            a = enum_
            b = face
            c = suit
        Returns:
            winner(int) - An integer 1-4 representing the player that won"""
        for a, b, c in sorted(set([p1disc, p2disc, p3disc,\
                                  p4disc]), reverse = True):
            if c == set_suit or c == "Spades":
                if (a,b,c) == p1disc:
                    cards.turn = [1,2,3,4]
                    cards.winner = 1
                if(a,b,c) == p2disc:
                    cards.turn = [2,3,4,1]
                    cards.winner = 2
                if(a,b,c) == p3disc:
                    cards.turn = [3,4,1,2]
                    cards.winner = 3
                if(a,b,c) == p4disc:
                    cards.turn = [4,1,2,3]
                    cards.winner = 4
                return cards.winner, cards.turn
