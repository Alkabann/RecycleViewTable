from kivymd.app import MDApp
from kivy.lang import Builder
from recycleviewrow import RecycleViewRow

class MyRecycleViewRow(RecycleViewRow):
    def get_recycle_view(self):
        return MDApp.get_running_app().screen.ids["recycle_view"]


class MyApp(MDApp):
    def build(self):
        self.screen = Builder.load_file('main.kv')
        return self.screen


MyApp().run()