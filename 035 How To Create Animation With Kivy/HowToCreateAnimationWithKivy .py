#############################################
# How To Create Animation With Kivy 
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
from kivy.animation import Animation

Builder.load_file('how.kv')

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        # Define the animation you wat yo do
        animate = Animation(
            background_color = (0,0,1,1),
            duration=1)
            #opacity=0)
        
        animate +=Animation(
            size_hint=(1,1))

        animate += Animation(
            size_hint=(.5,.5))

        animate += Animation(
            pos_hint = {"center_x": 0.1})

        animate += Animation(
            pos_hint = {"center_x": 0.5})

        animate += Animation(
            pos_hint = {"center_x": 1})

        animate += Animation(
            pos_hint = {"center_x": 0.5})

        # start the animation
        animate.start(widget)

        # crete a callback
        animate.bind(on_complete = self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = "Wow look ar that"


class AwersomeApp(App): #my.kv
    def build(self):
        return MyLayout()
        
if __name__ == '__main__':
    AwersomeApp().run()
    