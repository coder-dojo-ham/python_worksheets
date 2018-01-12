# Would you rather?

In this project we're going to make a small GUI that asks
random "Would you rather?" questions.

This will teach us about GUIs and further our understanding of 
Object Oriented Programming. 

## Getting Started
### What you need to know already

To do this project you need to understand:

- Variables.
- If statements.
- Functions.
- Objects.

### What we are introducing in this project

This project focuses on teaching you about:

- GUI programming.

## The Project

### Step 1 - The Application

Create a file called `would_you_rather.py`.

Inside write the following:

```python
import random
import tkinter


class WouldYouRather(tkinter.Tk):
    pass
    

push_the_button = WouldYouRather()

tkinter.mainloop()
```

#### What have we done?

So far all we have done is create a class of objects which will contain 
our logic for the would you rather program.

We create an instance of this class and then start what you call the `mainloop`.

In GUIs (and games) most actions operate on what you call the `mainloop`. This
is essentially a clock which ticks a certain number of times a second (e.g. 60).

Every time the clock ticks, the program redraws the GUI. This allows it to 
animate things like button clicks, or allows it to change the window to look
like something else. In gaming you will know this as the `frame rate`.

### Step 2 - Adding a button

Rewrite the class to look like this:

```python
class WouldYouRather(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(WouldYouRather, self).__init__(*args, **kwargs)
        self.the_button = tkinter.Button(self, text='Push the Button', command=self.button_press)
        self.the_button.pack()
        
    def button_press(self):
        print('Button Pushed!')
```

#### What have we done?

Now we've added an `__init__` and called the `super` function - giving us all
the power of the `tkinter.Tk` class when building GUIs.

We also created a button (called "the_button") and gave it some text to display
("Push the button"). We also gave it the command `self.button_press`. We followed this up by calling `the_button.pack()` which puts
the button onto our screen.

Finally we define the method `button_press` which simply prints "Button pushed!".

If we ran the program now we'd see a button on our screens which, when pushed,
would print "Button Pushed!" to the console.

### Step 3 - Adding a label

Labels are ways of displaying text in GUIs. We need one here to display our question.

Add the following to the `__init__` method. Don't remove any of the previous code. 
I've put in comments like these `#...` to show you where the previous code should be kept.


```python
class WouldYouRather(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        #... Keep the current __init__ logic here.
        
        self.text = tkinter.StringVar()
        self.text.set('Generate a question')

        self.text_label = tkinter.Label(self, textvariable=self.text)
        self.text_label.pack()
    #... Keep the button_press method here.

``` 

#### What have we done.

We've added two new variables to our GUI.

One is a `StringVar` this is like a special variable which holds only text. We
set it to say "Generate a question".

tkinter GUIs can't display strings directly so we have to use `StringVar`s instead.

The second variable is a `Label` which displays our above `StringVar`.

We pack the `Label` so it appears directly below our button.

If you ran the program now you'd see "Generate a question" displayed below the button
but you still aren't getting any questions! Lets do that next.

### Step 4 - Random question generator

At this point we leave GUI programming behind and start using normal logic.

We need a few lists of random nouns and verbs and a way to join these together
into a question. Feel free to figure out how to do this yourself as long as it is
a method on the class. Otherwise you can follow the below guide.

Keeping everything you've done before add the following to the class. I've put in comments
like `#...` to show where the old code should stay.

```python
class WouldYouRather(tkinter.Tk):
    
    ACTIVITIES = ['run', 'dance', 'jump', 'code', 'swim', 'climb', 'think']
    THINGS = ['spoon', 'tiger', 'chimney', 'table', 'chewing gum', 'floor', 'monkey']
    WITH_USING_EATING = ['with', 'using', 'while eating']

    #... Keep the __init__ and button_press methods as they are for now.

    def generate_option(self):
        return '{} {} a {}'.format(
            random.choice(self.ACTIVITIES),
            random.choice(self.WITH_USING_EATING),
            random.choice(self.THINGS)
        )

```

#### What have we done?

We have added 3 new lists as Class variables. We have a list of verbs, a list of 
nouns and a list of glue phrases like "with" and "using". We can combine elements
of these lists to create a would you rather option.

We then create the method `generate_option`. This uses something called 
`string formatting` which is a way of inserting stuff into a string. It will
replace a `{}` in a string with another variable you give it. In this case we
provide random choices from our lists to replace the `{}` in the string.

As a result we now generate would you rather options but we still don't actually
provide any questions.

### Step 5 - Asking the question

The last step is to generate the full question and display it on the screen.

We do this by rewriting the `button_press` method like as below. Remember to 
keep everything the same.

```python

class WouldYouRather(tkinter.Tk):
    #... Keep all the lists, the __init__ method and the generate_option
    #... method here.
    
    def button_press(self):
        self.text.set(
            'Would you rather {} or {}'.format(
                self.generate_option(), self.generate_option()
            )
        )
```

#### What have we done?

Now when the button is pressed it replaces the text in our `StringVar` with a
generated question.

We create the question by using `.format` again and inputting 2 randomly generated
questions.

Try it out!


### Extra

Try and see if you can make the button do anything else, or if there are different
types of questions you could get it to ask.