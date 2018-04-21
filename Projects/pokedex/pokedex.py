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
