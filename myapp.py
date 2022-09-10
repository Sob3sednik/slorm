from kivy.app import App
import math
#from kivy.uix.label import Label
from kivy.core.window import Window
#from kivy.uix.button import Button
#from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
Builder.load_file('My.kv')
from openpyxl import Workbook, load_workbook

Window.size = (1920, 1080)
#Window.clearcolor = (225/255, 255/255, 255/255)
Window.title = 'Приложение'


class Container(GridLayout):

    def calculate(self):

        wb = load_workbook("data.xlsx", read_only=True)
        ws = wb.active
        a023 = (ws['F3'].value)
        a024 = (ws['H3'].value)
        a025 = (ws['G3'].value)
        c102 = (ws['X3'].value)
        t = (ws['N3'].value)

        f = 96500
        r = 8.31
        epcd = -0.403 - (-0.763)
        epcu = 0.337 - (-0.763)
        kcu = math.exp((-2 * f * epcu) / (r * t))
        kcd = math.exp((-2 * f * epcd) / (r * t))
        ccu0 = kcu * ((a023 * c102)/a024)
        ccd0 = kcd * ((a025 * c102)/a024)

    #НИЖЕ НАПИСАНА ЗАГЛУШКА, ТАК КАК НЕКОТОРЫЕ ДАННЫЕ НЕИЗВЕСТНЫ
        amount_cu = 0
        if amount_cu == 0 or amount_cd == 0:
            self.test.text = str(ccd0)
        else:
            calc = str(2 + 2)
            self.test.text = str(calc)



class MyApp(App):

    def build(self):


        return Container()

if __name__ == "__main__":
    MyApp().run()
