# The Pokedex

In this project we're going to make a Pokedex.

We're going to take knowledge we've gained from making GUIs
as well as making and querying APIs and combine them into 
something useful.

## Getting started
### What you need to know already

To do this project you need to understand:

- Objects.
- Making requests.

I'd recommend doing the `paint` and `flask_calculator`
 projects first.

### What we are introducing in this project

This project focuses on teaching you about:

- Combining APIs with GUIs.
- Error handling.

## The Project

### Step 1 - The Application

First lets write up our GUI framework like so:

```python
import tkinter


class Pokedex(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    pokedex = Pokedex()
    tkinter.mainloop()
```

#### What have we done?

We've written a `stub` for our Pokedex program, providing the general 
framework to add code to.

A `stub` is simply a program which represents what we are going to do,
but doesn't actually do anything.

### Step 2 - Making a simple interface

We need a way to request Pokemon information, a text input and a button.

Let's add these to our `__init__` method. We'll use the grid system
for putting widgets on the screen to give us more control:

```python
class Pokedex(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.input_label = tkinter.Label(self, text='Which Pokemon do you want to learn about?')
        self.input_label.grid(row=0, column=0)

        self.input = tkinter.Entry(self)
        self.input.grid(row=0, column=1)

        self.button = tkinter.Button(text='Submit', command=self.query)
        self.button.grid(row=1, column=0, columnspan=2)

    def query(self):
        print(self.input.get())
```

#### What have we done?

We've added three widgets and a method.

The three widgets are a label to tell us what to do, a text entry and a 
button, with the button calling our new method when clicked.

We've used the grid system in this project, this lets us use a `row` and 
`column` system to define where our widgets go. We can also use `columnspan`
to define how wide our widget should be.

Try it out, put something in the input and click the button.

### Step 3 - Getting the information

What we've done so far gives us a nice interface but doesn't do
anything useful, lets change that with an API.

An API, in case you've forgotten, is simply a way for programs to interact 
with each other. A common way is by making `requests` to a URL on the 
internet and getting some information back as a `response`.

Luckily for us someone has made a database of Pokemon and created an API
that we can use for free. It's called the `pokeapi`, you can find out
more about it [here](https://pokeapi.co/).

For us to use this we need to do a couple things:

1) Import `requests` at the top of the file, so we can make requests to 
the `pokeapi`.

2) Add the `pokeapi` url to our Pokedex.

3) Store the data we get from the request.

Change your Pokedex file to look like this:

```python
import tkinter

import requests


class Pokedex(tkinter.Tk):

    pokeapi_url = 'https://pokeapi.co/api/v2/pokemon/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.input_label = tkinter.Label(self, text='Which Pokemon do you want to learn about?')
        self.input_label.grid(row=0, column=0)

        self.input = tkinter.Entry(self)
        self.input.grid(row=0, column=1)

        self.button = tkinter.Button(text='Submit', command=self.query)
        self.button.grid(row=1, column=0, columnspan=2)

        self.data = {}

    def query(self):
        response = requests.get(
            self.pokeapi_url + self.input.get()
        )
        self.data = response.json()

# keep the main statement below here
```

#### What have we done?

We've added the `pokeapi` url to the top of the class so we can use it 
easily.

We've also added a data dictionary in the `__init__` method.

Finally we've updated our `query` method to make a request to the API
and save the response in our data dictionary.

If you want you could print the dictionary to see what we get.

### Step 4 - Displaying the data

This is the biggest step of the lesson.

It's great that we have data, but we need to show it off.

Let's create a `Frame` widget which can hold more widgets inside itself.

Update the `__init__` method to look like this:

```python
# ...
class Pokedex(tinter.Tk):
    # ...
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.input_label = tkinter.Label(self, text='Which Pokemon do you want to learn about?')
        self.input_label.grid(row=0, column=0)

        self.input = tkinter.Entry(self)
        self.input.grid(row=0, column=1)

        self.button = tkinter.Button(text='Submit', command=self.query)
        self.button.grid(row=1, column=0, columnspan=2)

        self.data = {}

        self.display = tkinter.Frame(
            self,
            bd=2,
            relief=tkinter.SUNKEN
        )
        self.display.grid(row=0, column=2, rowspan=10, columnspan=5)
# ...
```

The main addition here is the `display` variable we add in the last
two statements.

Next add a method to display the data:

```python
# ...
class Pokedex(tinter.Tk):
    # ...
    def display_data(self):
        self.display.destroy()
        self.display = tkinter.Frame(
            self,
            bd=2,
            relief=tkinter.SUNKEN
        )
        self.display.grid(row=0, column=2, rowspan=10, columnspan=5)

        name_label = tkinter.Label(self.display, text='Name: ')
        name_label.grid(row=0, column=0)
        name = tkinter.Label(self.display, text=self.data['name'])
        name.grid(row=0, column=1)

        id_label = tkinter.Label(self.display, text='ID: ')
        id_label.grid(row=1, column=0)
        id = tkinter.Label(self.display, text=self.data['id'])
        id.grid(row=1, column=1)

        weight_label = tkinter.Label(self.display, text='Weight: ')
        weight_label.grid(row=2, column=0)
        weight = tkinter.Label(self.display, text=self.data['weight'])
        weight.grid(row=2, column=1)

        height_label = tkinter.Label(self.display, text='Height: ')
        height_label.grid(row=3, column=0)
        height = tkinter.Label(self.display, text=self.data['height'])
        height.grid(row=3, column=1)
# ...
```
This may look daunting, but most of it is copy and pasting and then
changing some names to add data to the frame.

