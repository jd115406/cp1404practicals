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

MilesConverterApp().run()
