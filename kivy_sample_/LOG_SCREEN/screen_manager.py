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
            text: "Login"
            font_name: "Tahoma Regular font"
            size_hint: .8, .09 
            font_size: "18sp"
            pos_hint: {"center_x": .5, "center_y": .3}
            background_color: 0,0,0,0
            on_press: root.manager.current = 'mainscreen'
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

<MainScreen>:
    name: 'mainscreen'
    BoxLayout:
        orientation: 'horizontal'

        # Left Sidebar
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.1
            padding: "8dp"
            spacing: "8dp"
            canvas.before:
                Color:
                    rgba: 0.15, 0.15, 0.25, 1  # Darker background color
                Rectangle:
                    pos: self.pos
                    size: self.size

            # Buttons for different functions (using MDIconButton)
            MDIconButton:
                icon: "home"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}  # Centered in the layout
                pos_hint_y: '.75'
                on_press: root.manager.current = 'homescreen'
            MDIconButton:
                icon: "clock-outline"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'countdownscreen'
            MDIconButton:
                icon: "clipboard-list"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'todolist'
            MDIconButton:
                icon: "note-edit-outline"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'notes'
            MDIconButton:
                icon: "chart-bar"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'statistics'
            MDIconButton:
                icon: "gamepad-variant"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'games'
            MDIconButton:
                icon: "account"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'account'
            MDIconButton:
                icon: "cog"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                on_press: root.manager.current = 'settings'

        # Right Content Area (for switching screens)
        ScreenManager:
            
            id: content_area
            Screen:
                name: 'homescreen'
                Label:
                    text: "Homescreen"
                    color: 0.6, 0.6, 0.6, 1
            Screen:
                name: 'countdownscreen'
                Label:
                    text: "Countdown Timer"
                    color: 0.6, 0.6, 0.6, 1
            Screen:
                name: 'todolist'
                Label:
                    text: "To-Do List"
                    color: 0.6, 0.6, 0.6, 1
            Screen:
                name: 'notes'
                Label:
                    text: "Notes"
                    color: 0.6, 0.6, 0.6, 1
            Screen:
                name: 'statistics'
                Label:
                    text: "Statistics"
                    color: 0.6, 0.6, 0.6, 1
            Screen:
                name: 'games'
                Label:
                    text: "Games"
                    color: 0.6, 0.6, 0.6, 1
            Screen:
                name: 'account'
                Label:
                    text: "Account Information"
                    color: 0.6, 0.6, 0.6, 1
            Screen:
                name: 'settings'
                Label:
                    text: "Settings"
                    color: 0.6, 0.6, 0.6, 1

<HomeScreen>:
    name: 'homescreen'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Welcome to the Home Screen'
            halign: 'center'
        MDButton:
            text: "Back to login"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'login'

<CountDownScreen>:
    name: 'countdownscreen'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Countdown Screen'
            halign: 'center'
        MDButton:
            text: "Back to home"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'homescreen'

<ToDoListScreen>:
    name: 'todolist'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'To-Do List Screen'
            halign: 'center'
        MDButton:
            text: "Back to home"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'homescreen'


<NotesScreen>:
    name: 'notes'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Notes Screen'
            halign: 'center'
        MDButton:
            text: "Back to home"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'homescreen'

<StatisticsScreen>:
    name: 'statistics'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Statistics Screen'
            halign: 'center'
        MDButton:
            text: "Back to home"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'homescreen'

<GamesScreen>:
    name: 'games'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Games Screen'
            halign: 'center'
        MDButton:
            text: "Back to home"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'homescreen'

<AccountScreen>:
    name: 'account'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: 'Account Screen'
            halign: 'center'
        MDButton:
            text: "Back to home"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'homescreen'
<SettingsScreen>:
    name: 'settings'
    BoxLayout:
        orientation: 'vertical'
        md_bg_color: (1, 1, 1, 1)
        MDLabel:
            text: 'Settings Screen'
            halign: 'center'
        MDButton:
            text: "Back to home"
            color: 0,0,0,1
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            on_press: root.manager.current = 'homescreen'
"""