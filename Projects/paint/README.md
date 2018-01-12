# MS Paint clone

In this project we're going to make a basic clone of Microsoft Paint.

This will teach us about GUIs and further our understanding of 
Object Oriented Programming. 

## Getting started
### What you need to know already

To do this project you need to understand:

- Variables.
- If statements.
- Functions.
- Objects.

I'd recommend doing the `would_you_rather_button` and `turtle_racing`
 projects first.

### What we are introducing in this project

This project focuses on teaching you about:

- GUI programming.

## The Project

### Step 1 - The Application

Create a file called `paint.py`.

Inside write the following:

```python
import tkinter


class Paint(tkinter.Tk):
    pass
    

lets_paint = Paint()

tkinter.mainloop()
```

#### What have we done?

So far all we have done is create a class of objects which will contain 
our logic for the paint program.

We create an instance of this class and then start what you call the `mainloop`.

In GUIs (and games) most actions operate on what you call the `mainloop`. This
is essentially a clock which ticks a certain number of times a second (e.g. 60).

Every time the clock ticks, the program redraws the GUI. This allows it to 
animate things like button clicks, or allows it to change the window to look
like something else. In gaming you will know this as the `frame rate`.

### Step 2 - Adding the Canvas

Rewrite the `Paint` class to mirror the following:

```python
class Paint(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(Paint, self).__init__(*args, **kwargs)
        self.canvas = tkinter.Canvas(self, background='white')
        self.canvas.pack(side=tkinter.LEFT, expand=1, fill='both')
```

#### What have we done?

We've added our first widget, the Canvas. This is the drawing area for our 
program. If you run the application now you should see a blank white page.

We've done three things here:

1) We added a `super` call to the `__init__` method. This means we gain all the
functionality inside the `tkinter.Tk` object.

2) We created a widget called `self.canvas`, we attached it to our `tkinter.Tk` 
class (this is why we pass `self` as an argument) and made it have a white background.

3) We `packed` the canvas on to the screen. This tells the GUI where the Canvas 
should go. In this case we said it should go on the left, it should fill as much 
space as possible (`expand=1`). And it should fill the space both horizontally and
vertically (`fill='both'`).

Whilst step 2 is what creates the canvas, step 3 is what actually makes it visible 
to us.

### Step 3 - Adding buttons - Version 1 (Easy)

Now we want to add more widgets to our Paint window. Edit your Paint class to look like
this:

```python
class Paint(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(Paint, self).__init__(*args, **kwargs)
        self.canvas = tkinter.Canvas(self, background='white')
        self.canvas.pack(side=tkinter.LEFT, expand=1, fill='both')

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
        self.colour = 'black'

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
```

#### What have we done?

There is a lot of code here but it is all doing roughly the same thing.

After the canvas we add in a blue `button`. This takes 3 arguments. 
1) `self` for the same reasons as `canvas`.

2) `command` which must be a function, telling the button what to do when we click it. 
In this case we give it a method we made called `change_to_blue` which assigns our active 
colour to `blue`.

3) `bg` which defines the colour background of the button, in this case `blue`.

After creating the button we pack it much like we do with canvas. by telling it to fill
as much space as possible. However we do not tell it to pack on a specific side.

This means that the buttons will align themselves vertically. If you want to know what
it will look like if you tell them to `side=tkinter.RIGHT`, put it in and try it out.

We then repeat the above code for all the colour buttons we want to have.

Lastly we make the methods the buttons use as their `command` which are required to
 change the colour.

### Step 3 - Adding buttons - version 2 (Hard)

This step is optional - you don't have to do it if you don't want to. But it will
reduce your code significantly.

Change the code you wrote above to the following (Note, only the methods and the 
button commands have changed):

```python
class Paint(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(Paint, self).__init__(*args, **kwargs)
        self.canvas = tkinter.Canvas(self, background='white')
        self.canvas.pack(side=tkinter.LEFT, expand=1, fill='both')

        self.blue_button = tkinter.Button(self, command=self.change_colour_factory('blue'), bg='blue')
        self.blue_button.pack(fill='both', expand=1)

        self.red_button = tkinter.Button(self, command=self.change_colour_factory('red'), bg='red')
        self.red_button.pack(fill='both', expand=1)

        self.green_button = tkinter.Button(self, command=self.change_colour_factory('green'), bg='green')
        self.green_button.pack(fill='both', expand=1)

        self.yellow_button = tkinter.Button(self, command=self.change_colour_factory('yellow'), bg='yellow')
        self.yellow_button.pack(fill='both', expand=1)

        self.black_button = tkinter.Button(self, command=self.change_colour_factory('black'), bg='black')
        self.black_button.pack(fill='both', expand=1)
        self.colour = 'black'
        
    def change_colour_factory(self, colour):
        def change_colour():
            self.colour = colour
        return change_colour
```

#### What have we done?

As a button command requires a function we can use something special called a `factory`.

This is function (or object) which creates other functions (or objects). in this case
we create the method `change_colour_factory`. This method takes one argument, `colour`.
It then creates a new function called `change_colour` which changes the colour to the one
given in the `colour` argument. This function is then returned and, in our use case, is
given to the `command` option as the function we want.

