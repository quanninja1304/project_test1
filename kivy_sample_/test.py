from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.core.window import Window
from kivy.properties import ListProperty,ObjectProperty
from kivy.uix.button import Button
from kivymd.uix.button import MDButton,MDFabButton,MDButtonText
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen, MDScreen
from kivy.clock import Clock
from kivy.uix.screenmanager import (
    SlideTransition,
    SwapTransition, 
    FadeTransition,
    WipeTransition,
    FallOutTransition,
    RiseInTransition,
    NoTransition
)
#from screen_manager import Screen_Manager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)
from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.transition import transition, MDFadeSlideTransition
# Window.size = (350, 600)

Screen_Manager = """
ScreenManager:
    LoginScreen:
    SignUpScreen:
    MainScreen:
    HomeScreen:
    CountDownScreen:
    ToDoListScreen:     
    NotesScreen:
    StatisticsScreen:
    GamesScreen:
    AccountScreen:
    SettingsScreen:

<LoginScreen>:
    name: "login"
    MDFloatLayout:
        md_bg_color: app.theme_cls.surfaceColor
        MDFloatLayout:
            size_hint: None, None
            pos_hint: {"center_x": .7, "center_y": .9}
            
        MDLabel:
            text: "Where knowledge begins"
            pos_hint: {"center_x": .55, "center_y": .75}
            size_hint_x: .42
            halign: "left"
            font_name: "Tahoma Regular font"
            font_size: "11sp"
        
        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y":.55}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Username"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
                font_size : "16sp"

        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y": .43}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Password"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                password: True
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
                font_size : "16sp"
        
        Button:
            text: "Sign in"
            font_name: "Tahoma Regular font"
            size_hint: .8, .09 
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            background_color: 0,0,0,0
            on_release: 
                on_release: app.change_screen("mainscreen")
        
            canvas.before:
                Color:
                    rgb: app.btn_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
        
        Button:
            text: "Sign up"
            font_name: "Tahoma Regular font"
            size_hint: .8, .09 
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .2}
            background_color: 0,0,0,0
            on_release: app.change_screen("signup")
            canvas.before:
                Color:
                    rgb: app.btn_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]


<SignUpScreen>:
    name:'signup'
    MDFloatLayout:
        md_bg_color: app.theme_cls.surfaceColor
        MDFloatLayout:
            size_hint: .4, .08
            pos_hint: {"center_x": .7, "center_y": .9}
            
        MDLabel:
            text: "Hey, Login Now."
            pos_hint: {"center_x": .55, "center_y": .75}
            size_hint_x: .42
            halign: "left"
            font_name: "Tahoma Regular font"
            font_size: "11sp"
        
        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y":.67}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Full Name"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
                font_size : "16sp"

        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y":.55}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Email"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
                font_size : "16sp"

        MDFloatLayout:
            size_hint: .8, .09
            pos_hint: {"center_x": .5, "center_y": .43}
            canvas:
                Color:
                    rgb: rgba(245,245,245,255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
            TextInput:
                hint_text: "Password"
                size_hint: 1, None
                pos_hint: {"center_x": .5, "center_y":.5}
                height: self.minimum_height
                multiline: False
                password: False
                hint_text_color: rgba(168,168,168,255)
                background_color: 0,0,0,0
                padding: 18
                font_name: "Tahoma Regular font"
                font_size : "16sp"
        
        Button:
            text: "Sign Up"
            font_name: "Tahoma Regular font"
            size_hint: .8, .09 
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            background_color: 0,0,0,0
            on_release: app.change_screen("login")
            canvas.before:
                Color:
                    rgb: app.btn_color
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [8]
        
        Button:
            text: "Already have an account?"
            font_name: "Tahoma Regular font"
            size_hint: .8, .09 
            font_size: "14sp"
            pos_hint: {"center_x": .5, "center_y": .225}
            color: 0.6, 0.6, 0.6, 1
            background_color: 0,0,0,0
            on_release: app.change_screen("login")

<DrawerItem>
    active_indicator_color: "#e7e4c0"

    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        theme_icon_color: "Custom"
        icon_color: "#4a4939"

    MDNavigationDrawerItemText:
        text: root.text
        theme_text_color: "Custom"
        text_color: "#4a4939"

        
<DrawerLabel>
    adaptive_height: True
    padding: "18dp", 0, 0, "12dp"

    MDNavigationDrawerItemLeadingIcon:
        icon: root.icon
        theme_icon_color: "Custom"
        icon_color: "#4a4939"
        pos_hint: {"center_y": .5}

    MDNavigationDrawerLabel:
        text: root.text
        theme_text_color: "Custom"
        text_color: "#4a4939"
        pos_hint: {"center_y": .5}
        padding: "6dp", 0, "16dp", 0
        theme_line_height: "Custom"
        line_height: 0


<MainScreen>:
    id: "main_screen"
    name: 'mainscreen'
    nav_layout: nav_layout
    MDScreen:
        md_bg_color: self.theme_cls.backgroundColor
        id: "screen1"
        MDNavigationLayout:
            id: nav_layout  # Reference the MDNavigationLayout
            MDScreenManager:
                id: screen_manager
            
                HomeScreen:
                    name: 'homescreen'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Welcome to Home Screen"
                        halign: "center"
                CountDownScreen:
                    name: 'countdownscreen'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Countdown Screen"
                        halign: "center"
                ToDoListScreen:   
                    name: 'todolist'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "To-Do List Screen"
                        halign: "center"  
                NotesScreen:
                    name: 'notes'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Notes Screen"
                        halign: "center"
                StatisticsScreen:
                    name: 'statistics'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Statistics Screen"
                        halign: "center"

                GamesScreen:
                    name: 'games'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Games Screen"
                        halign: "center"
                AccountScreen:
                    name: 'account'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Account Screen"
                        halign: "center"
                SettingsScreen:
                    name: 'settings'
                    MDScreen:  # Add an MDScreen here 
                    MDBoxLayout:  # Header is now part of the screen content
                        orientation: "vertical"
                        spacing: 0
                        padding: 0
                        # Blue header section
                        MDBoxLayout:
                            height: "56dp"
                            padding: "12dp"
                            spacing: "12dp"

                            MDIconButton:
                                icon: "menu"
                                theme_icon_color: "Custom"
                                size: (80, 80)
                                size_hint: None, None
                                pos_hint: {"center_y": .95}
                                on_release: nav_drawer.set_state("toggle") 

                            MDLabel:
                                theme_text_color: "Custom"
                                text_color: "white"
                    MDLabel:
                        text: "Settings Screen"
                        halign: "center"
                                
            MDNavigationDrawer:
                id: nav_drawer
                radius: 0, dp(16), dp(16), 0

                MDNavigationDrawerMenu:

                    MDNavigationDrawerHeader:
                        orientation: "vertical"
                        padding: 0, 0, 0, "12dp"
                        adaptive_height: True

                        MDLabel:
                            text: "Title"
                            theme_text_color: "Custom"
                            theme_line_height: "Custom"
                            line_height: 0
                            text_color: "#4a4939"
                            adaptive_height: True
                            padding_x: "16dp"
                            font_style: "Display"
                            role: "small"

                        MDLabel:
                            text: "...."
                            padding_x: "18dp"
                            adaptive_height: True
                            font_style: "Title"
                            role: "large"

                    MDNavigationDrawerDivider:

                    DrawerItem:
                        icon: "home"
                        text: "Home"
                        on_release: screen_manager.current = 'homescreen'

                    DrawerItem:
                        icon: "clock-outline"
                        text: "Count down"
                        on_release: 
                            screen_manager.current = 'countdownscreen'
                    
                    DrawerItem:
                        icon: "clipboard-list"
                        text: "To-do-list"
                        on_release: screen_manager.current = 'todolist'
                    
                    DrawerItem:
                        icon: "note-edit-outline"
                        text: "Note"
                        on_release: screen_manager.current = 'notes'

                    DrawerItem:
                        icon: "chart-bar"
                        text: "Statistics"
                        on_release: screen_manager.current = 'statistics'
                        
                    DrawerItem:
                        icon: "gamepad-variant"
                        text: "Game"
                        on_release: screen_manager.current = 'games'
                        
                    DrawerItem:
                        icon: "account"
                        text: "Profile"
                        on_release: screen_manager.current = 'account'
                
                    MDNavigationDrawerDivider:
                        size_hint_y: None
                        height: "1dp"
                                            
                    DrawerItem:
                        icon: "cog"
                        text: "Settings"
                        on_release: screen_manager.current = 'settings'
                        
                    DrawerItem:
                        icon: "logout"
                        text: "Log out"
                        on_release: root.manager.current = 'login'

"""
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
    nav_layout = ObjectProperty()
    def on_enter(self):
        Window.size = (900, 600)
    def change_screen(self, screen_name):
        self.screen_manager.transition = FadeTransition()
        self.screen_manager.current = screen_name

class HomeScreen(Screen):
    # You can initialize any properties here if needed
    def set_main_screen(self):
        # Now you can access app.root
        main_screen = self.manager.get_screen('mainscreen') 

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
# Ensure each screen is correctly registered and named.
sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))   
sm.add_widget(SignUpScreen(name='signup'))
sm.add_widget(MainScreen(name='mainscreen'))



# Main application class
class MainApp(MDApp):
    btn_color = ListProperty((177 / 255, 35 / 255, 65 / 255, 1))

    def build(self):
        self.screen_manager = Builder.load_string(Screen_Manager)
        
        return self.screen_manager

    def open_drawer(self, instance):
        Clock.schedule_once(lambda dt: self.toggle_drawer(instance), 0.1)

    def toggle_drawer(self, instance):
        nav_layout = instance.parent.parent.parent
        nav_layout.ids.nav_drawer.set_state("toggle")

    def change_screen(self, screen_name):
        self.screen_manager.transition = FadeTransition()
        self.screen_manager.current = screen_name



if __name__ == "__main__":
    MainApp().run()