"""
*This module help you to manage integrated button.*

---

Examples:
    >>> from pybox.button import SIMPLEBUTTON
    >>> but = SIMPLEBUTTON()
    >>> but.value
    0
    >>> # press and hold the button
    >>> but.value
    1

The module consists basically in two classes:
    - `SIMPLEBUTTON`: to get the value of the button
    - `BUTTON`: to bind custom functions to button behavior
"""

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import keypad


class SIMPLEBUTTON:
    """*SimpleButton class.*

    ---

    Examples:
        >>> but = SIMPLEBUTTON()
        >>> but.value
        0                           # if button is not pressed
    """

    def __init__(self, pin=None):
        if not pin:
            self.__pin = 6
            self.__btn = DigitalInOut(board.GP6)
        else:
            self.__pin = pin
            self.__btn = DigitalInOut(board.__dict__[f'GP{pin}'])

        self.__btn.direction = Direction.INPUT
        self.__btn.pull = Pull.UP

    def deinit(self):
        """Turn off the button."""
        self.__btn.deinit()

    @property
    def value(self) -> int:
        """Raw button value.

        It contains the value of the button based on its status: 1 if pressed, 0 otherwise.

        Examples:
            >>> but.value
            0
        """
        return int(not self.__btn.value)


class BUTTON:
    """*Button class.*

    ---

    Examples:
        >>> but = BUTTON()
        >>> def press_callback():
        ...     print("PRESSED")
        >>> def release_callback():
        ...     print("RELEASED")
        >>> but.press_handler(press_callback)
        >>> but.release_handler(release_callback)
        >>> while True:
        ...     but.update()

    """

    def __init__(self, pin=None):
        
        if not pin:
            self.__pin = board.GP6
        else:
            self.__pin = board.__dict__[f'GP{pin}']
        
        self.__keys = keypad.Keys((self.__pin,), value_when_pressed=False)
        self.__press_function = None
        self.__release_function = None
        self.__press_time = None
        self.__press_timestamp = None

    def update(self) -> None:
        """Update button state on main loop.

        Example:
            >>> but = BUTTON()
            >>> while True:
            ...     but.update()
        """

        event = self.__keys.events.get()

        if event:
            if event.pressed:
                self.__press_timestamp = time.monotonic()
                if self.__press_function:
                    self.__press_function()
            elif event.released:
                self.__press_time = time.monotonic() - self.__press_timestamp
                if self.__release_function:
                    self.__release_function()

    def press_handler(self, callback: callable = None) -> None:
        """Bind a function to call when button is pressed.

        Args:
            callback: a function to be executed when button is pressed.

        Examples:
            >>> def press_callback():
            ...     print("PRESSED")
            >>> push = BUTTON()
            >>> push.press_handler(press_callback)
            >>> while True:
            ...     # print PRESSED on press button
            ...     push.update()
        """

        self.__press_function = callback

    def release_handler(self, callback: callable = None) -> None:
        """Bind a function to call when button is released.

        Args:
            callback (callable): a function to be executed when button is released.

        Examples:
            >>> def release_callback():
            ...     print("RELEASED")
            >>> push = BUTTON()
            >>> push.release_handler(release_callback)
            >>> while True:
            ...     # print RELEASED on release button
            ...     push.update()
        """

        self.__release_function = callback

    def deinit(self):
        """Turn off the button."""
        self.__keys.deinit()

    @property
    def press_time(self) -> float:
        """Time of pressure."""
        return self.__press_time


if __name__ == "__main__":

    push = BUTTON()

    def pre():
        print("PRESSEEEED :-D")

    def rel():
        print("__RELEASED :-(")

    push.press_handler(pre)
    push.release_handler(rel)

    while True:
        push.update()
        # time.sleep(0.001)