The concept of factories is a very advanced one and may be quite difficult to grasp. If 
you are not sure you understand it, feel free to use `version 1` which is more obvious.

### Step 4 - Drawing on the canvas

At this point if we load the program, we have a canvas and we have buttons. But
we still can't actually do anything. Let's change that - this will be the most complicated
part of the lesson.

Add the below to your `Paint` class - make sure you don't remove any of the code you
currently have - I've left comments (`#...`) where the previous code should stay. 
 
```python
class Paint(tkinter.Tk):
    def __init__(self, *args, **kwargs):

        #... Keep the previous code in the __init__ method you've written above here.
        
        self.x = 0
        self.y = 0
        self.button = False
        
        self.canvas.bind('<Motion>', self.mouse_move)
        self.canvas.bind('<ButtonPress-1>', self.button_down)
        self.canvas.bind('<ButtonRelease-1>', self.button_up)

    #... Keep the change_colour_factory method here. 

    def button_down(self, event):
        self.button = True

    def button_up(self, event):
        self.button = False

    def mouse_move(self, event):
        if self.button:
            event.widget.create_line(self.x,
                                     self.y,
                                     event.x,
                                     event.y,
                                     smooth=True,
                                     fill=self.colour,
                                     width=5)
        self.x = event.x
        self.y = event.y
```

#### What have we done?

In the `__init__` method we've added a few new variables, `self.x`, `self.y`,
 `self.button`. `x` and `y` will keep track of where the mouse is. `button` 
 will tell us if the mouse button is being clicked.
 
 We also call `self.canvas.bind` three times. `bind` is a special way of linking an
 action, e.g. moving the mouse, to a function. In this case we link 3 actions.
 
 1) We link `<Motion>`, which is moving the mouse, to `self.mouse_move`.
 
 2) We link `<ButtonPress-1>`, which is clicking the left mouse button, to 
 `self.button_down`.
 
 3) We link `<ButtonRelease-1>`, which is letting go of the left mouse button,
 to `self.button_up`.
 
 We then create the three methods.
 
 1) `button_down` sets the `self.button` variable mentioned above to `True`.
 This tells our program the mouse button is being clicked.
 
 2) `button_up` sets the `self.button` variable mentioned above to `False`.
 This tells our program the mouse button is not being clicked.
 
 3) `mouse_move` is more complicated. It checks to see if `self.button` is 
 `True` - showing that the button is being clicked. If this is `True` then it
 calls `event.widget.create_line`. It gives it the old mouse co-ordinates on 
 the canvas and the new ones (the new co-ordinates are `event.x` and `event.y`).
 It also tells `create_line` to use `self.colour` and `width=5`. This means that
 the canvas will now draw a line of our selected colour between the old and new 
 mouse position - painting on the screen.
 
Finally we set our `self.x` and `self.y` to the new co-ordinates.

Now if you run the program it will draw on screen.

### Step 5 - Clearing the canvas

So now we can draw on the screen. But what if we make a mistake? The easiest 
thing is to start over again - we need to be able to clear the canvas.

Keeping all the previous code add in the following - again I've used comments
to mark where the old code should be:

```python
class Paint(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        #... Keep the previous code in the __init__ method you've written above here.
        self.clear_canvas = tkinter.Button(self, command=self.clear_canvas, text='Clear Canvas')
        self.clear_canvas.pack(fill='both', expand=1)
   
    #... Keep the other methods here.

    def clear_canvas(self):
        self.canvas.delete('all')      

```

#### What have we done.

Compared to the other steps this one is pretty simple.

We've added a new button, but this time we haven't set `bg`. Instead we gave it 
some text to display - "clear canvas".

We also set the command to a new method - `clear_canvas`. all this method does is
tell the canvas to delete everything via `self.canvas.delete('all')`.

If you run the code now you should be able to clear the whole canvas by clicking that button.

#### Extra challenge.

Want to delete only a small part of the drawing?

Try come up with a way of rubbing out the lines without deleting the whole canvas.

### Step 6 - Changing the size of the paint brush

Now we can draw, and we can delete our drawing. But what about our paintbrush size?

There is one last widget we can learn about which can do this.

Keeping all the previous code add in the following - again I've used comments
to mark where the old code should be:

```python
class Paint(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        #... Keep the previous code in the __init__ method you've written above here.
        self.size_scale = tkinter.Scale(self, from_=0, to=20)
        self.size_scale.pack(fill='both', expand=1)
```

Now edit the `event.widget.create_line` function call in `mouse_move` to look like this:

```python
event.widget.create_line(self.x,
                         self.y,
                         event.x,
                         event.y,
                         smooth=True,
                         fill=self.colour,
                         width=self.size_scale.get())
```

Note the only thing we changed was the last line - `width` so that it
 uses `self.size_scale.get()` instead of `5`.
 
#### What have we done.

We've added a sliding widget which decides - between 0 and 20 - how thick
our paint brush should be. We then use this slider to tell `create_line`
what the `width` should be.

That's it!