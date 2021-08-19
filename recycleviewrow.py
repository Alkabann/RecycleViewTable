from kivy.properties import ListProperty
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivymd.uix.textfield import MDTextFieldRect

class RecycleViewRow(RecycleDataViewBehavior, BoxLayout):
    index = None
    value_list = ListProperty([])
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i, w in enumerate(self.children):
            if isinstance(w, MDTextFieldRect):
                w.bind(text=self.update_widget_text)
            elif isinstance(w, CheckBox):
                w.bind(state=self.update_widget_text)

    def set_children_value(self, value_list):
        for i, value in enumerate(value_list):
            child = self.children[::-1][i] # les derniers seront les premiers
            if isinstance(child, MDTextFieldRect):
                child.text = value
            elif isinstance(child, CheckBox):
                child.state = value

    def get_recycle_view(self):
        "you have to give the recycle_view address (MDApp.get_running_app() is useful)"


    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        value_list = self.get_recycle_view().data[index]["value_list"]
        self.set_children_value(value_list)
        return super(RecycleViewRow, self).refresh_view_attrs(
            rv, index, data)

    def update_widget_text(self, instance, value):
        index_child = [instance == w for w in instance.parent.children][::-1].index(True)
        self.get_recycle_view().data[instance.parent.index]["value_list"][index_child] = value