# How To Set The Height And Width of Widgets

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True
        self.col_default_width=100

        # Create a second gridlayout
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height = 40,
            col_force_default=True,
            col_default_width=100
        )
        # set number of columns
        self.top_grid.cols = 2


        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        # Add input Box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        # Add input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Favorite Color: "))
        # Add input Box
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        
        # add the new top_grid to our app
        self.add_widget(self.top_grid)
        
        # Create a Submit Button
        self.submit = Button(text="Submit", # Configuracion del boton
            font_size=32,
            size_hint_y = None,
            height = 50,
            size_hint_x = None,
            width=200
            
            )

        #Binf the Button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza =  self.pizza.text
        color =  self.color.text

        #print(f'Hello {name}, you like {pizza} pizza, and your favorite color es {color}')

        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color es {color}'))

        # Clear the input boxes
        self.name.text= ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()