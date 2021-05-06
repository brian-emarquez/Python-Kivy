
#Autor: Brian E
#Fecha: 06 Mayo 2021
#Contacto: brian@mail.com
#Descrption: Create A Bottom Bar Button with KivyMD

from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp): 
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('how.kv')



MainApp().run()