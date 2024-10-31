from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivymd.uix.button import MDButton,MDFabButton,MDButtonText
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen, MDScreen
from screen_manager import Screen_Manager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)
from kivy.properties import StringProperty, ColorProperty
# Window.size = (350, 600)

# Registering the custom font
LabelBase.register(
    name="Tahoma Regular font",
    fn_regular="kivy_sample_/fonts/Tahoma Regular font.ttf",
    fn_bold="kivy_sample_/fonts/Tahoma Regular font.ttf"
)

# Define the Login and Signup screens
class LoginScreen(Screen):
    def on_enter(self):
        Window.size = (350, 600)

class SignUpScreen(Screen):
    pass

class MainScreen(Screen):
    def on_enter(self):
        Window.size = (900, 600)

class HomeScreen(Screen):
    # You can initialize any properties here if needed
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

class CountDownScreen(Screen):
    pass

class ToDoListScreen(Screen):
    pass

class NotesScreen(Screen):
    pass

class  StatisticsScreen(Screen):
    pass

class  GamesScreen(Screen):
    pass

class   AccountScreen(Screen):
    pass

class  SettingsScreen(Screen):
    pass

class DrawerLabel(MDBoxLayout):
    icon = StringProperty()
    text = StringProperty()

class DrawerItem(MDNavigationDrawerItem):
    icon = StringProperty()
    text = StringProperty()
    trailing_text = StringProperty()
    trailing_text_color = ColorProperty()

    _trailing_text_obj = None

    def on_trailing_text(self, instance, value):
        self._trailing_text_obj = MDNavigationDrawerItemTrailingText(
            text=value,
            theme_text_color="Custom",
            text_color=self.trailing_text_color,
        )
        self.add_widget(self._trailing_text_obj)

    def on_trailing_text_color(self, instance, value):
        self._trailing_text_obj.text_color = value

# Creating the ScreenManager instance
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))   
sm.add_widget(SignUpScreen(name='signup'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(HomeScreen(name='homescreen'))
sm.add_widget(CountDownScreen(name='countdownscreen'))
sm.add_widget(ToDoListScreen(name='todolist'))
sm.add_widget(NotesScreen(name='notes'))
sm.add_widget(StatisticsScreen(name='statistics'))
sm.add_widget(GamesScreen(name='games'))
sm.add_widget(AccountScreen(name='account'))
sm.add_widget(SettingsScreen(name='settings'))

# Main application class
class MainApp(MDApp):
    btn_color = ListProperty((177/255, 35/255, 65/255, 1))

    def build(self):
        return Builder.load_string(Screen_Manager)

if __name__ == "__main__":
    MainApp().run()