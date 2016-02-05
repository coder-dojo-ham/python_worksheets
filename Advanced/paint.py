# This is a GUI program which emulates a basic paint program.
# GUI stands for Graphical User Interface.
# Any program you use which you can see and use with your mouse and/or keyboard is a GUI.

# This program will use a basic GUI class and functions to build a paint program.
# In it you should be able to pick a colour from a palette and draw on a canvas.

import tkinter  # tkinter is the standard Python GUI library - it gives us loads of tools to build GUI's with.


class Paint(tkinter.Tk):
    """
    It is best practice to build GUI's using classes, or objects as they are also known.

    It is best to think of each thing in a GUI as an object with it's own set of properties.

    We are making a Paint class which "inherits" tkinters Tk object. The Tk object is a basic GUI window.
    """
    def __init__(self, *args, **kwargs):
        """
        The __init__ function is the first function called when a class is created.

        This makes it really useful to set things up in it. Here we use it to put in a canvas for drawing, some buttons
        to control how we paint, and some basic settings like the paint colour and if we are clicking the mouse button
        or not.
        """
        # super is a special function we should call when inheriting a class to make sure everything works right.
        super(Paint, self).__init__(*args, **kwargs)

        # as a GUI is like a graph, we should store the position of the mouse using x and y co-ordinates.
        # Lets set them to 0 here as we don't know where the mouse is yet - these will change later
        self.x = 0
        self.y = 0

        # Here we are setting the colour property to black. It will be used to tell us what colour we are drawing with.
        # We can change this later.
        self.colour = 'black'

        # Here we are making a button property. We will use this to tell us if the mouse button is being clicked or not.
        # For now False means it is not being clicked, and True means it is.
        # It doesn't have to be True or False, it could be anything you want.
        self.button = False

        # Here we are making a canvas using tkinters Canvas object.
        # GUI objects are often called widgets so we will use the term widget from now on.
        #  We set the background colour to white.
        self.canvas = tkinter.Canvas(self, background='white')

        # After we make the canvas we have to "pack" it.
        # Packing puts widgets onto the Tk window so we can see and use them.
        # Here we make sure the canvas goes on the left and fills all the space without other widgets in it.
        self.canvas.pack(side=tkinter.LEFT, fill='both', expand=1)

        # Now the canvas is packed in we can build extra widgets.
        # Lets put some buttons in. These ones can use a "command" which is a function it will call when clicked.
        # Some easy buttons could be to change the colour we are drawing with like below.

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

        # How about the thickness of the pen? We could use a slider to choose how thick the pen is when drawing.
        # This stores the value the slider is on, so we don't need to add a command here.
        self.size_scale = tkinter.Scale(self, from_=0, to=20)
        self.size_scale.pack(fill='both', expand=1)

        # And what about when we want to start over? We need to clear the canvas. Lets add a button for that.
        # This time we can add some text to say what it does.
        self.clear_canvas = tkinter.Button(self, command=self.clear_canvas, text='Clear Canvas')
        self.clear_canvas.pack(fill='both', expand=1)

        # Lastly we need to "bind" some functions to our mouse when it is on the canvas.
        # We do this with the bind method for the canvas.
        # Each bind below takes a type of action, like moving the mouse or pressing and releasing a button, and makes
        # sure a function is called when that action occurs.
        self.canvas.bind('<Motion>', self.mouse_move)
        self.canvas.bind('<ButtonPress-1>', self.button_down)
        self.canvas.bind('<ButtonRelease-1>', self.button_up)

        # OK now we've made all the widgets and bound them to functions - we need to define the functions they use.
        # Important - when you define a function within a class, they are actually called methods!
        # Also every method will take an argument called "self". Self is a special argument which is always the object
        # itself. This is so you can access the properties we made in the __init__ function.

    def button_down(self, event):
        """
        This is called when a person clicks down on the left mouse button.

        All it does is set the button attribute to True!
        """
        self.button = True

    def button_up(self, event):
        """
        This is called when a person releases the left mouse button.

        All it does is set the button attribute to False!
        """
        self.button = False

    def mouse_move(self, event):
        """
        This is the most important method!

        It is called everytime the mouse moves.

        It makes sure the button is down, and if it is it will draw something.
        If the button isn't down it will just record where the mouse is and not draw anything.

        The event argument is what is happening - in this case the mouse is moving.
        Event has loads of useful properties like widget - which tells you which widget we are in.
        It also has x and y co-ordinates which tell us where the mouse is.
        """
        if self.button:  # Here we check if the button is down. Remember True means it is down, False means it isn't.
            # If the button is down we use the create_line method to draw something.
            event.widget.create_line(self.x,  # This is the old position of the mouse
                                     self.y,
                                     event.x,  # This is the new position of the mouse
                                     event.y,
                                     smooth=True,  # This allows us to draw smooth shapes, otherwise it would all be straight lines
                                     fill=self.colour,  # Here we take the colour property to know what colour we are using.
                                     width=self.size_scale.get())  # And here we take the slider value for the line size.

        # Finally we have to record where the new mouse position is.
        self.x = event.x
        self.y = event.y

    def change_to_blue(self):
        """
        This is called when you click the blue button.

        All it does is set the colour we draw with to blue!
        """
        self.colour = 'blue'

    def change_to_red(self):
        """
        This is called when you click the red button.

        All it does is set the colour we draw with to red!
        """
        self.colour = 'red'

    def change_to_green(self):
        """
        This is called when you click the green button.

        All it does is set the colour we draw with to green!
        """
        self.colour = 'green'

    def change_to_yellow(self):
        """
        This is called when you click the yellow button.

        All it does is set the colour we draw with to yellow!
        """
        self.colour = 'yellow'

    def change_to_black(self):
        """
        This is called when you click the black button.

        All it does is set the colour we draw with to black!
        """
        self.colour = 'black'

    def clear_canvas(self):
        """
        This is caled when you click the clear canvas button.

        It deletes everything from the canvas so we can start over again!
        """
        self.canvas.delete('all')

lets_paint = Paint()

tkinter.mainloop()