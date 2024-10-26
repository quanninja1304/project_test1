from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivymd.uix.button import MDButton,MDFabButton
from kivy.uix.screenmanager import ScreenManager, Screen
from screen_manager import Screen_Manager

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

    def on_login_press(self):
        # Implement your login logic here
        print("Login button pressed")

    def switch_theme_style(self):
        # Implement your theme switch logic here
        print("Theme style switched")

if __name__ == "__main__":
    MainApp().run()