from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)

class JudoApp(App):
    def build(self):
        return Builder.load_file('judo.kv')


def calculator():
    print('1+1=2')

if __name__ == '__main__':
    JudoApp().run()