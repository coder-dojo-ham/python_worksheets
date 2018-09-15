import tkinter


class TheButton(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.the_button = tkinter.Button(self, text='Push the Button', command=self.button_press)
        self.the_button.pack()

    def button_press(self):
        print('You pushed the button!')


if __name__ == '__main__':
    the_button = TheButton()
    tkinter.mainloop()
