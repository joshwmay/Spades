import random
import math
import pandas as pd

def counter(player_hand):
    """This function counts occurrences of suits within a players hand
    Args:
        player_hand(list of tuples) - The playing cards a player has in a game

    Returns:
        count_hearts(int) - Number of hearts in hand
        count_clubs(int) - Number of clubs in hand
        count_diamonds(int) - Number of diamonds in hand
        count_spades(int) - Number of spades in hand
    """
    count_hearts = 0
    count_clubs = 0
    count_diamonds = 0
    count_spades = 0

    for i in player_hand:
        if "Hearts" in i:
            count_hearts = count_hearts + 1
        if "Clubs" in i:
            count_clubs = count_clubs + 1
        if "Diamonds" in i:
            count_diamonds = count_diamonds + 1
        if "Spades" in i:
            count_spades = count_spades + 1
    return count_hearts, count_clubs, count_diamonds, count_spades


def spades_deck():
    """
    This function creates a deck of cards to be used in a game of spades

    Returns:
        ready_to_shuffle(list) - An indexed list of card tuples grouped by suit,
                                 in ascending order by face value and suit,
                                 with Spades being the highest indexed suit
    """
    ready_for_shuffle = []
    for num in range(1,53):
        if num < 14 :
            suit = "Hearts"
            if num < 10:
                face = num + 1
        if 13 < num < 27:
            suit = "Clubs"
            if 13 < num < 23:
                face = (num + 1) - 13
        if 26 < num < 40:
            suit = "Diamonds"
            if 26 < num < 36:
                face = (num + 1) - (13 * 2)
        if 39 < num < 53:
            suit = "Spades"
            if 39 < num < 49:
                face = (num + 1) - (13 * 3)
        if (num == 10 or num == 23 or num == 36 or num == 49):
            face = "Jack"
        if (num == 11 or num == 24 or num == 37 or num == 50):
            face = "Queen"
        if (num == 12 or num == 25 or num == 38 or num == 51):
            face = "King"
        if (num == 13 or num == 26 or num == 39 or num == 52):
            face = "Ace"
        card_point = (num, face, suit)
        ready_for_shuffle +=  [card_point]
    return ready_for_shuffle

def shuffled(deck):
    """
    This function shuffles a deck of cards

    Args:
        deck(list or tuples) - A list of card tuples to be shuffled

    Returns:
        deck(list of tuples) - A shuffled deck of cards
    """
    for num in range(1000):
        random.shuffle(deck)
    return deck

def spades_deal(deck):
    """
    This function deals out cards to 4 players playing spades from a shuffled
    deck

    Args:
        deck(list of tuples) - A deck of cards to be shuffled for spades

    Returns:
        p1(list of tuples) - A list of tuples for player 1, to be used as cards
        p2(list of tuples) - A list of tuples for player 2, to be used as cards
        p3(list of tuples) - A list of tuples for player 3, to be used as cards
        p4(list of tuples) - A list of tuples for player 4, to be used as cards
    """
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    x = 0
    for i in deck:
        x = x + 1
        if x < 14:
            p1.append(i)
        if 13 < x < 27:
            p2.append(i)
        if 26 < x < 40:
            p3.append(i)
        if 39 < x < 53:
            p4.append(i)
    return sorted(p1), sorted(p2), sorted(p3), sorted(p4)

def bid(player):
    """
    This function serves to create automated bids for computer players in the
    game of spades

    Args:
        deal(multiple lists of tuples) - The playing cards for each player in
                                         a game of spades
    Returns:
        bid: An integer bid number
    """
    bid = 0
    spades = 0
    hearts = 0
    diamonds = 0
    clubs = 0
    for card in player:
        if card[0] in range(1,14):
            hearts += 1
        if card[0] in range(14,27):
            clubs += 1
        if card[0] in range(27,40):
            diamonds += 1
        if card[0] in range(40,53):
            spades += 1
        if (card[1] == "Ace"
            or card[1] == "King"):
            bid += 1
    if hearts < 2 and spades > 2:
        bid += 2
    if diamonds < 2 and spades > 2:
        bid += 2
    if clubs < 2 and spades > 2:
        bid += 2
    if (hearts + diamonds + clubs) < 7 and spades > 5:
        bid += 1
    if ((hearts + diamonds + clubs) >= 12
       and (52,"Ace","Spades") not in player
       and (51, "King","Spades") not in player
       and (50, "Queen","Spades") not in player):
       bid = 0
    if bid < 0:
        bid = 1
    return bid

