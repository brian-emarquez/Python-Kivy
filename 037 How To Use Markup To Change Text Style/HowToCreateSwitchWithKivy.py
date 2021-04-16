
#Autor: Brian E
#Fecha: 16 Abril 2021
#Contacto: brian@mail.com
#Descrption: How To Create a Switch With Kivy

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
    def switch_click(self, switchObject, switchValue):
        #print(switchValue)
        if (switchValue):
            self.ids.my_label.text = "You Clicked the Switch On!"
        else:
            self.ids.my_label.text = "You Clicked the Switch !Off!"
            #self.ids.my_switch.disabled = True

class AwersomeApp(App): #my.kv
    def build(self):
        return MyLayout()
        
if __name__ == '__main__':
    AwersomeApp().run()
    