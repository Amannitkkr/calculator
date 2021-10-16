from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput



class MyApp(GridLayout):
    def calculate(self,calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except Exception:
                self.display.text="Error"


class LoginApp(App):
    def build(self):
        return MyApp()


if __name__ == '__main__':
    LoginApp().run()
