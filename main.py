from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


use_kivy_settings = False


class MenuScreen(Screen):
    pass


class HostScreen(Screen):
    pass


class ContestantScreen(Screen):
    pass


class KC(Widget):
    pass


class KCApp(App):

    def build(self):

        self.title = 'KC - Knowledge Challenge'

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(HostScreen(name='host'))
        sm.add_widget(ContestantScreen(name='contestant'))
        return sm


if __name__ == '__main__':
    KCApp().run()
