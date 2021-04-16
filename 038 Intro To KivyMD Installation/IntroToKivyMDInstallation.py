
#Autor: Brian E
#Fecha: 16 Abril 2021
#Contacto: brian@mail.com
#Descrption: Intro To KivyMD Installation

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
    pass
class AwersomeApp(App): #my.kv
    def build(self):
        return MyLayout()
        
if __name__ == '__main__':
    AwersomeApp().run()
    