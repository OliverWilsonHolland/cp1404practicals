"""
CP1404/CP5632 Practical
Kivy GUI program to convert Miles to KM
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to km """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 300)
        self.title = "Miles to KM Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation, output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        handle increment up/down button press
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        """
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
