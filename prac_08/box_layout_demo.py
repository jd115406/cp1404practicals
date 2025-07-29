from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo app is an app that greets user input"""
    def build(self):
        """Build GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Updates output label with greeting"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Clears label and input"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
