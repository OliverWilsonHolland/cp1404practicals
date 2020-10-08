"""
CP1404/CP5632 Practical
Dynamically create labels from a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()
