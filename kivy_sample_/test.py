from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivymd.uix.button import MDButton,MDFabButton
from kivy.uix.screenmanager import ScreenManager, Screen
from screen_manager import Screen_Manager
Window.size = (350, 600)

LabelBase.register(
    name="Tahoma Regular font",
    fn_regular="kivy_sample_/fonts/Tahoma Regular font.ttf",
    fn_bold="kivy_sample_/fonts/Tahoma Regular font.ttf"
)

class Login_screen:
    pass

class Signup_screen:
    pass

sm=ScreenManager()
sm.add_widget(Login_screen(name='Login'))   
sm.add_widget(Signup_screen(name='Signup'))

class Main_app(MDApp):
    btn_color=ListProperty((177/255,35/255,65/255,1))

    def build(self):
        return Builder.load_string(Screen_Manager)
    
if __name__ == "__main__":
    Main_app().run()