import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.op1_score = 0
        self.op2_score = 0
        
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2
        
        self.inside2 = GridLayout()
        self.inside2.cols = 1

        
        self.op1 = Label(text="Opponent 1: ", font_size = 40)
        self.inside.add_widget(self.op1)
        self.op2 = Label(text="Opponent 2: ", font_size = 40)
        self.inside.add_widget(self.op2)

        self.inside_op1 = GridLayout()
        self.inside_op1.cols = 3

        self.op1nb1 = Button(text="+1", font_size=40)
        self.op1nb1.bind(on_press=self.increment_op1)
        self.inside_op1.add_widget(self.op1nb1)
        self.op1n = TextInput(multiline=False)
        self.inside2.add_widget(self.op1n)
        self.op1nb2 = Button(text="-1", font_size=40)
        self.op1nb2.bind(on_press=self.decrement_op1)
        self.inside_op1.add_widget(self.op1nb2)

        self.inside2.add_widget(self.inside_op1)
        self.inside.add_widget(self.inside2)

        self.inside2_op2 = GridLayout()
        self.inside2_op2.cols = 1

        self.inside_op2 = GridLayout()
        self.inside_op2.cols = 3

        self.op2nb1 = Button(text="+1", font_size=40)
        self.op2nb1.bind(on_press=self.increment_op2)
        self.inside_op2.add_widget(self.op2nb1)
        self.op2n = TextInput(multiline=False)
        self.inside2_op2.add_widget(self.op2n)
        self.op2nb2 = Button(text="-1", font_size=40)
        self.op2nb2.bind(on_press=self.decrement_op2)
        self.inside_op2.add_widget(self.op2nb2)

        self.inside2_op2.add_widget(self.inside_op2)
        self.inside.add_widget(self.inside2_op2)

        self.inside_buttons = GridLayout()
        self.inside_buttons.cols = 1
        
        self.reset = Button(text="Set Board", font_size=40)
        self.reset.bind(on_press=self.set_board)
        self.inside_buttons.add_widget(self.reset)

        self.reset = Button(text="Reset Board", font_size=40)
        self.reset.bind(on_press=self.reset_board)
        self.inside_buttons.add_widget(self.reset)

        self.inside_intermission = GridLayout()
        self.inside_intermission.cols = 1

        self.set_button = Button(text="Set Intermission Message", font_size=20)
        self.set_button.bind(on_press=self.change_intermission_message)
        self.inside_intermission.add_widget(self.set_button)

        self.set_text = TextInput(text="", font_size=20)
        self.set_text.bind(on_press=self.change_intermission_message)
        self.inside_intermission.add_widget(self.set_text)

        self.inside.add_widget(self.inside_buttons)
        self.inside.add_widget(self.inside_intermission)
        self.add_widget(self.inside)

    def reset_board(self, instance):
        self.op1_score = 0
        self.op2_score = 0

        self.op1.text = self.op1n.text + ": " + str(self.op1_score)
        self.op2.text = self.op2n.text + ": " + str(self.op2_score)
    
    def set_board(self, instance):
        self.op1.text = self.op1n.text + ": " + str(self.op1_score)
        self.op2.text = self.op2n.text + ": " + str(self.op2_score)

        FileEditor().write_value(self.op1.text, 1)
        FileEditor().write_value(self.op2.text, 2)

    def increment_op1(self, instance):
        self.op1_score += 1
        self.op1.text = self.op1n.text + ": " + str(self.op1_score)
        FileEditor().write_value(self.op1.text, 1)
    def decrement_op1(self, instance):
        self.op1_score -= 1
        self.op1.text = self.op1n.text + ": " + str(self.op1_score)
        FileEditor().write_value(self.op1.text, 1)
    def increment_op2(self, instance):
        self.op2_score += 1
        self.op2.text = self.op2n.text + ": " + str(self.op2_score)
        FileEditor().write_value(self.op2.text, 2)
    def decrement_op2(self, instance):
        self.op2_score -= 1
        self.op2.text = self.op2n.text + ": " + str(self.op2_score)
        FileEditor().write_value(self.op2.text, 2)
    def change_intermission_message(self, instance):
        FileEditor().write_value(self.set_text.text, 3)
        
        

class MyApp(App):
    def build(self):
        return MyGrid()


class FileEditor():

    def __init__(self):
        
        self.opponent_1 = "opponent1.txt"
        self.opponent_2 = "opponent2.txt"

    def write_value(self, string_value, opponent):
        if opponent == 1:
            self.op1 = open(self.opponent_1, "w")
            self.op1.write(string_value)
            self.op1.close()
        elif opponent == 2:
            self.op2 = open(self.opponent_2, "w")
            self.op2.write(string_value)
            self.op2.close()
        else:
            self.intermission_file = open("Intermission Message.txt", "w")
            self.intermission_file.write(string_value)
            self.intermission_file.close()

if __name__ == "__main__":
    MyApp().run()