def initialize_spades(deck):
    """
    This function initiates a deck of cards intended for a game of spades,
    gives bids for 4 players, and returns a hand for each player

    Args:
        deck(list of tuples) - A shuffled list of sorted cards

    Returns:
        first_bid(int) - A randomized player set to bid and discard first
        p1(list of tuples) - A hand of cards for a player in spades
        p1_bid(int) - An automated bid number
        p2(list of tuples) - A hand of cards for a player in spades
        p2_bid(int) - An automated bid number
        p3(list of tuples) - A hand of cards for a player in spades
        p3_bid(int) - An automated bid number
        p4(list of tuples) - A hand of cards for a player in spades
        p4_bid(int) - An automated bid number
    """
    x = 0
    for i in deck: #Same structure could be used for
        x = x + 1
        if x == 1:
            p1 = i
            if (1,2,"Hearts") in p1:
                first_bid = 1
        if x == 2:
            p2 = i
            if (1,2,"Hearts") in p2:
                first_bid = 2
        if x == 3:
            p3 = i
            if (1,2,"Hearts") in p3:
                first_bid = 3
        if x == 4:
            p4 = i
            if (1,2,"Hearts") in p4:
                first_bid = 4
    if first_bid == 1:
        p1_bid = bid(p1)
        p2_bid = bid(p2)
        if p1_bid == 0:
            p3_bid = bid(p3) + 1
        if p1_bid > 0:
            p3_bid = bid(p3)
        if p2_bid == 0:
            p4_bid = bid(p4) + 1
        if p2_bid > 0:
            p4_bid = bid(p4)
        if p1_bid + p2_bid + p3_bid + p4_bid < 13:
            p4_bid = p4_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid < 10:
            p4_bid = p4_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid >= 13:
            p4_bid = p4_bid - 1
        first_bid = [1,2,3,4]
    if first_bid == 2:
        p2_bid = bid(p2)
        p3_bid = bid(p3)
        if p2_bid == 0:
            p4_bid = bid(p4) + 1
        if p2_bid > 0:
            p4_bid = bid(p4)
        if p3_bid == 0:
            p1_bid = bid(p1) + 1
        if p3_bid > 0:
            p1_bid = bid(p1)
        if p1_bid + p2_bid + p3_bid + p4_bid < 13:
            p1_bid = p1_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid < 10:
            p1_bid = p1_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid >= 14:
            p1_bid = p1_bid - 1
        first_bid = [2,3,4,1]
    if first_bid == 3:
        p3_bid = bid(p3)
        p4_bid = bid(p4)
        if p3_bid == 0:
            p1_bid = bid(p1) + 1
        if p3_bid > 0:
            p1_bid = bid(p1)
        if p4_bid == 0:
            p2_bid = bid(p2) + 1
        if p4_bid > 0:
            p2_bid = bid(p2)
        if p1_bid + p2_bid + p3_bid + p4_bid < 13:
            p2_bid = p2_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid < 10:
            p2_bid = p2_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid >= 14:
            p2_bid = p2_bid - 1
        first_bid = [3,4,1,2]
    if first_bid == 4:
        p4_bid = bid(p4)
        p1_bid = bid(p1)
        if p4_bid == 0:
            p2_bid = bid(p2) + 1
        if p4_bid > 0:
            p2_bid = bid(p2)
        if p1_bid == 0:
            p3_bid = bid(p3) + 1
        if p1_bid > 0:
            p3_bid = bid(p3)
        if p1_bid + p2_bid + p3_bid + p4_bid < 13:
            p3_bid = p3_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid < 10:
            p3_bid = p3_bid + 1
        if p1_bid + p2_bid + p3_bid + p4_bid >= 13:
            p3_bid = p3_bid - 1
        first_bid = [4,1,2,3]
    return first_bid , p1, p1_bid, p2, p2_bid, p3, p3_bid, p4, p4_bid
