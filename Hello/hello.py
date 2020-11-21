import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.11.1')


class MainApp(App):
    def build(self):
        return Label(text='Hola Kibyy', font_size=72)

if __name__ == '__main__':
    MainApp().run()