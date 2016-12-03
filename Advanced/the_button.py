"""
This is the button.

It is a super minimal tkinter project designed to teach GUi interactivity.
"""

import tkinter  # tkinter is the standard Python GUI library - it gives us loads of tools to build GUI's with.


class TheButton(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(TheButton, self).__init__(*args, **kwargs)

        # To make things more interesting we will add a text entry widget.
        # This will allow us to do more with the button.
        self.text_input = tkinter.Entry(self)
        self.text_input.pack()

        # This is the button itself which we pack onto the GUI.
        self.the_button = tkinter.Button(self, text='Push the Button', command=self.button_press)
        self.the_button.pack()

        # And finally a stringvar and label in case we want to display anything.
        self.text = tkinter.StringVar()
        self.text.set('')

        self.text_label = tkinter.Label(self, textvariable=self.text)  # We use a label to display the StringVar.
        self.text_label.pack()

    def button_press(self):
        """
        Here is where we control what happens when a user pushes the button.
        """
        print('Button pushed!')

push_the_button = TheButton()

tkinter.mainloop()