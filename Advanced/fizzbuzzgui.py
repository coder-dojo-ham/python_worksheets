"""
Just in case we have excess time. We can throw in some GUI learning with grids and Entry boxes to show fizzbuzz off.
"""

import tkinter
from fizzbuzz import fizzbuzz


class FizzBuzzGui(tkinter.Tk):
    """
    We need an object to hold all the widgets.

    A widget being the various buttons and text we see in a GUI.
    """
    def __init__(self, *args, **kwargs):
        super(FizzBuzzGui, self).__init__(*args, **kwargs)

        self.text = tkinter.StringVar()  # We need a StringVar which we use to change the displayed value.
        self.text.set('0')  # lets start with 0.

        self.text_label = tkinter.Label(self, textvariable=self.text)  # We use a label to display the StringVar.
        self.text_label.grid(row=0, column=0, columnspan=2)

        self.text_input = tkinter.Entry(self)  # We need an entry widget
        self.text_input.grid(row=1, column=0, columnspan=2)

        self.button = tkinter.Button(self, text='Submit', command=self.calc_fizzbuzz)
        self.button.grid(row=2, column=0, columnspan=2)

        # For a bit of added complexity we can add fizz and buzz inputs to change their values.

        self.fizz_label = tkinter.Label(self, text='fizz')  # label to show which is fizz.
        self.fizz_label.grid(row=3, column=0)

        self.buzz_label = tkinter.Label(self, text='buzz')  # label to show which is buzz
        self.buzz_label.grid(row=3, column=1)

        self.fizz_input = tkinter.Entry(self)  # entry for fizz.
        self.fizz_input.grid(row=4, column=0)

        self.buzz_input = tkinter.Entry(self)  # entry for buzz.
        self.buzz_input.grid(row=4, column=1)

        # set some default values

        self.fizz_input.insert(tkinter.END, '3')
        self.buzz_input.insert(tkinter.END, '5')

    def calc_fizzbuzz(self):
        """
        Calculate the input and change the text accordingly.

        Getting the numbers using the method below for int will error if there is nothing there.

        But we can ignore that for now.
        """
        num = int(self.text_input.get())  # get the number we will calculate

        fizz_var = int(self.fizz_input.get())  # get fizz

        buzz_var = int(self.buzz_input.get())  # get buzz

        result = str(fizzbuzz(num, fizz=fizz_var, buzz=buzz_var))

        # No need to return anything in this function. Simply change the StringVar to what we want
        self.text.set(result)


fizz = FizzBuzzGui()  # build the gui.

tkinter.mainloop()  # run the gui.
