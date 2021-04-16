
#Autor: Brian E
#Fecha: 16 Abril 2021
#Contacto: brian@mail.com
#Descrption: How To Teach Yourself KivyMD Quickly

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp

Builder.load_file('how.kv')

class MyLayout(Widget):
    pass

class AwersomeApp(MDApp): #my.kv
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwersomeApp().run()
    