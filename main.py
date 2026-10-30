from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class JarvisApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.08, 0.14, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20,
        )

        title = Label(
            text="JARVIS\nPersonal AI Assistant",
            font_size="28sp",
            color=(0.2, 0.9, 0.9, 1),
            halign="center",
        )

        self.command = TextInput(
            hint_text="Type a command",
            multiline=False,
            size_hint_y=None,
            height=60,
        )

        send_button = Button(
            text="Send command",
            size_hint_y=None,
            height=60,
        )
        send_button.bind(on_press=self.send_command)

        self.status = Label(
            text="Ready. Type a command.",
            font_size="18sp",
        )

        layout.add_widget(title)
        layout.add_widget(self.command)
        layout.add_widget(send_button)
        layout.add_widget(self.status)

        return layout

    def send_command(self, instance):
        text = self.command.text.strip()

        if text:
            self.status.text = f"Yes boss. I heard: {text}"
        else:
            self.status.text = "Please enter a command."


if __name__ == "__main__":
    JarvisApp().run()
