"""
Convert Miles Program
"""

from kivy.app import App
from kivy.lang import Builder

CONVERSION = 1.60934


class MilesConverterApp(App):
    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_valid_input(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0

    def handle_calculate(self):
        value = self.get_valid_input()
        result = value * CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


MilesConverterApp().run()
