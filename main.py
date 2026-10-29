from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=30, spacing=20)
        title = Label(text="JARVIS\nPersonal AI Assistant", font_size="28sp")
        self.command = TextInput(hint_text="Type a command", multiline=False)
        status = Label(text="Ready. Type a command.")
        button = Button(text="Send command")
        button.bind(on_press=lambda x: setattr(status, "text", "Yes boss. I heard: " + self.command.text))
        layout.add_widget(title)
        layout.add_widget(self.command)
        layout.add_widget(button)
        layout.add_widget(status)
        return layout

JarvisApp().run()