Finally call this method at the end of the `query` method:

```python
# ...
class Pokedex(tinter.Tk):
    # ...
    def query(self):
        response = requests.get(
            self.pokeapi_url + self.input.get()
        )
        self.data = response.json()

        self.display_data()
# ...
```

#### What have we done?

We created a `Frame` object to put inside our GUI, this acts like a GUI 
within a GUI so we can add objects directly to it instead of adding them
to the main window (`self`).

We the created a method, `display_data`, which destroys this frame, to clear it, and then
recreates it and adds the new data to it.

Finally we updated our `query` method to call `display_data`.

### Step 5 - Handling Exceptions

Try out the program, you should be able to put in a pokemon name or number
and get something showing.

But what happens if you ask for something that isn't a pokemon? Try it out.

To fix this we need to learn about handling exceptions.

An exception is something a program raises when something goes wrong. Normally
this would result in a program crashes but luckily `tkinter` stops that 
happening creating an odd bug for us to solve.

To stop an exception from ruining your program you have to "handle" or `catch`
it. In python you do this with `try/catch` statements.

We'll do this with our `query` method and a new `handle_exception` method:

```python
# ...
class Pokedex(tinter.Tk):
    # ...
    def query(self):
        response = requests.get(
            self.pokeapi_url + self.input.get()
        )
        self.data = response.json()

        try:
            self.display_data()
        except KeyError:
            self.handle_error()

    def handle_error(self):
        self.display.destroy()
        self.display = tkinter.Frame(
            self,
            bd=2,
            relief=tkinter.SUNKEN
        )
        self.display.grid(row=0, column=2, rowspan=2)

        error = tkinter.Label(self.display, text='ERROR! That was not a Pokemon!', fg='red')
        error.grid(row=0, column=0)
    
```

#### What have we done?

We added error handling by catching the `KeyError` thrown when we tried to 
get an invalid Pokemon. If a different exception was thrown, e.g. 
`ValueError` we could simply replace `KeyError` with that to catch it.

Once caught we display our own custom error to tell the user what has 
happened.

Exception handling is an important aspect of programming when trying to
predict everything that could (and should) go wrong in a program.


### The final product

The final code should look something like this:

```python
import tkinter

import requests


class Pokedex(tkinter.Tk):

    pokeapi_url = 'https://pokeapi.co/api/v2/pokemon/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title

        self.input_label = tkinter.Label(self, text='Which Pokemon do you want to learn about?')
        self.input_label.grid(row=0, column=0)

        self.input = tkinter.Entry(self)
        self.input.grid(row=0, column=1)

        self.button = tkinter.Button(text='Submit', command=self.query)
        self.button.grid(row=1, column=0, columnspan=2)

        self.data = {}

        self.display = tkinter.Frame(
            self,
            bd=2,
            relief=tkinter.SUNKEN
        )
        self.display.grid(row=0, column=2, rowspan=2)

    def query(self):
        response = requests.get(
            self.pokeapi_url + self.input.get()
        )
        self.data = response.json()

        try:
            self.display_data()
        except KeyError:
            self.handle_error()

    def handle_error(self):
        self.display.destroy()
        self.display = tkinter.Frame(
            self,
            bd=2,
            relief=tkinter.SUNKEN
        )
        self.display.grid(row=0, column=2, rowspan=2)

        error = tkinter.Label(self.display, text='ERROR! That was not a Pokemon!', fg='red')
        error.grid(row=0, column=0)

    def display_data(self):
        self.display.destroy()
        self.display = tkinter.Frame(
            self,
            bd=2,
            relief=tkinter.SUNKEN
        )
        self.display.grid(row=0, column=2, rowspan=2)

        name_label = tkinter.Label(self.display, text='Name: ')
        name_label.grid(row=0, column=0)
        name = tkinter.Label(self.display, text=self.data['name'])
        name.grid(row=0, column=1)

        id_label = tkinter.Label(self.display, text='ID: ')
        id_label.grid(row=1, column=0)
        id = tkinter.Label(self.display, text=self.data['id'])
        id.grid(row=1, column=1)

        weight_label = tkinter.Label(self.display, text='Weight: ')
        weight_label.grid(row=2, column=0)
        weight = tkinter.Label(self.display, text=self.data['weight'])
        weight.grid(row=2, column=1)

        height_label = tkinter.Label(self.display, text='Height: ')
        height_label.grid(row=3, column=0)
        height = tkinter.Label(self.display, text=self.data['height'])
        height.grid(row=3, column=1)


if __name__ == '__main__':
    pokedex = Pokedex()
    tkinter.mainloop()
```

### What next?

That's it for the basics of making a Pokedex. But it can always be 
improved.

Some ideas that you can try to implement yourself:

1) Create a `cache` - a place to store data you've already queried 
so you don't need to query the API again (as API calls can be slow).

2) Display more data - the rest of the fields are held inside 
`dicts` and `lists` so you'll have to figure out how to display these
dynamically.

3) Query more endpoints - the `pokeapi` allows you to get a lot more
than just Pokemon, take a look [here](https://pokeapi.co/docsv2).

4) Make the GUI resizeable - right now it's very static, we should
let the widgets expand with the GUI.

5) Add styling! Right now the interface is dull, we should make it
look more interesting.

If you have any other ideas feel free to try them out!