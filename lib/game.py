import uinput
import time

class Game:

    keymap = {
        'up': uinput.KEY_1,
        'down': uinput.KEY_2,
        'left': uinput.KEY_3,
        'right': uinput.KEY_4,
        'a': uinput.KEY_5,
        'b': uinput.KEY_6,
        'start': uinput.KEY_7,
        'select': uinput.KEY_8
    }
    events = (
        uinput.KEY_1,
        uinput.KEY_2,
        uinput.KEY_3,
        uinput.KEY_4,
        uinput.KEY_5,
        uinput.KEY_6,
        uinput.KEY_7,
        uinput.KEY_8
        )

    device = uinput.Device(events)

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        self.device.emit_click(self.button_to_key(button))
        time.sleep(.15)
