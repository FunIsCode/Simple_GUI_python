# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# BMI

from tkinter import *


class Userinterface:
    def __init__(self):
        self.__mainwindow = Tk()
        # TODO: Change the title of the main window to be "BMI calculator"
        self.__mainwindow.title("BMI calculator")

        # TODO: Add GUI components to make the GUI understandable for the
        # user, for example labels to indicate what the user should write
        # in the Entry-components.
        label_weight = Label(self.__mainwindow, text='Weight Value')
        label_height = Label(self.__mainwindow, text='Height Value')

        # TODO: Create an Entry-component for the weight.
        self.weight = StringVar()
        self.__weight_value = Entry(self.__mainwindow, textvariable=self.weight)
        # TODO: Create an Entry-component for the height.
        self.height = StringVar()
        self.__height_value = Entry(self.__mainwindow, textvariable=self.height)
        # self.height.set(0)
        # self.weight.set(0)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        # the default colour.
        self.__calculate_button = Button(self.__mainwindow, text='calculate_BMI', fg='red', command=self.calculate_BMI)
        # TODO: Create a Label that will show the decimal value of the BMI 
        # after it has been calculated.
        self.result_text = StringVar()
        self.__result_text = Label(self.__mainwindow, textvariable=self.result_text)
        # self.result.set("Decimal Value:")
        # TODO: Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.explanation_text = StringVar()
        self.__explanation_text = Label(self.__mainwindow, textvariable=self.explanation_text)
        # self.text.set("Description...")
        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text='Stop', fg='red', command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        label_weight.grid(row=0, sticky=E)
        label_height.grid(row=1, sticky=E)
        self.__weight_value.grid(row=0, column=1)
        self.__height_value.grid(row=1, column=1)
        self.__calculate_button.grid(row=2, column=1)
        self.__stop_button.grid(row=5, column=1)
        self.__result_text.grid(row=4, column=1)
        self.__explanation_text.grid(row=3, column=1)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text. 
            
            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text.

        """
        try:
            weight_value = float(self.weight.get().strip())
            height_value = float(self.height.get().strip()) / 100
        except ValueError:
            self.explanation_text.set("Error: height and weight must be numbers.")
            self.reset_fields()

        else:
            positive_values = weight_value > 0 and height_value > 0
            if not positive_values:
                self.explanation_text.set("Error: height and weight must be positive.")
                self.reset_fields()
                return
            weight_index = weight_value / (height_value ** 2)
            overweight_index = weight_index > 25
            underweight_index = weight_index < 18.5
            if overweight_index:
                self.explanation_text.set("You are overweight.")
            elif underweight_index:
                self.explanation_text.set("You are underweight.")
            else:
                self.explanation_text.set("Your weight is normal.")
            self.result_text.set('{:.2f}'.format(weight_index))

    def reset_fields(self, msg=''):
        """ In error situations this method will zeroize the elements
            self.__result_text, self.__height_value, and self.__weight_value.
        """
        # delete method(0, end)
        # text_result configure
        #
        # self.height.set('')
        # self.weight.set('')
        # self.result_text.set('')
        self.__weight_value.delete(0, END)
        self.__height_value.delete(0, END)
        self.__result_text.configure(text='')

        self.__explanation_text.configure(text=msg)

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
