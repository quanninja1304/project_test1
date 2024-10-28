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
            text: "Hey, Login Now."
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
            on_release: root.manager.current = 'mainscreen'
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
            on_press: root.manager.current = 'signup' 
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
            on_press: root.manager.current = 'login'
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
            on_press: root.manager.current = 'login' 

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
    name: 'mainscreen'
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
"""