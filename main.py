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
        self.cols = 1

        #setting up a grid for bottom third so that the submit button is not the complete bottom half of the app
        self.bottom_grid = GridLayout()
        self.bottom_grid.cols = 3

        #top third
        self.add_widget(Label(text="Text to encrypt", font_size=30))

        #text input field for text to encrypt
        self.text_to_encrypt = TextInput(multiline=False)
        self.add_widget(self.text_to_encrypt)

        #submit button in the middle of the bottom third
        self.submit = Button(text="Submit", font_size=20)
        self.submit.bind(on_press=self.pressed_submit)

        self.bottom_grid.add_widget(Label(text=""))
        self.bottom_grid.add_widget(self.submit)
        self.bottom_grid.add_widget(Label(text=""))

        #implement bottom_grid into main grid
        self.add_widget(self.bottom_grid)

    #read text input
    def pressed_submit(self, instance):
        text = self.text_to_encrypt.text
        print("Text: ", text)

#building the app
class Encrypter_Decrypter(App):
    def build(self):
        return MyGrid()

#running the app
if __name__ == "__main__":
    Encrypter_Decrypter().run()