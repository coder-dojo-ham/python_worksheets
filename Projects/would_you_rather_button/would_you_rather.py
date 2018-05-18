"""
This is the would you rather generator.

It is a super minimal tkinter project designed to teach GUi interactivity.
"""

import random
import tkinter  # tkinter is the standard Python GUI library - it gives us loads of tools to build GUI's with.


class WouldYouRather(tkinter.Tk):

    ACTIVITIES = ['run', 'dance', 'jump', 'code', 'swim', 'climb', 'think']
    THINGS = ['spoon', 'tiger', 'chimney', 'table', 'chewing gum', 'floor', 'monkey']
    WITH_USING_EATING = ['with', 'using', 'while eating']

    def __init__(self, *args, **kwargs):
        super(WouldYouRather, self).__init__(*args, **kwargs)

        # This is the button itself which we pack onto the GUI.
        self.the_button = tkinter.Button(self, text='Push the Button', command=self.button_press)
        self.the_button.pack()

        # And finally a stringvar and label in case we want to display anything.
        self.text = tkinter.StringVar()
        
        self.text.set('')

        self.text_label = tkinter.Label(self, textvariable=self.text)  # We use a label to display the StringVar.
        self.text_label.pack()

    def generate_option(self):
        """
        Generate an option for people to choose from.
        """
        return '{} {} a {}'.format(
            random.choice(self.ACTIVITIES),
            random.choice(self.WITH_USING_EATING),
            random.choice(self.THINGS)
        )

    def button_press(self):
        """
        Here is where we control what happens when a user pushes the button.
        """
        self.text.set(
            'Would you rather {} or {}'.format(
                self.generate_option(), self.generate_option()
            )
        )


would_you_rather = WouldYouRather()
tkinter.mainloop()
