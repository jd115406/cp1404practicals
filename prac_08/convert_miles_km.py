"""
Convert Miles Program
"""

from kivy.app import App
from kivy.lang import Builder

CONVERSION = 1.60934


class MilesConverterApp(App):
    """MilesConverter App is an app that converts miles to kms"""
    def build(self):
        """Build GUI"""
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_valid_input(self):
        """Get input from text_input and convert to float, otherwise set to 0.0"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0

    def handle_calculate(self):
        """Convert miles to km using conversion factor and update label"""
        value = self.get_valid_input()
        result = value * CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Increment input by desired change"""
        value = self.get_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()


MilesConverterApp().run()
