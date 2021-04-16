
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

class MainApp(MDApp): 
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('how.kv')

#'Red', 'Pink', 'Purple', 'DeepPurple',
#'Indigo', 'Blue', 'LightBlue', 'Cyan',
#'Teal', 'Gren', 'LightGreen', 'Lime'

MainApp().run()