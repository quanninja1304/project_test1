from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText, MDButtonIcon
from kivymd.uix.screen import MDScreen

class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style="Light" # màu nền light hoặc dảk
        self.theme_cls.primary_palette="Olive" #màu text và icon trong button
        self.theme_cls.bg_dark = [0.965, 0.957, 1.0, 1] # color #F6F4FF in RGBA

        return (
            MDScreen(
                MDButton(
                    MDButtonIcon(
                        icon="eye"
                    ),
                    MDButtonText(
                        text="Password"
                    ),
                    style="elevated",
                    pos_hint={"center_x":0.5,"center_y":0.1}
                ),
                MDButton(
                    MDButtonIcon(
                        icon="home"
                    ),
                    MDButtonText(
                        text="Home"
                    ),
                    style="elevated",
                    pos_hint={"center_x":0.5,"center_y":0.5}
                ),
                md_bg_color=self.theme_cls.bg_dark,
            )
        )
    
if __name__=="__main__":
    Main().run()