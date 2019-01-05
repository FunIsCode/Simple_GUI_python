# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Task: dicegame, program code template, version 1 (GUI components separately)

import random
from tkinter import *

DICEPICS = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif", "6.gif"]

PLAYER_1 = 1
PLAYER_2 = 2


class Dicegame:
    def __init__(self):
        self.__window = Tk()
        self.__window.title("Dicegame")

        self.__turn = None
        self.__throwcount = None

        self.__dicepics = []
        for kuvatiedosto in DICEPICS:
            kuva = PhotoImage(file=kuvatiedosto)
            self.__dicepics.append(kuva)

        Label(self.__window, text="Player 1 score:") \
            .grid(row=0, column=0, columnspan=2, sticky=E)
        Label(self.__window, text="Player 2 score:") \
            .grid(row=1, column=0, columnspan=2, sticky=E)

        self.__player1pointsLabel = Label(self.__window)
        self.__player1pointsLabel.grid(row=0, column=2, sticky=W)
        self.__player2pointsLabel = Label(self.__window)
        self.__player2pointsLabel.grid(row=1, column=2, sticky=W)

        self.__throwButton = Button(self.__window, text="throw", command=self.throw)

        self.__throwButton.grid(row=0, column=3, sticky=W + E)
        self.__endturnButton = Button(self.__window, text="end turn")
        self.__endturnButton.grid(row=1, column=3, sticky=W + E)

        Button(self.__window, text="new game", command=self.initialize_game) \
            .grid(row=2, column=3, sticky=W + E + N)
        Button(self.__window, text="stop", command=self.__window.destroy) \
            .grid(row=4, column=3, sticky=W + E + S)

        self.__dice1Label = Label(self.__window)
        self.__dice1Label.grid(row=2, column=0)
        self.__dice2Label = Label(self.__window)
        self.__dice2Label.grid(row=2, column=1)
        self.__dice3Label = Label(self.__window)
        self.__dice3Label.grid(row=2, column=2)

        self.__lock1Button = Button(self.__window)
        self.__lock1Button.grid(row=3, column=0)
        self.__lock2Button = Button(self.__window)
        self.__lock2Button.grid(row=3, column=1)
        self.__lock3Button = Button(self.__window)
        self.__lock3Button.grid(row=3, column=2)

        self.__infoLabel = Label(self.__window)
        self.__infoLabel.grid(row=4, column=0, columnspan=3)

        self.initialize_game()

    def initialize_game(self):
        self.__turn = PLAYER_1
        self.__throwcount = 2
        self.times = 0

        self.__dice1Label.configure(image=self.__dicepics[0])
        self.__dice2Label.configure(image=self.__dicepics[0])
        self.__dice3Label.configure(image=self.__dicepics[0])

        self.report_turn_situations()

        self.enable_throw_and_stop_turn()

        self.release_and_disable_lockbuttons()

    def disable_throw_and_stop_turn(self):
        self.__throwButton.configure(state=DISABLED)
        self.__endturnButton.configure(state=DISABLED)

    def enable_throw_and_stop_turn(self):
        self.__throwButton.configure(state=NORMAL)
        self.__endturnButton.configure(state=NORMAL)
        # self.__throwButton.bind("<Button-1>", lambda event: self.throw(event))

    def report_turn_situations(self):
        self.__infoLabel.configure(text=
                                   "Player {:d} turn, {:d} throws left" \
                                   .format(self.__turn, self.__throwcount))

    def release_and_disable_lockbuttons(self):
        self.__lock1Button.configure(text="unlocked")
        self.__lock2Button.configure(text="unlocked")
        self.__lock3Button.configure(text="unlocked")

        self.__lock1Button.configure(background="green")
        self.__lock2Button.configure(background="green")
        self.__lock3Button.configure(background="green")

        self.__lock1Button.configure(state=DISABLED)
        self.__lock2Button.configure(state=DISABLED)
        self.__lock3Button.configure(state=DISABLED)

    def throw(self):
        """ Throw all dices """
        #
        dice_1_number = random.randint(0, 5)
        dice_2_number = random.randint(0, 5)
        dice_3_number = random.randint(0, 5)
        # print(dice_1_number+1, dice_2_number+1, dice_3_number+1)
        self.__dice1Label.configure(image=self.__dicepics[dice_1_number])
        self.__dice2Label.configure(image=self.__dicepics[dice_2_number])
        self.__dice3Label.configure(image=self.__dicepics[dice_3_number])

        self.times += 1
        if self.times % 2 == 1:
            self.__turn = 2
            if self.__throwcount == 0:
                self.disable_throw_and_stop_turn()
        else:
            self.__turn = 1
            self.__throwcount -= 1
        self.report_turn_situations()

    def start(self):
        self.__window.mainloop()


def main():
    ui = Dicegame()
    ui.start()


main()
