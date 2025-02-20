from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        # Основной контейнер
        layout = FloatLayout()

        Window.size = (600,750)

        # Задний фон
        self.background = Image(source="D:/УлГТУ/Python/PycharmProjects/Python lessons/test__work/cosmos.png", allow_stretch=True)

        # Добавление изображения на задний план
        layout.add_widget(self.background)

        # Кнопка
        self.button = Button(text="Начать игру", size_hint=(None, None), size=(200, 50),
                             pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button.bind(on_press=self.button_pressed)  # Привязка обработчика события
        layout.add_widget(self.button)  # Добавляем кнопку в layout

        return layout  # Возвращаем layout с изображением и кнопкой

    def button_pressed(self, instance):
        self.button.command = self.game() # Изменение текста кнопки

    def game(self):
        self.ship = Image(source="D:/УлГТУ/Python/PycharmProjects/Python lessons/test__work/ship.png")
        self.ship.size = (120,190)




if __name__ == "__main__":
    MyApp().run()

