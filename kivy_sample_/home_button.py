from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivymd.uix.screen import MDScreen


class STUDYBUDDY(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Olive"  # "Purple", "Red"

        return (
            MDScreen(
                MDButton(
                    MDButtonIcon(
                        icon="eye-off",
                    ),
                    MDButtonText(
                        text="Password",
                    ),
                    style="elevated",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                ),
                md_bg_color=self.theme_cls.backgroundColor,
            )
        )

STUDYBUDDY().run()