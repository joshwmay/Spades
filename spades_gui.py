from spades_cards import Cards
from spades_discard import Discard
from spades_functions import *
from spades_rules import Rules
from pygame import mixer

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QComboBox, QPushButton, QTableWidgetItem, QSlider

import time
import webbrowser

class Ui_MainWindow(object):
    """
    This class creates a GUI environment for the card game 'Spades'.

    Attributes:
        round_score (PyQt5 Table Widget): details the results of every round
        master_score (PyQt5 Table Widget): details the total score
        p1_disc_spot (PyQt5 Object): The spot for discards for player 1.
            Above holds true for p2, p3, and p4

    Methods:
        setupUi(self, MainWindow, cards)
        star_place(self, cards)
        open_link(self, link)
        reset_discs(self, cards, disc_class, rules)
        on_click(self, index, cards, cardex, disc_class, rules)
        retranslateUi(self, MainWindow)
        display_card(self, n, cards, card)
        display_card_all(self, cards)
        clear_discard(self, cards)
        disc_click(self, cards, disc_class)
        p2disp(self, cards)
        p3disp(self, cards)
        p4disp(self, cards)
        bid_input(self, cards, disc_class)
        update_table_round(self, cards_class)
        update_table_bid(self, cards_class)
        update_score(self, cards)
        clickBid(self)
        clickcard(self)
        ui_winner(self, cards, rules, disc_class)
        takingturn(self)
        max_max_music_vol(self)
        max_music_vol(self)
        sev_five_music_vol(self)
        med_music_vol(self)
        min_music_vol(self)
        play_music(self)
        stop_music(self)
    """

    def setupUi(self, MainWindow, cards):
        """
        Sets up the GUI, according to the PyQt5 Designer.

        Args:
            MainWindow: MainWindow attribute as defined by PyQt5
            cards (cards object): An initialized cards class.

        """
        MainWindow.setObjectName("SpadesWindow")
        MainWindow.resize(1122, 944)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow) # ID main widget
        self.centralwidget.setObjectName("centralwidget") # Name main widget

        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-40, -60, 1261, 971))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background.png"))
        self.background.setObjectName("background")
        self.background.raise_()

        self.float_link = QtWidgets.QPushButton(self.centralwidget)
        self.float_link.setGeometry(QtCore.QRect(1000, 30, 100, 50))
        self.float_link.setText("Learn to Play")
        self.float_link.setObjectName("tutorial")
        self.float_link.raise_()

        self.round_score = QtWidgets.QTableWidget(self.centralwidget)
        self.round_score.setGeometry(QtCore.QRect(170, 690, 891, 161))
        self.round_score.setMaximumSize(QtCore.QSize(931, 16777215))

        font = QtGui.QFont()
        font.setPointSize(7)

        self.round_score.setFont(font)
        self.round_score.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.round_score.setAutoFillBackground(False)
        self.round_score.setStyleSheet("")
        self.round_score.setVerticalScrollBarPolicy(QtCore.\
                                                    Qt.ScrollBarAlwaysOff)

        self.round_score.setHorizontalScrollBarPolicy(QtCore.\
                                                      Qt.ScrollBarAlwaysOff)

        self.round_score.setAutoScroll(True)
        self.round_score.setAutoScrollMargin(40)
        self.round_score.setAlternatingRowColors(True)
        self.round_score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.round_score.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.round_score.setSelectionMode(QtWidgets.QAbstractItemView.\
                                                    ExtendedSelection)
        self.round_score.setSelectionBehavior(QtWidgets.\
                                              QAbstractItemView.SelectRows)
        self.round_score.setGridStyle(QtCore.Qt.SolidLine)
        self.round_score.setWordWrap(True)
        self.round_score.setCornerButtonEnabled(False)
        self.round_score.setRowCount(5)
        self.round_score.setColumnCount(15)
        self.round_score.setObjectName("round_score")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        for n in range(0,5):
            self.round_score.setVerticalHeaderItem(n, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)

        for n in range(0,15):
            self.round_score.setHorizontalHeaderItem(n, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(8)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)


        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)

        self.round_score.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)

        self.round_score.setItem(4, 1, item)
        self.round_score.horizontalHeader().setVisible(True)
        self.round_score.horizontalHeader().setCascadingSectionResizes(False)
        self.round_score.horizontalHeader().setDefaultSectionSize(55)
        self.round_score.horizontalHeader().setMinimumSectionSize(60)
        self.round_score.verticalHeader().setDefaultSectionSize(25)


        item = QtWidgets.QTableWidgetItem(0)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        item.setFont(font)
        self.round_score.setItem(0,0, item)

        item = QtWidgets.QTableWidgetItem(0)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        item.setFont(font)
        self.round_score.setItem(1,0, item)

        item = QtWidgets.QTableWidgetItem(0)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        item.setFont(font)
        self.round_score.setItem(2,0, item)

        item = QtWidgets.QTableWidgetItem(0)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(75)
        item.setFont(font)
        self.round_score.setItem(3,0, item)

        self.drops = []

        self.discard_box = QtWidgets.QGroupBox(self.centralwidget)
        self.discard_box.setGeometry(QtCore.QRect(299, 109, 491, 411))
        self.discard_box.setTitle("")
        self.discard_box.setObjectName("discard_box")
        self.p3_disc_spot = QtWidgets.QLabel(self.discard_box)
        self.p3_disc_spot.setGeometry(QtCore.QRect(210, 40, 81, 111))
        self.p3_disc_spot.setStyleSheet("border-color: rgb(25, 25, 25);\n"
        "background-color: rgb(118, 118, 118);")
        self.p3_disc_spot.setObjectName("p3_disc_spot")
        self.gridLayout = QtWidgets.QGridLayout(self.p3_disc_spot)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.p1_disc_spot = QtWidgets.QLabel(self.discard_box)
        self.p1_disc_spot.setGeometry(QtCore.QRect(210, 270, 81, 111))
        self.p1_disc_spot.setStyleSheet("border-color: rgb(25, 25, 25);\n"
        "background-color: rgb(118, 118, 118);")
        self.p1_disc_spot.setObjectName("p1_disc_spot")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.p1_disc_spot)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.p2_disc_spot = QtWidgets.QLabel(self.discard_box)
        self.p2_disc_spot.setGeometry(QtCore.QRect(30, 140, 81, 111))
        self.p2_disc_spot.setStyleSheet("border-color: rgb(25, 25, 25);\n"
        "background-color: rgb(118, 118, 118);")
        self.p2_disc_spot.setObjectName("p2_disc_spot")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.p2_disc_spot)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.p4_disc_spot = QtWidgets.QLabel(self.discard_box)
        self.p4_disc_spot.setGeometry(QtCore.QRect(380, 140, 81, 111))
        self.p4_disc_spot.setStyleSheet("border-color: rgb(25, 25, 25);\n"
        "background-color: rgb(118, 118, 118);")
        self.p4_disc_spot.setObjectName("p4_disc_spot")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.p4_disc_spot)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.turn_head = QtWidgets.QLabel(self.discard_box)
        self.turn_head.setGeometry(QtCore.QRect(self.star_place(cards)))
        self.turn_head.setPixmap(QtGui.QPixmap("star.png"))
        self.turn_head.raise_()

        mixer.init()
        self.playlist = list()
        self.playlist.append('01 - Ace of Spades.mp3')
        self.playlist.append('01 - The Gambler.mp3')
        self.playlist.append('04 - Queen Of Hearts.mp3')
        self.music_play_trigger = QtWidgets.QPushButton(self.centralwidget)
        self.music_play_trigger.setGeometry(QtCore.QRect(10, 475, 80, 25))
        self.music_play_trigger.setText("Next Song")
        self.music_play_trigger.setObjectName("music_play_trigger")
        self.music_play_trigger.clicked.connect(lambda:self.play_music())
        self.music_play_trigger.raise_()

        self.music_vol_min = QtWidgets.QPushButton(self.centralwidget)
        self.music_vol_min.setGeometry(QtCore.QRect(10, 430, 15, 20))
        self.music_vol_min.setText("")
        self.music_vol_min.setObjectName("volume_min")
        self.music_vol_min.clicked.connect(lambda:self.min_music_vol())
        self.music_vol_min.raise_()

        self.music_vol_med = QtWidgets.QPushButton(self.centralwidget)
        self.music_vol_med.setGeometry(QtCore.QRect(25, 420, 15, 30))
        self.music_vol_med.setText("")
        self.music_vol_med.setObjectName("volume_med")
        self.music_vol_med.clicked.connect(lambda:self.med_music_vol())
        self.music_vol_med.raise_()

        self.music_vol_sev_five = QtWidgets.QPushButton(self.centralwidget)
        self.music_vol_sev_five.setGeometry(QtCore.QRect(40, 410, 15, 40))
        self.music_vol_sev_five.setText("")
        self.music_vol_sev_five.setObjectName("volume_sev_five")
        self.music_vol_sev_five.clicked.connect(lambda:self.sev_five_music_vol())
        self.music_vol_sev_five.raise_()

        self.music_vol_max = QtWidgets.QPushButton(self.centralwidget)
        self.music_vol_max.setGeometry(QtCore.QRect(55, 400, 15, 50))
        self.music_vol_max.setText("")
        self.music_vol_max.setObjectName("volume_8_five")
        self.music_vol_max.clicked.connect(lambda:self.max_music_vol())
        self.music_vol_max.raise_()

        self.music_vol_max_max = QtWidgets.QPushButton(self.centralwidget)
        self.music_vol_max_max.setGeometry(QtCore.QRect(70, 390, 15, 60))
        self.music_vol_max_max.setText("")
        self.music_vol_max_max.setObjectName("volume_8_five")
        self.music_vol_max_max.clicked.connect(lambda:self.max_max_music_vol())
        self.music_vol_max_max.raise_()

        self.music_stop_trigger = QtWidgets.QPushButton(self.centralwidget)
        self.music_stop_trigger.setGeometry(QtCore.QRect(10, 450, 80, 25))
        self.music_stop_trigger.setText("Stop Music")
        self.music_stop_trigger.setObjectName("music_stop_trigger")
        self.music_stop_trigger.clicked.connect(lambda:self.stop_music())
        self.music_stop_trigger.raise_()

        self.p1cards = QtWidgets.QGroupBox(self.centralwidget)
        self.p1cards.setGeometry(QtCore.QRect(10, 550, 1051, 141))
        self.p1cards.setObjectName("self.p1cards")

        self.p2_cards = QtWidgets.QGroupBox(self.centralwidget)
        self.p2_cards.setGeometry(QtCore.QRect(90, 20, 171, 531))
        self.p2_cards.setTitle("")
        self.p2_cards.setObjectName("p2_cards")
        spacer = 30
        self.label1 = QtWidgets.QLabel(self.p2_cards)
        self.label1.setGeometry(QtCore.QRect(60, 1 * spacer, 101, 71))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("back.png"))

        self.label2 = QtWidgets.QLabel(self.p2_cards)
        self.label2.setGeometry(QtCore.QRect(60, 2 * spacer, 101, 71))
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("back.png"))

        self.label3 = QtWidgets.QLabel(self.p2_cards)
        self.label3.setGeometry(QtCore.QRect(60, 3 * spacer, 101, 71))
        self.label3.setText("")
        self.label3.setPixmap(QtGui.QPixmap("back.png"))

        self.label4 = QtWidgets.QLabel(self.p2_cards)
        self.label4.setGeometry(QtCore.QRect(60, 4 * spacer, 101, 71))
        self.label4.setText("")
        self.label4.setPixmap(QtGui.QPixmap("back.png"))

        self.label5 = QtWidgets.QLabel(self.p2_cards)
        self.label5.setGeometry(QtCore.QRect(60, 5 * spacer, 101, 71))
        self.label5.setText("")
        self.label5.setPixmap(QtGui.QPixmap("back.png"))

        self.label6 = QtWidgets.QLabel(self.p2_cards)
        self.label6.setGeometry(QtCore.QRect(60, 6 * spacer, 101, 71))
        self.label6.setText("")
        self.label6.setPixmap(QtGui.QPixmap("back.png"))

        self.label7 = QtWidgets.QLabel(self.p2_cards)
        self.label7.setGeometry(QtCore.QRect(60, 7 * spacer, 101, 71))
        self.label7.setText("")
        self.label7.setPixmap(QtGui.QPixmap("back.png"))

        self.label8 = QtWidgets.QLabel(self.p2_cards)
        self.label8.setGeometry(QtCore.QRect(60, 8 * spacer, 101, 71))
        self.label8.setText("")
        self.label8.setPixmap(QtGui.QPixmap("back.png"))

        self.label9 = QtWidgets.QLabel(self.p2_cards)
        self.label9.setGeometry(QtCore.QRect(60, 9 * spacer, 101, 71))
        self.label9.setText("")
        self.label9.setPixmap(QtGui.QPixmap("back.png"))

        self.label10 = QtWidgets.QLabel(self.p2_cards)
        self.label10.setGeometry(QtCore.QRect(60, 10 * spacer, 101, 71))
        self.label10.setText("")
        self.label10.setPixmap(QtGui.QPixmap("back.png"))

        self.label11 = QtWidgets.QLabel(self.p2_cards)
        self.label11.setGeometry(QtCore.QRect(60, 11 * spacer, 101, 71))
        self.label11.setText("")
        self.label11.setPixmap(QtGui.QPixmap("back.png"))


        self.label12 = QtWidgets.QLabel(self.p2_cards)
        self.label12.setGeometry(QtCore.QRect(60, 12 * spacer, 101, 71))
        self.label12.setText("")
        self.label12.setPixmap(QtGui.QPixmap("back.png"))

        self.label13 = QtWidgets.QLabel(self.p2_cards)
        self.label13.setGeometry(QtCore.QRect(60, 13 * spacer, 101, 71))
        self.label13.setText("")
        self.label13.setPixmap(QtGui.QPixmap("back.png"))

        self.p3_cards = QtWidgets.QGroupBox(self.centralwidget)
        self.p3_cards.setGeometry(QtCore.QRect(300, 0, 491, 111))
        self.p3_cards.setTitle("")
        self.p3_cards.setObjectName("p3_cards")

        self.label14 = QtWidgets.QLabel(self.p3_cards)
        self.label14.setGeometry(QtCore.QRect(30, 10, 71, 101))
        self.label14.setText("")
        self.label14.setPixmap(QtGui.QPixmap("back2.png"))

        self.label15 = QtWidgets.QLabel(self.p3_cards)
        self.label15.setGeometry(QtCore.QRect(30 * 2, 10, 71, 101))
        self.label15.setText("")
        self.label15.setPixmap(QtGui.QPixmap("back2.png"))

        self.label16 = QtWidgets.QLabel(self.p3_cards)
        self.label16.setGeometry(QtCore.QRect(30 * 3, 10, 71, 101))
        self.label16.setText("")
        self.label16.setPixmap(QtGui.QPixmap("back2.png"))

        self.label17 = QtWidgets.QLabel(self.p3_cards)
        self.label17.setGeometry(QtCore.QRect(30 * 4, 10, 71, 101))
        self.label17.setText("")
        self.label17.setPixmap(QtGui.QPixmap("back2.png"))

        self.label18 = QtWidgets.QLabel(self.p3_cards)
        self.label18.setGeometry(QtCore.QRect(30 * 5, 10, 71, 101))
        self.label18.setText("")
        self.label18.setPixmap(QtGui.QPixmap("back2.png"))

        self.label19 = QtWidgets.QLabel(self.p3_cards)
        self.label19.setGeometry(QtCore.QRect(30 * 6, 10, 71, 101))
        self.label19.setText("")
        self.label19.setPixmap(QtGui.QPixmap("back2.png"))

        self.label20 = QtWidgets.QLabel(self.p3_cards)
        self.label20.setGeometry(QtCore.QRect(30 * 7, 10, 71, 101))
        self.label20.setText("")
        self.label20.setPixmap(QtGui.QPixmap("back2.png"))

        self.label21 = QtWidgets.QLabel(self.p3_cards)
        self.label21.setGeometry(QtCore.QRect(30 * 8, 10, 71, 101))
        self.label21.setText("")
        self.label21.setPixmap(QtGui.QPixmap("back2.png"))

        self.label22 = QtWidgets.QLabel(self.p3_cards)
        self.label22.setGeometry(QtCore.QRect(30 * 9, 10, 71, 101))
        self.label22.setText("")
        self.label22.setPixmap(QtGui.QPixmap("back2.png"))

        self.label23 = QtWidgets.QLabel(self.p3_cards)
        self.label23.setGeometry(QtCore.QRect(30 * 10, 10, 71, 101))
        self.label23.setText("")
        self.label23.setPixmap(QtGui.QPixmap("back2.png"))

        self.label24 = QtWidgets.QLabel(self.p3_cards)
        self.label24.setGeometry(QtCore.QRect(30 * 11, 10, 71, 101))
        self.label24.setText("")
        self.label24.setPixmap(QtGui.QPixmap("back2.png"))

        self.label25 = QtWidgets.QLabel(self.p3_cards)
        self.label25.setGeometry(QtCore.QRect(30 * 12, 10, 71, 101))
        self.label25.setText("")
        self.label25.setPixmap(QtGui.QPixmap("back2.png"))

        self.label26 = QtWidgets.QLabel(self.p3_cards)
        self.label26.setGeometry(QtCore.QRect(30 * 13, 10, 71, 101))
        self.label26.setText("")
        self.label26.setPixmap(QtGui.QPixmap("back2.png"))

        self.p4_cards = QtWidgets.QGroupBox(self.centralwidget)
        self.p4_cards.setGeometry(QtCore.QRect(820, 30, 171, 531))
        self.p4_cards.setTitle("")
        self.p4_cards.setObjectName("p4_cards")

        self.label27 = QtWidgets.QLabel(self.p4_cards)
        self.label27.setGeometry(QtCore.QRect(10, 20 + (1 * 30), 101, 71))
        self.label27.setText("")
        self.label27.setPixmap(QtGui.QPixmap("back.png"))

        self.label28 = QtWidgets.QLabel(self.p4_cards)
        self.label28.setGeometry(QtCore.QRect(10, 20 + (2 * 30), 101, 71))
        self.label28.setText("")
        self.label28.setPixmap(QtGui.QPixmap("back.png"))

        self.label29 = QtWidgets.QLabel(self.p4_cards)
        self.label29.setGeometry(QtCore.QRect(10, 20 + (3 * 30), 101, 71))
        self.label29.setText("")
        self.label29.setPixmap(QtGui.QPixmap("back.png"))

        self.label30 = QtWidgets.QLabel(self.p4_cards)
        self.label30.setGeometry(QtCore.QRect(10, 20 + (4 * 30), 101, 71))
        self.label30.setText("")
        self.label30.setPixmap(QtGui.QPixmap("back.png"))

        self.label31 = QtWidgets.QLabel(self.p4_cards)
        self.label31.setGeometry(QtCore.QRect(10, 20 + (5 * 30), 101, 71))
        self.label31.setText("")
        self.label31.setPixmap(QtGui.QPixmap("back.png"))

        self.label32 = QtWidgets.QLabel(self.p4_cards)
        self.label32.setGeometry(QtCore.QRect(10, 20 + (6 * 30), 101, 71))
        self.label32.setText("")
        self.label32.setPixmap(QtGui.QPixmap("back.png"))

        self.label33 = QtWidgets.QLabel(self.p4_cards)
        self.label33.setGeometry(QtCore.QRect(10, 20 + (7 * 30), 101, 71))
        self.label33.setText("")
        self.label33.setPixmap(QtGui.QPixmap("back.png"))

        self.label34 = QtWidgets.QLabel(self.p4_cards)
        self.label34.setGeometry(QtCore.QRect(10, 20 + (8 * 30), 101, 71))
        self.label34.setText("")
        self.label34.setPixmap(QtGui.QPixmap("back.png"))

        self.label35 = QtWidgets.QLabel(self.p4_cards)
        self.label35.setGeometry(QtCore.QRect(10, 20 + (8 * 30), 101, 71))
        self.label35.setText("")
        self.label35.setPixmap(QtGui.QPixmap("back.png"))

        self.label36 = QtWidgets.QLabel(self.p4_cards)
        self.label36.setGeometry(QtCore.QRect(10, 20 + (9 * 30), 101, 71))
        self.label36.setText("")
        self.label36.setPixmap(QtGui.QPixmap("back.png"))

        self.label37 = QtWidgets.QLabel(self.p4_cards)
        self.label37.setGeometry(QtCore.QRect(10, 20 + (10 * 30), 101, 71))
        self.label37.setText("")
        self.label37.setPixmap(QtGui.QPixmap("back.png"))

        self.label38 = QtWidgets.QLabel(self.p4_cards)
        self.label38.setGeometry(QtCore.QRect(10, 20 + (11 * 30), 101, 71))
        self.label38.setText("")
        self.label38.setPixmap(QtGui.QPixmap("back.png"))

        self.label39 = QtWidgets.QLabel(self.p4_cards)
        self.label39.setGeometry(QtCore.QRect(10, 20 + (12 * 30), 101, 71))
        self.label39.setText("")
        self.label39.setPixmap(QtGui.QPixmap("back.png"))

        self.p2disp(cards)
        self.p3disp(cards)
        self.p4disp(cards)

        self.master_score = QtWidgets.QTableWidget(self.centralwidget)
        self.master_score.setGeometry(QtCore.QRect(10, 740, 151, 111))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.master_score.setFont(font)
        self.master_score.setAutoFillBackground(False)
        self.master_score.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.master_score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.master_score.setAutoScroll(False)
        self.master_score.setTabKeyNavigation(False)
        self.master_score.setProperty("showDropIndicator", False)
        self.master_score.setAlternatingRowColors(True)
        self.master_score.setGridStyle(QtCore.Qt.SolidLine)
        self.master_score.setCornerButtonEnabled(False)
        self.master_score.setRowCount(2)
        self.master_score.setColumnCount(2)
        self.master_score.setObjectName("master_score")

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.master_score.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)

        self.master_score.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.master_score.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.master_score.setHorizontalHeaderItem(1, item)
        self.master_score.horizontalHeader().setVisible(True)
        self.master_score.horizontalHeader().setCascadingSectionResizes(False)
        self.master_score.horizontalHeader().setDefaultSectionSize(45)
        self.master_score.horizontalHeader().setMinimumSectionSize(40)
        self.master_score.verticalHeader().setVisible(True)
        self.master_score.verticalHeader().setDefaultSectionSize(40)

        self.p1cards.raise_()
        self.discard_box.raise_()
        self.p2_cards.raise_()
        self.p3_cards.raise_()
        self.master_score.raise_()
        self.round_score.raise_()
        self.p4_cards.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName("menubar")
        self.menuSpades = QtWidgets.QMenu(self.menubar)
        self.menuSpades.setObjectName("menuSpades")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSpades.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.round_score.setItem(0, 1, QTableWidgetItem(str(cards.p1wins)))
        self.round_score.setItem(1, 1, QTableWidgetItem(str(cards.p2wins)))
        self.round_score.setItem(2, 1, QTableWidgetItem(str(cards.p3wins)))
        self.round_score.setItem(3, 1, QTableWidgetItem(str(cards.p4wins)))

    def star_place(self, cards):
        """
        Finds the location of the indicator for the current players turn.

        Args:
            cards (cards object): Used in order to determine who's turn it is.

        Returns:
            QRect object: The location to place the indicator
        """
        if cards.winner == 1:
            return QtCore.QRect(218, 180, 81, 111)
        if cards.winner == 2:
            return QtCore.QRect(120, 160, 81, 111)
        if cards.winner == 3:
            return QtCore.QRect(218, 125, 81, 111)
        if cards.winner == 4:
            return QtCore.QRect(300, 140, 81, 111)
        if cards.turn[0] == 1:
            return QtCore.QRect(218, 180, 81, 111)
        if cards.turn[0] == 2:
            return QtCore.QRect(120, 160, 81, 111)
        if cards.turn[0] == 3:
            return QtCore.QRect(218, 125, 81, 111)
        if cards.turn[0] == 4:
            return QtCore.QRect(300, 140, 81, 111)


    def open_link(self, link):
        """
        Opens a webrowser link, to be used for the tutorial.

        Args:
            link (string): The link to the website to be opened

        Returns:
            webrowser object: The website to be opened
        """
        return webbrowser.open(link)

    def reset_discs(self, cards, disc_class, rules):
        """
        Resets attributes at the end of the round. If the cards round is 14, it
        resets the game. Should probably be a cards method.

        Args:
            cards (cards object)
            disc_class (discard object)
            rules (rules object)

        Returns:
            cards attributes

        Side Effects:
            Sets player discards and set_suit to none, while increasong the
                round by one.
        """

        cards.p1disc = None
        cards.p2disc = None
        cards.p3disc = None
        cards.p4disc = None
        cards.set_suit = None
        cards.round += 1
        if cards.round == 14:
            self.update_score(cards)
            cards.reset_all(cards)
            self.setupUi(MainWindow, cards = cards)
            self.master_score.setItem(0, 0, QTableWidgetItem(str(cards.team1_score)))
            self.master_score.setItem(1, 0, QTableWidgetItem(str(cards.team2_score)))
            self.master_score.setItem(0,1, QTableWidgetItem(str(cards.team1_bags)))
            self.master_score.setItem(1,1, QTableWidgetItem(str(cards.team2_bags)))
            self.display_card_all(cards)
            cards.p1_bid = self.bid_input(cards, disc_class)[0]
            self.update_table_bid(cards)

            self.card1.clicked.connect(lambda: self.on_click(index = self.card1,\
                                     cards = cards, cardex = cards.c1, disc_class = disc_class,\
                                     rules = rules))
            self.card2.clicked.connect(lambda: self.on_click(index = self.card2,\
                                     cards = cards, cardex = cards.c2, disc_class = disc_class,\
                                     rules = rules))
            self.card3.clicked.connect(lambda: self.on_click(index = self.card3,\
                                     cards = cards, cardex = cards.c3, disc_class = disc_class,\
                                     rules = rules))
            self.card4.clicked.connect(lambda: self.on_click(index = self.card4,\
                                     cards = cards, cardex = cards.c4, disc_class = disc_class,\
                                     rules = rules))
            self.card5.clicked.connect(lambda: self.on_click(index = self.card5,\
                                     cards = cards, cardex = cards.c5, disc_class = disc_class,\
                                     rules = rules))
            self.card6.clicked.connect(lambda: self.on_click(index = self.card6,\
                                     cards = cards, cardex = cards.c6, disc_class = disc_class,\
                                     rules = rules))
            self.card7.clicked.connect(lambda: self.on_click(index = self.card7,\
                                     cards = cards, cardex = cards.c7, disc_class = disc_class,\
                                     rules = rules))
            self.card8.clicked.connect(lambda: self.on_click(index = self.card8,\
                                     cards = cards, cardex = cards.c8, disc_class = disc_class,\
                                     rules = rules))
            self.card9.clicked.connect(lambda: self.on_click(index = self.card9,\
                                     cards = cards, cardex = cards.c9, disc_class = disc_class,\
                                     rules = rules))
            self.card10.clicked.connect(lambda: self.on_click(index = self.card10,\
                                    cards = cards, cardex = cards.c10, disc_class = disc_class,\
                                    rules = rules))
            self.card11.clicked.connect(lambda: ui.on_click(index = ui.card11,\
                                    cards = cards, cardex = cards.c11, disc_class = disc_class,\
                                    rules = rules))
            self.card12.clicked.connect(lambda: self.on_click(index = self.card12,\
                                    cards = cards, cardex = cards.c12, disc_class = disc_class,\
                                    rules = rules))
            ui.card13.clicked.connect(lambda: ui.on_click(index = ui.card13,\
                                    cards = cards, cardex = cards.c13, disc_class = disc_class,\
                                    rules = rules))
        return cards.p1disc, cards.p2disc, cards.p3disc, cards.p4disc,\
               cards.set_suit, cards.round

    def on_click(self, index, cards, cardex, disc_class, rules):
        """
        Discards a card when it is clicked, and computer player cards after.

        Args:
            index: card gui object
            cards: cards class
            cardex (tuple): The card to be discarded
            disc_class
            rules

        Returns:
            Just used to call other methods

        """
        if cards.started == 1:
            index.hide()
            cards.started = 0
            cards.p1disc = cardex
            if cards.turn[0] == 1:
                cards.set_suit = cardex[2]
                return print("cards.turn[0] == 1; user disc r" + str(cards.round)),\
        disc_class.after_user_disc(cards, cards.p1disc),\
        self.p1_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p1disc[0])+".png")),\
        QtTest.QTest.qWait(500),\
        self.p2_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p2disc[0])+".png")),\
        self.p2disp(cards),\
        QtTest.QTest.qWait(500),\
        self.p3_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p3disc[0])+".png")),\
        self.p3disp(cards),\
        QtTest.QTest.qWait(500),\
        self.p4_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p4disc[0])+".png")),\
        self.p4disp(cards),\
        cards.started, self.ui_winner(cards, rules, disc_class),\
        self.turn_head.setGeometry(QtCore.QRect(self.star_place(cards))),\
        self.turn_head.raise_()
            if cards.turn[1] == 1:
                return print("cards.turn[1] == 1; user disc r" + str(cards.round)),\
        disc_class.after_user_disc(cards, cards.p1disc),\
        self.p1_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p1disc[0])+".png")),\
        QtTest.QTest.qWait(500),\
        self.p2_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p2disc[0])+".png")),\
        self.p2disp(cards),\
        QtTest.QTest.qWait(500),\
        self.p3_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p3disc[0])+".png")),\
        self.p3disp(cards),\
        cards.started, self.ui_winner(cards, rules, disc_class),\
        self.turn_head.setGeometry(QtCore.QRect(self.star_place(cards))),\
        self.turn_head.raise_()

            if cards.turn[2] == 1:
                return print("cards.turn[2] == 1; user disc r" + str(cards.round)),\
        disc_class.after_user_disc(cards, cards.p1disc),\
        self.p1_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p1disc[0])+".png")),\
        QtTest.QTest.qWait(500),\
        self.p2_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p2disc[0])+".png")),\
        self.p2disp(cards),\
        cards.started, self.ui_winner(cards, rules, disc_class),\
        self.turn_head.setGeometry(QtCore.QRect(self.star_place(cards))),\
        self.turn_head.raise_()

            if cards.turn[3] == 1:
                return print("cards.turn[3] == 1; user disc r" + str(cards.round)),\
         disc_class.after_user_disc(cards, cards.p1disc),\
        self.p1_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p1disc[0])+".png")),\
        cards.started, self.ui_winner(cards, rules, disc_class),\
        self.turn_head.setGeometry(QtCore.QRect(self.star_place(cards))),\
        self.turn_head.raise_()

    def retranslateUi(self, MainWindow):
        """
        Sets the text of many GUI elements. Created through PyQt5 designer.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.p1cards.setTitle(_translate("MainWindow", "Your Cards"))
        item = self.master_score.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Team1"))
        item = self.master_score.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Team2"))
        item = self.master_score.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Score"))
        item = self.master_score.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Bags"))
        self.round_score.setSortingEnabled(False)
        item = self.round_score.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player 1"))
        item = self.round_score.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Player 2"))
        item = self.round_score.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Player 3"))
        item = self.round_score.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Player 4"))
        item = self.round_score.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Winner"))
        item = self.round_score.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bid"))
        item = self.round_score.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Wins"))
        item = self.round_score.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Discs R1"))
        item = self.round_score.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Discs R2"))
        item = self.round_score.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Discs R3"))
        item = self.round_score.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Discs R4"))
        item = self.round_score.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Discs R5"))
        item = self.round_score.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Discs R6"))
        item = self.round_score.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Discs R7"))
        item = self.round_score.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Discs R8"))
        item = self.round_score.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Discs R9"))
        item = self.round_score.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Discs R10"))
        item = self.round_score.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Discs R11"))
        item = self.round_score.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Discs R12"))
        item = self.round_score.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Discs R13"))
        __sortingEnabled = self.round_score.isSortingEnabled()
        self.round_score.setSortingEnabled(False)
        self.round_score.setSortingEnabled(__sortingEnabled)
        self.menuSpades.setTitle(_translate("MainWindow", "Spades"))

    def display_card(self, n, cards, card):

        """
        Displays a given card in the location of a specific place for player 1.

        Args:
            n (int): The number card to be displayed by p1.
            cards: cards object
            card (tuple): card to be discarded
        """

        spacer_pivot = 10
        spacer = 80
        if n == 1:
             card1_icon = QtGui.QIcon()
             card1_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                  QtGui.QIcon.Normal, QtGui.QIcon.Off)
             self.card1 = QtWidgets.QPushButton(self.p1cards)
             self.card1.setGeometry(QtCore.QRect(10, 20, 71, 101))

             self.card1.setIcon(card1_icon)
             self.card1.setIconSize(QtCore.QSize(256, 256))
             self.card1.setObjectName(str(card))
             self.card1.raise_()
             self.card1.show()
        if n == 2:

            card2_icon = QtGui.QIcon()
            card2_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card2 = QtWidgets.QPushButton(self.p1cards)
            self.card2.setGeometry(QtCore.QRect(1 * spacer + 10,\
                                                      20, 71, 101))

            self.card2.setIcon(card2_icon)
            self.card2.setIconSize(QtCore.QSize(256, 256))
            self.card2.setObjectName(str(card))
            self.card2.raise_()
            self.card2.show()
        if n == 3:
            card3_icon = QtGui.QIcon()
            card3_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card3 = QtWidgets.QPushButton(self.p1cards)
            self.card3.setGeometry(QtCore.QRect(2 * spacer + 10,\
                                                      20, 71, 101))

            self.card3.setIcon(card3_icon)
            self.card3.setIconSize(QtCore.QSize(256, 256))
            self.card3.setObjectName(str(card))
            self.card3.raise_()
            self.card3.show()
        if n == 4:
            card4_icon = QtGui.QIcon()
            card4_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card4 = QtWidgets.QPushButton(self.p1cards)
            self.card4.setGeometry(QtCore.QRect(3 * spacer + 10,\
                                                      20, 71, 101))

            self.card4.setIcon(card4_icon)
            self.card4.setIconSize(QtCore.QSize(256, 256))
            self.card4.setObjectName(str(card))
            self.card4.raise_()
            self.card4.show()
        if n == 5:
            card5_icon = QtGui.QIcon()
            card5_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card5 = QtWidgets.QPushButton(self.p1cards)
            self.card5.setGeometry(QtCore.QRect(4 * spacer + 10,\
                                                      20, 71, 101))

            self.card5.setIcon(card5_icon)
            self.card5.setIconSize(QtCore.QSize(256, 256))
            self.card5.setObjectName(str(card))
            self.card5.raise_()
            self.card5.show()
        if n == 6:
            card6_icon = QtGui.QIcon()
            card6_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card6 = QtWidgets.QPushButton(self.p1cards)
            self.card6.setGeometry(QtCore.QRect(5 * spacer + 10,\
                                                      20, 71, 101))

            self.card6.setIcon(card6_icon)
            self.card6.setIconSize(QtCore.QSize(256, 256))
            self.card6.setObjectName(str(card))
            self.card6.raise_()
            self.card6.show()
        if n == 7:
            card7_icon = QtGui.QIcon()
            card7_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card7 = QtWidgets.QPushButton(self.p1cards)
            self.card7.setGeometry(QtCore.QRect(6 * spacer + 10,\
                                                      20, 71, 101))

            self.card7.setIcon(card7_icon)
            self.card7.setIconSize(QtCore.QSize(256, 256))
            self.card7.setObjectName(str(card))
            self.card7.raise_()
            self.card7.show()
        if n == 8:
            card8_icon = QtGui.QIcon()
            card8_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card8 = QtWidgets.QPushButton(self.p1cards)
            self.card8.setGeometry(QtCore.QRect(7 * spacer + 10,\
                                                      20, 71, 101))

            self.card8.setIcon(card8_icon)
            self.card8.setIconSize(QtCore.QSize(256, 256))
            self.card8.setObjectName(str(card))
            self.card8.raise_()
            self.card8.show()
        if n == 9:
            card9_icon = QtGui.QIcon()
            card9_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card9 = QtWidgets.QPushButton(self.p1cards)
            self.card9.setGeometry(QtCore.QRect(8 * spacer + 10,\
                                                      20, 71, 101))

            self.card9.setIcon(card9_icon)
            self.card9.setIconSize(QtCore.QSize(256, 256))
            self.card9.setObjectName(str(card))
            self.card9.raise_()
            self.card9.show()
        if n == 10:
            card10_icon = QtGui.QIcon()
            card10_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card10 = QtWidgets.QPushButton(self.p1cards)
            self.card10.setGeometry(QtCore.QRect(9 * spacer + 10,\
                                                      20, 71, 101))

            self.card10.setIcon(card10_icon)
            self.card10.setIconSize(QtCore.QSize(256, 256))
            self.card10.setObjectName(str(card))
            self.card10.raise_()
            self.card10.show()
        if n == 11:
            card11_icon = QtGui.QIcon()
            card11_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card11 = QtWidgets.QPushButton(self.p1cards)
            self.card11.setGeometry(QtCore.QRect(10 * spacer + 10,\
                                                      20, 71, 101))

            self.card11.setIcon(card11_icon)
            self.card11.setIconSize(QtCore.QSize(256, 256))
            self.card11.setObjectName(str(card))
            self.card11.raise_()
            self.card11.show()
        if n == 12:
            card12_icon = QtGui.QIcon()
            card12_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card12 = QtWidgets.QPushButton(self.p1cards)
            self.card12.setGeometry(QtCore.QRect(11 * spacer + 10,\
                                                      20, 71, 101))

            self.card12.setIcon(card12_icon)
            self.card12.setIconSize(QtCore.QSize(256, 256))
            self.card12.setObjectName(str(card))
            self.card12.raise_()
            self.card12.show()
        if n == 13:
            card13_icon = QtGui.QIcon()
            card13_icon.addPixmap(QtGui.QPixmap(str(card[0])+".PNG"),
                                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.card13 = QtWidgets.QPushButton(self.p1cards)
            self.card13.setGeometry(QtCore.QRect(12 * spacer + 10,\
                                                      20, 71, 101))

            self.card13.setIcon(card13_icon)
            self.card13.setIconSize(QtCore.QSize(256, 256))
            self.card13.setObjectName(str(card))
            self.card13.raise_()
            self.card13.show()

    def display_card_all(self, cards):
        """
        Calls self.display_card for every card in a players hand.

        Args:
            cards
        """
        self.display_card(1, cards, cards.c1)
        self.display_card(2, cards, cards.c2)
        self.display_card(3, cards, cards.c3)
        self.display_card(4, cards, cards.c4)
        self.display_card(5, cards, cards.c5)
        self.display_card(6, cards, cards.c6)
        self.display_card(7, cards, cards.c7)
        self.display_card(8, cards, cards.c8)
        self.display_card(9, cards, cards.c9)
        self.display_card(10, cards, cards.c10)
        self.display_card(11, cards, cards.c11)
        self.display_card(12, cards, cards.c12)
        self.display_card(13, cards, cards.c13)




    def clear_discard(self, cards):
        """
        Resets the image of all 4 discard piles, to be used at the end of
         a round.

        Args:
            cards
        """
        self.p1_disc_spot.setPixmap(QtGui.QPixmap("back2.png"))
        self.p1_disc_spot.raise_()
        self.p2_disc_spot.setPixmap(QtGui.QPixmap("back2.png"))
        self.p2_disc_spot.raise_()
        self.p3_disc_spot.setPixmap(QtGui.QPixmap("back2.png"))
        self.p3_disc_spot.raise_()
        self.p4_disc_spot.setPixmap(QtGui.QPixmap("back2.png"))
        self.p4_disc_spot.raise_()

    def disc_click(self, cards, disc_class):
        """
        This is part of the engine of the game and operates to determine
            CPU discards, modify the window appropriately, and start the game.

        Args:
            cards
            disc_class
        """
        QtTest.QTest.qWait(500)
        cards.started = 1
        while (len(cards.p1) == len(cards.p2)
        and len(cards.p1) == len(cards.p3)
        and len(cards.p1) == len(cards.p4)):
            if cards.turn[0] == 1:
                return cards.started
            if cards.turn[0] == 2:
                return print("Trying... cards.turn[0] == 2"),\
                disc_class.comp_discards(cards = cards),\
     self.p2_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p2disc[0])+".png")),\
     self.p2disp(cards),\
     self.p3_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p3disc[0])+".png")),\
     self.p3disp(cards),\
     self.p4_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p4disc[0])+".png")),\
     self.p4disp(cards),\
     cards.started
            if cards.turn[0] == 3:
                return disc_class.comp_discards(cards),\
                       print("Trying... cards.turn[0] == 3"),\
     self.p3_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p3disc[0])+".png")),\
     self.p3disp(cards),\
     self.p4_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p4disc[0])+".png")),\
     self.p4disp(cards),\
     cards.started

            if cards.turn[0] == 4:
                return print("Trying... cards.turn[0] == 4"), disc_class.comp_discards(cards),\
    self.p4_disc_spot.setPixmap(QtGui.QPixmap(str(cards.p4disc[0])+".png")),\
    self.p4disp(cards),\
    cards.started

    def p2disp(self, cards):
        """
        Hides and shows the appropriate number of cards according to player 2's
         hand.

        Args:
            cards
        """
        n = len(cards.p2)
        if n == 0:
            self.label1.hide()
        if n == 1:
            self.label2.hide()
        if n == 2:
            self.label3.hide()
        if n == 3:
            self.label4.hide()
        if n == 4:
            self.label5.hide()
        if n == 5:
            self.label6.hide()
        if n == 6:
            self.label7.hide()
        if n == 7:
            self.label8.hide()
        if n == 8:
            self.label9.hide()
        if n == 9:
            self.label10.hide()
        if n == 10:
            self.label11.hide()
        if n == 11:
            self.label12.hide()
        if n == 12:
            self.label13.hide()
        if n == 13:
            self.label1.raise_()
            self.label2.raise_()
            self.label3.raise_()
            self.label4.raise_()
            self.label5.raise_()
            self.label6.raise_()
            self.label7.raise_()
            self.label8.raise_()
            self.label9.raise_()
            self.label10.raise_()
            self.label11.raise_()
            self.label12.raise_()
            self.label13.raise_()

    def p3disp(self, cards):
        """
        Hides and shows the appropriate number of cards according to player 3's
         hand.

        Args:
            cards
        """
        n = len(cards.p3)
        if n == 0:
            self.label14.hide()
        if n == 1:
            self.label15.hide()
        if n == 2:
            self.label16.hide()
        if n == 3:
            self.label17.hide()
        if n == 4:
            self.label18.hide()
        if n == 5:
            self.label19.hide()
        if n == 6:
            self.label20.hide()
        if n == 7:
            self.label21.hide()
        if n == 8:
            self.label22.hide()
        if n == 9:
            self.label23.hide()
        if n == 10:
            self.label24.hide()
        if n == 11:
            self.label25.hide()
        if n == 12:
            self.label26.hide()
        if n == 13:
            self.label14.raise_()
            self.label15.raise_()
            self.label16.raise_()
            self.label17.raise_()
            self.label18.raise_()
            self.label19.raise_()
            self.label20.raise_()
            self.label21.raise_()
            self.label22.raise_()
            self.label23.raise_()
            self.label24.raise_()
            self.label25.raise_()
            self.label26.raise_()


    def p4disp(self, cards):
        """
        Hides and shows the appropriate number of cards according to player 4's
         hand.

        Args:
            cards
        """
        n = len(cards.p4)
        if n == 0:
            self.label27.hide()
        if n == 1:
            self.label28.hide()
        if n == 2:
            self.label29.hide()
        if n == 3:
            self.label30.hide()
        if n == 4:
            self.label31.hide()
        if n == 5:
            self.label32.hide()
        if n == 6:
            self.label33.hide()
        if n == 7:
            self.label34.hide()
        if n == 8:
            self.label35.hide()
        if n == 9:
            self.label36.hide()
        if n == 10:
            self.label37.hide()
        if n == 11:
            self.label38.hide()
        if n == 12:
            self.label39.hide()
        if n == 13:
            self.label27.raise_()
            self.label28.raise_()
            self.label29.raise_()
            self.label30.raise_()
            self.label31.raise_()
            self.label32.raise_()
            self.label33.raise_()
            self.label34.raise_()
            self.label35.raise_()
            self.label36.raise_()
            self.label37.raise_()
            self.label38.raise_()
            self.label39.raise_()



    def bid_input(self, cards, disc_class):
        """
        Creates a widget for the user to input their desired bid.

        Args:
            cards
            disc_class

        Returns:
            (int): The bid of the user, player 1.
            Runs self.disc_click
        """
        print("starting bid method")
        self.bidBox = QComboBox(self.centralwidget)
        self.bidBox.setGeometry(QtCore.QRect(0, 300, 90, 25))
        self.bidBox.setObjectName(("comboBox"))

        self.bidBox.addItem('0')
        self.bidBox.addItem('1')
        self.bidBox.addItem('2')
        self.bidBox.addItem('3')
        self.bidBox.addItem('4')
        self.bidBox.addItem('5')
        self.bidBox.addItem('6')
        self.bidBox.addItem('7')
        self.bidBox.addItem('8')
        self.bidBox.addItem('9')
        self.bidBox.addItem('10')
        self.bidBox.addItem('11')
        self.bidBox.addItem('12')
        self.bidBox.addItem('13')

        self.suggested = QPushButton(self.centralwidget)
        self.suggested.setGeometry(QtCore.QRect(0, 250, 90, 25))
        self.suggested.setText("Suggested: " + str(cards.p1_bid))
        self.suggested.setObjectName("Suggested Bid")

        self.bidButton = QPushButton('Submit Bid', self.centralwidget)
        self.bidButton.setGeometry(QtCore.QRect(0, 275, 90, 25))
        self.bidButton.setToolTip('Select your bid.')
        self.bidButton.clicked.connect(self.clickBid)
        self.bidBox.show()
        self.bidButton.show()
        self.suggested.show()
        self.bidbool = 0
        print("entering loop")
        print(self.bidbool)
        while (self.bidbool == 0):
            QtCore.QCoreApplication.processEvents()
        self.bidBox.hide()
        self.bidButton.hide()
        self.suggested.hide()
        return int(self.bidBox.currentText()),\
               self.disc_click(cards, disc_class)


    def update_table_round(self, cards_class):
        """
        Updates the round table at the end of the round.

        Args:
            cards
        """
        if cards.winner == 1:
            cards.p1wins += 1
            cards.team1_wins += 1
            return cards.p1wins, cards.team1_wins,\
            self.round_score.setItem(0, 1, QTableWidgetItem(str(cards.p1wins)))
        elif cards.winner == 2:
            cards.p2wins += 1
            cards.team2_wins += 1
            return cards.p2wins, cards.team2_wins,\
            self.round_score.setItem(1, 1, QTableWidgetItem(str(cards.p2wins)))
        elif cards.winner == 3:
            cards.p3wins += 1
            cards.team1_wins += 1
            return cards.p3wins, cards.team1_wins,\
            self.round_score.setItem(2, 1, QTableWidgetItem(str(cards.p3wins)))
        elif cards.winner == 4:
            cards.p4wins += 1
            cards.team2_wins += 1
            return cards.p4wins, cards.team2_wins,\
            self.round_score.setItem(3, 1, QTableWidgetItem(str(cards.p4wins)))

    def update_table_bid(self, cards_class):
        """
        Updates the round table for bids.

        Args:
            cards_class
        """

        self.round_score.setItem(0, 0, QTableWidgetItem(str(cards_class.p1_bid)))
        self.round_score.setItem(1, 0, QTableWidgetItem(str(cards_class.p2_bid)))
        self.round_score.setItem(2, 0, QTableWidgetItem(str(cards_class.p3_bid)))
        self.round_score.setItem(3, 0, QTableWidgetItem(str(cards_class.p4_bid)))

    def update_score(self, cards): # In Progress
        """
        Updates the scoring table.

        Args:
            cards

        Returns:
            Each team's score and bags.
        """
        if cards.round != 14:
            return
        temp_bags1 = (cards.p1wins - cards.p1_bid)+(cards.p3wins - cards.p3_bid)
        if ((cards.p1_bid == 0 and cards.p1wins > 0)
         or (cards.p3_bid == 0 and cards.p3wins > 0)):
           cards.team1_score -= 100
           if temp_bags1 >= 0:
               cards.team1_score += temp_bags1
               cards.team1_bags += temp_bags1

        if ((cards.p1_bid == 0 and cards.p1wins == 0)
         or (cards.p3_bid == 0 and cards.p3wins == 0)):
           cards.team1_score += 100
           if temp_bags1 >= 0:
               cards.team1_score += temp_bags1
               cards.team1_bags += temp_bags1

        if (cards.p1_bid != 0 and cards.p3_bid != 0):
            if temp_bags1 < 0:
                cards.team1_score -= 50
            if temp_bags1 >= 0:
                cards.team1_score += (cards.p1_bid * 10) + (cards.p3_bid * 10)+\
                                     temp_bags1
                cards.team1_bags += temp_bags1

        if cards.team1_bags >= 10:
            cards.team1_bags = 0
            cards.team1_score -= 75

        cards.team2_wins = cards.p2wins + cards.p4wins
        temp_bags2 = (cards.p2wins - cards.p2_bid)+(cards.p4wins - cards.p4_bid)

        if ((cards.p2_bid == 0 and cards.p2wins > 0)
         or (cards.p4_bid == 0 and cards.p4wins > 0)):
           cards.team2_score -= 100

           if temp_bags >= 0:
               cards.team2_score += temp_bags2
               cards.team2_bags += temp_bags2

        if ((cards.p2_bid == 0 and cards.p2wins == 0)
         or (cards.p4_bid == 0 and cards.p4wins == 0)):
           cards.team2_score += 100
           if temp_bags2 >= 0:
               cards.team2_score += temp_bags2
               cards.team2_bags += temp_bags2

        if (cards.p2_bid != 0 and cards.p4_bid != 0):
            if temp_bags2 < 0:
                cards.team2_score -= 50
            if temp_bags2 >= 0:
                cards.team2_score += (cards.p2_bid * 10) + (cards.p4_bid * 10)+\
                                     temp_bags2
                cards.team2_bags += temp_bags2
        if temp_bags1 < 0:
            cards.team1_bags += 0
        if temp_bags2 < 0:
            cards.team2_bags += 0

        if cards.team2_bags >= 10:
            cards.team2_bags = 0
            cards.team2_score -= 75

        return cards.team1_score, cards.team1_bags,\
               cards.team2_score, cards.team2_bags

    def clickBid(self):
        """
        Changes bidbool to 1, exiting the loop to confirm the user's bid.

        Side Affects:
            Sets bidbool = 1.
        """
        self.bidbool = 1

    def clickcard(self):
        """
        Changes cardbool to 1, exiting the loop to confirm the user's card.

        Side Affects:
            Sets cardbool = 1.
        """
        self.cardbool = 1

    def ui_winner(self, cards, rules, disc_class):
        """
        Determines the winner after 4 discards and updates round score table.

        Args:
            cards
            rules
            disc_class

        Returns:
            Used to call other commands
        """
        winner = rules.winner_(cards, cards.p1disc, cards.p2disc, cards.p3disc,\
                               cards.p4disc, cards.set_suit)
        cards.winner = winner[0]
        cards.turn = winner[1]

        n = cards.round + 1
        QtTest.QTest.qWait(2000)
        self.clear_discard(cards)
        if cards.round != 14:
            p1_stdin = str(cards.p1disc[1]).strip("()").replace("'","")
            if cards.p1disc[2] == "Hearts":
                p1_stdin += " ♥"
            if cards.p1disc[2] == "Clubs":
                p1_stdin += " ♣"
            if cards.p1disc[2] == "Diamonds":
                p1_stdin += " ♦"
            if cards.p1disc[2] == "Spades":
                p1_stdin += " ♠"
            p2_stdin = str(cards.p2disc[1]).strip("()").replace("'","")
            if cards.p2disc[2] == "Hearts":
                p2_stdin += " ♥"
            if cards.p2disc[2] == "Clubs":
                p2_stdin += " ♣"
            if cards.p2disc[2] == "Diamonds":
                p2_stdin += " ♦"
            if cards.p2disc[2] == "Spades":
                p2_stdin += " ♠"
            p3_stdin = str(cards.p3disc[1]).strip("()").replace("'","")
            if cards.p3disc[2] == "Hearts":
                p3_stdin += " ♥"
            if cards.p3disc[2] == "Clubs":
                p3_stdin += " ♣"
            if cards.p3disc[2] == "Diamonds":
                p3_stdin += " ♦"
            if cards.p3disc[2] == "Spades":
                p3_stdin += " ♠"
            p4_stdin = str(cards.p4disc[1]).strip("()").replace("'","")
            if cards.p4disc[2] == "Hearts":
                p4_stdin += " ♥"
            if cards.p4disc[2] == "Clubs":
                p4_stdin += " ♣"
            if cards.p4disc[2] == "Diamonds":
                p4_stdin += " ♦"
            if cards.p4disc[2] == "Spades":
                p4_stdin += " ♠"
            return print("Round: "+str(cards.round)),cards.winner, cards.turn,\
        self.round_score.setItem(0, n, QTableWidgetItem(p1_stdin)),\
        self.round_score.setItem(1, n, QTableWidgetItem(p2_stdin)),\
        self.round_score.setItem(2, n, QTableWidgetItem(p3_stdin)),\
        self.round_score.setItem(3, n, QTableWidgetItem(p4_stdin)),\
        self.round_score.setItem(4, n, QTableWidgetItem(str(cards.winner))),\
        self.update_table_round(cards), self.reset_discs(cards, disc_class, rules),\
        QtTest.QTest.qWait(500), self.disc_click(cards = cards, disc_class = disc_class)

    def takingturn(self):
        """
        Waits until the player finishes taking their turn to progress.
        """

        self.cardbool = 0
        while (self.cardbool == 0):
            QtCore.QCoreApplication.processEvents()

    def max_max_music_vol(self):
        """
        Sets the music volume to the highest setting.
        """
        mixer.music.set_volume(1.0)

    def max_music_vol(self):
        """
        Sets the music volume to a high setting.
        """
        mixer.music.set_volume(0.85)

    def sev_five_music_vol(self):
        """
        Sets the music volume to a medium-high setting.
        """
        mixer.music.set_volume(0.60)

    def med_music_vol(self):
        """
        Sets the music volume to a medium setting.
        """
        mixer.music.set_volume(0.5)

    def min_music_vol(self):
        """
        Sets the music volume to a low setting.
        """
        mixer.music.set_volume(0.25)

    def play_music(self):
        """
        Plays the music.
        """
        if len(self.playlist):
            mixer.music.load(self.playlist.pop())
            mixer.music.play()
        else:
            self.playlist.append('01 - Ace of Spades.mp3')
            self.playlist.append('01 - The Gambler.mp3')
            self.playlist.append('04 - Queen Of Hearts.mp3')
            mixer.music.load(self.playlist.pop())
            mixer.music.play()


    def stop_music(self):
        """
        Stops the music.
        """
        mixer.music.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    cards = Cards()
    td = Discard()
    tr = Rules()
    ui.setupUi(MainWindow, cards = cards)
    ui.display_card_all(cards)
    MainWindow.show()
    cards.p1_bid = ui.bid_input(cards, td)[0]
    ui.update_table_bid(cards)
    link = "https://www.youtube.com/watch?v=HmxpLGjZ5sQ"

    ui.float_link.clicked.connect(lambda:ui.open_link(link))

    ui.card1.clicked.connect(lambda: ui.on_click(index = ui.card1,\
                             cards = cards, cardex = cards.c1, disc_class = td,\
                             rules = tr))
    ui.card2.clicked.connect(lambda: ui.on_click(index = ui.card2,\
                             cards = cards, cardex = cards.c2, disc_class = td,\
                             rules = tr))
    ui.card3.clicked.connect(lambda: ui.on_click(index = ui.card3,\
                             cards = cards, cardex = cards.c3, disc_class = td,\
                             rules = tr))
    ui.card4.clicked.connect(lambda: ui.on_click(index = ui.card4,\
                             cards = cards, cardex = cards.c4, disc_class = td,\
                             rules = tr))
    ui.card5.clicked.connect(lambda: ui.on_click(index = ui.card5,\
                             cards = cards, cardex = cards.c5, disc_class = td,\
                             rules = tr))
    ui.card6.clicked.connect(lambda: ui.on_click(index = ui.card6,\
                             cards = cards, cardex = cards.c6, disc_class = td,\
                             rules = tr))
    ui.card7.clicked.connect(lambda: ui.on_click(index = ui.card7,\
                             cards = cards, cardex = cards.c7, disc_class = td,\
                             rules = tr))
    ui.card8.clicked.connect(lambda: ui.on_click(index = ui.card8,\
                             cards = cards, cardex = cards.c8, disc_class = td,\
                             rules = tr))
    ui.card9.clicked.connect(lambda: ui.on_click(index = ui.card9,\
                             cards = cards, cardex = cards.c9, disc_class = td,\
                             rules = tr))
    ui.card10.clicked.connect(lambda: ui.on_click(index = ui.card10,\
                            cards = cards, cardex = cards.c10, disc_class = td,\
                            rules = tr))
    ui.card11.clicked.connect(lambda: ui.on_click(index = ui.card11,\
                            cards = cards, cardex = cards.c11, disc_class = td,\
                            rules = tr))
    ui.card12.clicked.connect(lambda: ui.on_click(index = ui.card12,\
                            cards = cards, cardex = cards.c12, disc_class = td,\
                            rules = tr))
    ui.card13.clicked.connect(lambda: ui.on_click(index = ui.card13,\
                            cards = cards, cardex = cards.c13, disc_class = td,\
                            rules = tr))

    sys.exit(app.exec_())
