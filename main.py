import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#Since this is a project to learn Kivy and Python simultaneously, there is commenting on every step.
#This is also meant to help me getting to know Github better.
#If that all bothers you, please have a look at my newer projects (if available).

class MyGrid(GridLayout):
    #initializer to start the app with infinite amount of key word input
    def __init__(self, **kwargs):
        #instructor call from inherited GridLayout by super() keyword
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 4
        self.add_widget(Label(text="Word to encrypt"))

#building the app
class Encrypter_Decrypter(App):
    def build(self):
        return MyGrid()

#running the app
if __name__ == "__main__":
    Encrypter_Decrypter().run()