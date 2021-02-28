#############################################
# Standalone Python EXE Executable
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

        # test for error firts
        if "Error" in prior:
            prior = ''
        
        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''  
            self.ids.calc_input.text = f'{button}'  
        else:
            self.ids.calc_input.text = f'{prior}{button}' 

    # Create Functions to remove last character in text
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    # Create fenction to make text
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # test
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Create decimal funtion
    def dot(self):
        prior = self.ids.calc_input.text
        #split out text box +
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1] :
            # add a decimal to the end of the  text
            prior = f'{prior}.'
            # Output back to the text box
            self.ids.calc_input.text = prior

        elif "." in prior:
            pass
        else:
            # add a decimal to the end of the  text
            prior = f'{prior}.'
            # Output back to the text box
            self.ids.calc_input.text = prior


    # create addition function
    def math_sign(self, sign):
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'
    
    
    def equals(self):
        prior = self.ids.calc_input.text

        # Error Handling
        try:
            # Evaluate the math from the text box
            answer = eval(prior)

            # Output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"


        '''
        # addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0

            for number in num_list:
                answer =  answer + float(number)

            #print(answer)    
            self.ids.calc_input.text = str(answer)
        '''

class CalculatorApp(App): #my.kv
    def build(self):
        return MyLayout()
        

if __name__ == '__main__':
    CalculatorApp().run()
    