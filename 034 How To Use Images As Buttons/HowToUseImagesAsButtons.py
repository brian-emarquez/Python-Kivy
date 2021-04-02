#############################################
# How To Use Images As Buttons
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

Builder.load_file('how.kv')

class MyLayout(Widget):
    def hello_on(self):
        self.ids.my_label.text = "You Pressed the Button!"
        self.ids.my_image.source = 'images/login_press.png'

    def hello_off(self):
        self.ids.my_image.source = 'images/login.png'




class AwersomeApp(App): #my.kv
    def build(self):
        return MyLayout()
        
if __name__ == '__main__':
    AwersomeApp().run()
    