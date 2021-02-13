#############################################
#  How To Update Labels
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
#from kivy.uix.float_layout2 import float_layout2

# Designate our .kv design file
Builder.load_file('float_layout2.kv')

class MyLayout(Widget):
    def press(self):
        #create variables for our wodget
        name = self.ids.name_input.text
        #print(name)

        #update the label
        self.ids.name_label.text = f'Hello {name}!'

        # Clear  input box
        self.ids.name_input.text = ''

class AwersomeApp(App): #my.kv
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwersomeApp().run()