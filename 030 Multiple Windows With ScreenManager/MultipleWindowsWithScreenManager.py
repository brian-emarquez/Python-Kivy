#############################################
# Multiple Windows With ScreenManager
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
from kivy.core.spelling import Spelling
from kivy.uix.screenmanager import ScreenManager, Screen

# define our differenrt screens
class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# Designate our .kv design file
kv = Builder.load_file('new_window.kv')

class AwersomeApp(App): #my.kv
    def build(self):
        return kv
        
if __name__ == '__main__':
    AwersomeApp().run()
    