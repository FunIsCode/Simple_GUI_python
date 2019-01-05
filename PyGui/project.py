# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# Friday Menu in Konetalo


"""
this is a simple UI ofr konetalo friday food menu which provides burger, chicken wings and rice.
in order to simplify the calculation, we assume student has price of 2.60 each and staff pays 4.90 euros each.
after order submission, the corresponding expense will be displayed below

"""
#  QI YUAN ,267957
# LI KAI, REN, 267122

from tkinter import *


class Userinterface:
    """define the initial display of the UI

    """

    def __init__(self):
        # define the title of UI, which is used for Friday menu display in Konetalo
        self.__mainwindow = Tk()
        self.__mainwindow.title("Friday Menu in Konetalo ")

        # define the first option - burger
        label_burger = Label(self.__mainwindow, text='Burger')
        burger_unit = Label(self.__mainwindow, text='Portion')
        label_burger.grid(row=0, sticky=E)
        burger_unit.grid(row=0, column=2)

        # define the second option - chicken wings
        label_chicken_wings = Label(self.__mainwindow, text='Chicken Wings')
        chicken_wings_unit = Label(self.__mainwindow, text='Pieces')
        label_chicken_wings.grid(row=1, sticky=E)
        chicken_wings_unit.grid(row=1, column=2)

        # define the third option - normal food: rice and dishes
        label_normal_food = Label(self.__mainwindow, text='Rice & Dishes')
        normal_food_unit = Label(self.__mainwindow, text='Portion')
        label_normal_food.grid(row=2, sticky=E)
        normal_food_unit.grid(row=2, column=2)

        # define the widget which is to present the quantity of burger
        self.Burger_quantity = StringVar()
        burger_info = Entry(self.__mainwindow, textvariable=self.Burger_quantity)

        # define the widget which is to present the quantity of chicken wings
        self.Chicken_wings_quantity = StringVar()
        chicken_wings_info = Entry(self.__mainwindow, textvariable=self.Chicken_wings_quantity)

        # define the widget which is to present the quantity of rice & dishes
        self.Rice_quantity = StringVar()
        rice_info = Entry(self.__mainwindow, textvariable=self.Rice_quantity)

        # define the button which calculates the money of orders
        self.__calculate_button = Button(self.__mainwindow, text='Payment', fg='red', command=self.payment)

        # define the widget which is to present total expense of orders
        self.result_text = StringVar()
        self.__result_text = Label(self.__mainwindow, textvariable=self.result_text)

        # define the widget which is to present details of orders
        self.explanation_text = StringVar()
        self.__explanation_text = Label(self.__mainwindow, textvariable=self.explanation_text)

        # define the button which ends UI
        self.__stop_button = Button(self.__mainwindow, text='Stop', fg='red', command=self.stop)

        # define the button which resets the values
        self.__reset_button = Button(self.__mainwindow, text='Reset', fg='red', command=self.reset)

        # define the button which shows the identity of customers  students or staff
        self.__CheckVar = IntVar()
        C = Checkbutton(self.__mainwindow, text="Student", variable=self.__CheckVar,
                        onvalue=1, offvalue=0)

        # grip the widgets in right place of UI
        burger_info.grid(row=0, column=1)
        chicken_wings_info.grid(row=1, column=1)
        rice_info.grid(row=2, column=1)
        C.grid(row=3, column=1)
        self.__calculate_button.grid(row=4, column=1)
        self.__reset_button.grid(row=5, column=1)
        self.__explanation_text.grid(row=6, column=1)
        self.__result_text.grid(row=7, column=1)
        self.__stop_button.grid(row=8, column=1)

        # initialize the UI
        self.reset()

    def reset(self):
        """ this function is to reset the value when initializes the UI or customers manually reset the values.

        :return:  None
        """
        self.Burger_quantity.set(0)
        self.Chicken_wings_quantity.set(0)
        self.Rice_quantity.set(0)
        self.explanation_text.set('')
        self.result_text.set('')

    def payment(self):
        """ this method is to calculate the expense of orders. First, it checks if the inputs are valid, then it checks
        if the values of each orders are not negative, otherwise, it would show the error messages.
        It also considers the identify of customers, if customer is student, we assume that the price for each food
        is 2.60 euros, if not, it is 4.90 euros each.

        """
        try:
            burger_value = int(self.Burger_quantity.get().strip())
            wings_value = int(self.Chicken_wings_quantity.get().strip())
            rice_value = int(self.Rice_quantity.get().strip())
        except ValueError:
            self.explanation_text.set("Error: the values must be numbers.... Please input again")
            self.result_text.set('')

        else:
            positive_values = burger_value >= 0 and wings_value >= 0 and rice_value >= 0

            if not positive_values:
                self.explanation_text.set("Error: the values must be positive.... Please input again")
                self.result_text.set('')
                return

            # check if customer has ordered something ot not, if not, print the message
            if not burger_value and not wings_value and not rice_value:
                self.explanation_text.set("Welcome to our restaurant, please order!")
                self.result_text.set('')
                return

            student = self.__CheckVar.get()
            if student:
                total_money = (burger_value + wings_value / 5 + rice_value) * 2.60
            else:
                total_money = (burger_value + wings_value / 5 + rice_value) * 4.90
            text = 'You ordered {} portions of burger, {} pieces of chicken wings, {} portions of rice and dishes!'

            self.explanation_text.set(text.format(burger_value, wings_value, rice_value))
            self.result_text.set(' Total money are {:.2f} euros'.format(total_money))

    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


main()
