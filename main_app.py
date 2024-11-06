# напиши здесь свое приложение
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from ruffier import test

#1 экран - приветствие и дисклеймер

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        line = BoxLayout(orientation = 'vertical')
        name = Label(text='Тест Руфье')
        description = Label(text='Это приложение \nдля анализа работоспособности сердца')
        disclaimer = Label(text='Это приложение НЕ является \n инструментом для постановки диагнозов')
        age_ = Label(text='Этот тест только до 18 лет!')
        btn = Button(text='Далее')
        btn.on_press = self.next
        line.add_widget(name)
        line.add_widget(description)
        line.add_widget(disclaimer)
        line.add_widget(age_)
        line.add_widget(btn)
        self.add_widget(line)
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'
        
#2 экран - введение в курс дела, ввод возраста и Кнопка старт

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        line2 = BoxLayout(orientation = 'vertical')
        plan2 = Label(text='Нужно ввести свой возраст, потом 3 пульса, чтобы получить результат')
        age_text = Label(text='Введите возраст:')
        age = TextInput()
        btn = Button(text='Далее')
        line2.add_widget(plan2)
        line2.add_widget(age_text)
        line2.add_widget(age)
        line2.add_widget(btn)
        self.add_widget(line2)
        
        btn.on_press = self.next
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'third'
        
#3 экран - текст для состояния покоя, ввод первого пельса и Кнопка продолжить

class ThirdScr(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        line3 = BoxLayout(orientation = 'vertical')
        calm_text = Label(text='Измерьте пульс в состоянии покоя за 15 секунд')
        pulse1 = TextInput()
        btn = Button(text='Далее')
        line3.add_widget(calm_text)
        line3.add_widget(pulse1)
        line3.add_widget(btn)
        self.add_widget(line3)
        
        btn.on_press = self.next
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'fourth'

#4 экран - текст для физической нагрузки и Кнопка продолжить

class FourthScr(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        line4 = BoxLayout(orientation = 'vertical')
        phys_text = Label(text='Сделайте 30 приседаний за 45 секунд')
        btn = Button(text='Далее')
        line4.add_widget(phys_text)
        line4.add_widget(btn)
        self.add_widget(line4)
        
        btn.on_press = self.next
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'fifth'
        
#5 экран - текст для состояния после физической активности, ввод второго пульса и Кнопка продолжить
        
class FifthScr(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        line5 = BoxLayout(orientation = 'vertical')
        calm5_text = Label(text='После того, как вы сделали приседания, измерьте пульс за 15 секунд')
        pulse2 = TextInput()
        btn = Button(text='Далее')
        line5.add_widget(calm5_text)
        line5.add_widget(pulse2)
        line5.add_widget(btn)
        self.add_widget(line5)
        
        btn.on_press = self.next
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'sixth'
        

#6 экран - текст для отдыха и Кнопка продолжить

class SixthScr(Screen):
    def __init__(self, name='sixth'):
        super().__init__(name=name)
        line6 = BoxLayout(orientation = 'vertical')
        relax_text = Label(text='Почувствуйте, что вы находитесь на пляже и отдохните 30 секунд')
        btn = Button(text='Далее')
        line6.add_widget(relax_text)
        line6.add_widget(btn)
        self.add_widget(line6)
        
        btn.on_press = self.next
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'seventh'

#7 экран - текст для состояния покоя, ввод третьего пульса и Кнопка для получения Результата

class SeventhScr(Screen):
    def __init__(self, name='seventh'):
        super().__init__(name=name)
        line7 = BoxLayout(orientation = 'vertical')
        calm7_text = Label(text='После хорошего отдыха измерьте пульс и введите его')
        pulse3 = TextInput()
        btn_result = Button(text='Посчитать')
        line7.add_widget(calm7_text)
        line7.add_widget(pulse3)
        line7.add_widget(btn_result)
        self.add_widget(line7)
        
        btn_result.on_press = self.next
        
    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'eighth'

#8 экран - вывод Результата и Кнопка начать заново

class EighthScr(Screen):
    def __init__(self, name='eighth'):
        super().__init__(name=name)
        line8 = BoxLayout(orientation = 'vertical')
        result_text = Label(text='')
        btn_restart = Button(text='Начать заново')
        line8.add_widget(result_text)
        line8.add_widget(btn_restart)
        self.add_widget(line8)
        
        btn_restart.on_press = self.next
        
    def next(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'first'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        sm.add_widget(ThirdScr())
        sm.add_widget(FourthScr())
        sm.add_widget(FifthScr())
        sm.add_widget(SixthScr())
        sm.add_widget(SeventhScr())
        sm.add_widget(EighthScr())
        return sm
    
app = MyApp()
app.run()