#############################################
# Spell Checker
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

# Designate our .kv design file
Builder.load_file('spell.kv')

class MyLayout(Widget):
    def press (self):
        # Create instalce of spelling
        s = Spelling()

        # Select the lenguje
        s.select_language('en_US')

        # See the Languaje options
        #print(s.list_languages())

        # Grab the word
        word = self.ids.word_input.text

        options = s.suggest(word)
        x = ''
        for item in options:
            x = f'{x} {item}'
        # update our label
        self.ids.word_label.text = f'{x}'


class AwersomeApp(App): #my.kv
    def build(self):
        return MyLayout()
        

if __name__ == '__main__':
    AwersomeApp().run()
    