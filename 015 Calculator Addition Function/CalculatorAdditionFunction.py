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

# Create a button pressing function
    def button_press(self, button):
        prior = self.ids.calc_input.text
        
        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''  
            self.ids.calc_input.text = f'{button}'  
        else:
            self.ids.calc_input.text = f'{prior}{button}' 

# create addition function
    def subtract(self):
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}-'

    def add(self):
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}+'

    def multiply(self):
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}x'

    def divide(self):
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}/'

    def equals(self):
        prior = self.ids.calc_input.text

        # addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0

            for number in num_list:
                answer =  answer + int(number)

            #print(answer)    
            self.ids.calc_input.text = str(answer)
class CalculatorApp(App): #my.kv
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()