# This is a GUI program which emulates a basic paint program.
# GUI stands for Graphical User Interface.
# Any program you use which you can see and use with your mouse and/or keyboard is a GUI.

# This program will use some basic GUI classes and functions to build a paint program.
# In it you should be able to pick a colour from a palette and draw on a canvas.

import tkinter


class Paint(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        super(Paint, self).__init__(*args, **kwargs)

        self.x = None
        self.y = None

        self.colour = 'black'

        self.button = 0

        self.canvas = tkinter.Canvas(self, background='white')
        self.canvas.pack(side=tkinter.LEFT, fill='both', expand=1)

        self.blue_button = tkinter.Button(self, command=self.change_to_blue, bg='blue')
        self.blue_button.pack(fill='both', expand=1)

        self.red_button = tkinter.Button(self, command=self.change_to_red, bg='red')
        self.red_button.pack(fill='both', expand=1)

        self.green_button = tkinter.Button(self, command=self.change_to_green, bg='green')
        self.green_button.pack(fill='both', expand=1)

        self.yellow_button = tkinter.Button(self, command=self.change_to_yellow, bg='yellow')
        self.yellow_button.pack(fill='both', expand=1)

        self.black_button = tkinter.Button(self, command=self.change_to_black, bg='black')
        self.black_button.pack(fill='both', expand=1)

        self.size_scale = tkinter.Scale(self, from_=0, to=20)
        self.size_scale.pack(fill='both', expand=1)

        self.clear_canvas = tkinter.Button(self, command=self.clear_canvas, text='Clear Canvas')
        self.clear_canvas.pack(fill='both', expand=1)

        self.canvas.bind('<Motion>', self.mouse_move)
        self.canvas.bind('<ButtonPress-1>', self.button_down)
        self.canvas.bind('<ButtonRelease-1>', self.button_up)


    def button_down(self, event):
        self.button = 1

    def button_up(self, event):
        self.button = 0

    def mouse_move(self, event):

        if self.button:
            if self.x is not None and self.y is not None:
                event.widget.create_line(self.x,
                                         self.y,
                                         event.x,
                                         event.y,
                                         smooth=True,
                                         fill=self.colour,
                                         width=self.size_scale.get())
        self.x = event.x
        self.y = event.y

    def change_to_blue(self):
        self.colour = 'blue'

    def change_to_red(self):
        self.colour = 'red'

    def change_to_green(self):
        self.colour = 'green'

    def change_to_yellow(self):
        self.colour = 'yellow'

    def change_to_black(self):
        self.colour = 'black'

    def clear_canvas(self):
        self.canvas.delete('all')

if __name__ == '__main__':
    start = Paint()
