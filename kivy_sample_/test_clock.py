from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, SlideTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

KV = '''
ScreenManager:
    Screen:
        name: "screen1"
        BoxLayout:
            orientation: "vertical"
            Label:
                text: "Screen 1"
            Button:
                text: "Go to Screen 2 (Fade)"
                on_release: app.change_screen("screen2", "fade")

    Screen:
        name: "screen2"
        BoxLayout:
            orientation: "vertical"
            Label:
                text: "Screen 2"
            Button:
                text: "Go to Screen 1 (Slide)"
                on_release: app.change_screen("screen1", "slide")
'''

class TransitionApp(App):
    def build(self):
        self.screen_manager = Builder.load_string(KV)
        return self.screen_manager

    def change_screen(self, screen_name, transition_type):
        if transition_type == "fade":
            self.screen_manager.transition = FadeTransition()
        elif transition_type == "slide":
            self.screen_manager.transition = SlideTransition()
        self.screen_manager.current = screen_name

if __name__ == '__main__':
    TransitionApp().run()