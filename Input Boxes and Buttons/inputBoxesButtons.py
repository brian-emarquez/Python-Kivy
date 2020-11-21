import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#kivy.require('1.11.1')

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)






class MyApp(App):
    def build(self):
        return Label(text='Hola Kibyy', font_size=72)

if __name__ == '__main__':
    MyApp().run()