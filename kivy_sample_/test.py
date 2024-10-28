from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)

KV = '''
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


MDScreen:
    md_bg_color: self.theme_cls.backgroundColor

    MDNavigationLayout:

        MDScreenManager:
			id: screen_manager
            MDScreen:
				MDBoxLayout:
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
                            size: (80,80)
                            size_hint: None, None
                            pos_hint: {"center_y": .95}
                            on_release: nav_drawer.set_state("toggle")
                            
                        MDLabel:
                            theme_text_color: "Custom"
                            text_color: "white"
                            
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
                    trailing_text: "+99"
                    trailing_text_color: "#4a4939"

                DrawerItem:
                    icon: "clock-outline"
                    text: "Count down"
                
                DrawerItem:
                    icon: "clipboard-list"
                    text: "To-do-list"
                
                DrawerItem:
                    icon: "note-edit-outline"
                    text: "Note"

                DrawerItem:
                    icon: "chart-bar"
                    text: "Statistics"
                    
                DrawerItem:
                    icon: "gamepad-variant"
                    text: "Game"
                    
                DrawerItem:
                    icon: "account"
                    text: "Profile"
            
                MDNavigationDrawerDivider:
					size_hint_y: None
                    height: "1dp"
                                        
                DrawerItem:
                    icon: "cog"
                    text: "Settings"
                    
                DrawerItem:
                    icon: "logout"
                    text: "Log out"
'''


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


class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)


Example().run()