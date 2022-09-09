from kivy.app import App
#from kivy.uix.label import Label
from kivy.core.window import Window
#from kivy.uix.button import Button
#from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
Builder.load_file('My.kv')

Window.size = (1920, 1080)
#Window.clearcolor = (225/255, 255/255, 255/255)
Window.title = 'Приложение'


class Container(GridLayout):

    def calculate(self):
        #consumption = flow_rate * pipe_area / 3600 (расход)
        #flow_rate = ??? (скорость потока)
        #pipe_area = 3.14 * pipe_diameter / 4 (площадь трубы)
        #pipe_diameter = ??? (диаметр трубы)
        #amount_cu = ??? (содержание меди)
        #amount_cd = ??? (содержание камдия)
        #concentration_cd = amount_cd / 1000 (концентрация камдия)
        #concentration_cu = amount_cu / 1000 (концентрация меди)
        #amount_zinc_dust = flow_rate * pipe_area * concentration_cu * 1.0288 / 1000 (количество цинковой пыли)
        #zinc_dust = concentration_cd * 0.5816 * ? * consumtion / 1000 (цинковая пыль)

        #НИЖЕ НАПИСАНА ЗАГЛУШКА, ТАК КАК НЕКОТОРЫЕ ДАННЫЕ НЕИЗВЕСТНЫ
        amount_cu = 0
        if amount_cu == 0 or amount_cd == 0:
            self.test.text = "Отказ в работе!"
        else:
            calc = str(2 + 2)
            self.test.text = calc



class MyApp(App):

    def build(self):


        return Container()

if __name__ == "__main__":
    MyApp().run()
