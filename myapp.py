from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
Builder.load_file('My.kv')

Window.size = (600, 600)
Window.clearcolor = (225/255, 255/255, 255/255)
Window.title = 'Приложение'

class Container(GridLayout):
    pass

class MyApp(App):

    def build(self):


        return Container()

if __name__ == "__main__":
    MyApp().run()
