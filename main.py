from kivy.app import App
from kivy.logger import Logger
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


use_kivy_settings = False


class MenuScreen(Screen):
    pass


class HostScreen(Screen):
    pass


class ContestantScreen(Screen):
    pass


class CreateScreen(Screen):
    pass


class Casey(Widget):
    pass


class CaseyApp(App):

    def build(self):

        self.title = 'Casey - Knowledge Challenge'

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(HostScreen(name='host'))
        sm.add_widget(ContestantScreen(name='contestant'))
        sm.add_widget(CreateScreen(name='create'))
        return sm

    def on_stop(self):
        Logger.debug('CaseyApp: Running on_stop()')


if __name__ == '__main__':
    CaseyApp().run()
