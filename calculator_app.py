from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import math

# Dark mode background
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class Calculator(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.spacing = 10
        self.padding = 10

        # Display
        self.display = TextInput(
            font_size=36,
            readonly=True,
            halign="right",
            multiline=False,
            background_color=(0, 0, 0, 1),
            foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.display)

        buttons = [
            "C", "⌫", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "x²", "√",
        ]

        for text in buttons:
            self.add_widget(self.create_button(text))

        # Equals button (full width)
        equals = Button(
            text="=",
            font_size=28,
            background_color=(0, 0.6, 1, 1)
        )
        equals.bind(on_press=self.calculate)
        self.add_widget(equals)

    def create_button(self, text):
        btn = Button(
            text=text,
            font_size=24,
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=self.on_button_press)
        return btn

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.display.text = ""

        elif text == "⌫":
            self.display.text = self.display.text[:-1]

        elif text == "x²":
            try:
                self.display.text = str(eval(self.display.text) ** 2)
            except:
                self.display.text = "Error"

        elif text == "√":
            try:
                self.display.text = str(math.sqrt(eval(self.display.text)))
            except:
                self.display.text = "Error"

        elif text == "%":
            try:
                self.display.text = str(eval(self.display.text) / 100)
            except:
                self.display.text = "Error"

        else:
            self.display.text += text

    def calculate(self, instance):
        try:
            self.display.text = str(eval(self.display.text))
        except:
            self.display.text = "Error"

class CalculatorApp(App):
    def build(self):
        return Calculator()

CalculatorApp().run()
