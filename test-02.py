from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

import kivy
kivy.require('1.0.8')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

import random

class TutorialApp(App):
    def build(self):

        rSet1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        rSet1Is = str(random.choice(rSet1))

        Label(text=rSet1Is,
              font_size=150)

class ScrollViewApp(App):

    def build(self):



        # create a default grid layout with custom width/height
        layout = GridLayout(cols=1, padding=10, spacing=10,
                size_hint=(None, None), width=500)

        rSet1 = [1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26,27,28,29,30,
                31,32,33,34,35,36,37,38,39,40,
                41,42,43,44,45,46,47,48,49,50,
                51,52,53,54,55,56,57,58,59,60,
                61,62,63,64,65,66,67,68,69]

        rSet2 = [1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26]

        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required
        # to contain all the childs. (otherwise, we'll child outside the
        # bounding box of the childs)

        layout.bind(minimum_height=layout.setter('height'))

        # add button into that grid
        for i in range(5):
            rSet1Is = random.choice(rSet1)
            btn = Button(text=str(rSet1Is), size=(480, 40),
                         size_hint=(None, None))
            layout.add_widget(btn)

        # create a scroll view, with a size < size of the grid
        root = ScrollView(size_hint=(None, None), size=(500, 320),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        root.add_widget(layout)

        return root

class ButtonApp(App):

    def build(self):

        # create a default grid layout with custom width/height
        layout = GridLayout(cols=1, padding=10, spacing=10,
                size_hint=(None, None), width=500)

        rSet1 = [1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26,27,28,29,30,
                31,32,33,34,35,36,37,38,39,40,
                41,42,43,44,45,46,47,48,49,50,
                51,52,53,54,55,56,57,58,59,60,
                61,62,63,64,65,66,67,68,69]

        rSet2 = [1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26]

        # when we add children to the grid layout, its size doesn't change at
        # all. we need to ensure that the height will be the minimum required
        # to contain all the childs. (otherwise, we'll child outside the
        # bounding box of the childs)

        layout.bind(minimum_height=layout.setter('height'))

        # add button into that grid
        for i in range(6):
            if i < 5:
                rSet1Is = random.choice(rSet1)
                btn = Button(text=str(rSet1Is), size=(480, 40),
                            size_hint=(None, None))
                layout.add_widget(btn)
            elif i == 5:
                rSet2Is = random.choice(rSet2)
                btn = Button(text="PowerBall:  "+str(rSet2Is), size=(480, 40),
                            size_hint=(None, None))
                layout.add_widget(btn)

        # create a scroll view, with a size < size of the grid
        root = ScrollView(size_hint=(None, None), size=(500, 320),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        root.add_widget(layout)

        return root

if __name__ == "__main__":
    #TutorialApp().run()
    #randomNumber()
    #ScrollViewApp().run()
    ButtonApp().run()