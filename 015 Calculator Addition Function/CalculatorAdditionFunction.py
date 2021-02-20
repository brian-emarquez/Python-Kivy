#############################################
# Calculator Addition Function
#############################################

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500, 700)

# Designate our .kv design file
Builder.load_file('cal.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

class CalculatorApp(App): #my.kv
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()