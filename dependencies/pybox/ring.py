from neopixel import NeoPixel
import board
from pybox.color import RED, OFF


class RING:
    NUMBER = 12

    def __init__(self, ctrl_pin=board.GP27, color=RED, brightness=0.25):
        self._np = NeoPixel(
            ctrl_pin,
            RING.NUMBER,
            brightness=brightness,
            auto_write=True)

        self._col = [color] * RING.NUMBER
        self._global_col = color

    def __setitem__(self, index, item):
        """_set a pixel as list item_

        Args:
            index (int): pixel index
            item (tuple): tuple for RGB desc
        """
        self._np[index] = self.__parse_color(index, item)

    def __getitem__(self, index):
        return self._np[index]

    def set(self, index, col=None):
        if isinstance(index, int):
            self.__set_single_led(index, col)
            return None
        else:
            try:
                for i in index:
                    self.__set_single_led(i, col)
                return None
            except TypeError as exc:
                raise TypeError(
                    "Please, provide an int, a tuple or a list as first arg") from exc

    def __set_single_led(self, index, color):
        self._np[index] = self.__parse_color(index, color)

    def fill(self, col=None):
        if col is not None:
            if isinstance(col, tuple):
                if col != OFF:
                    self._global_col = col
                _col = col
            elif col == 0:
                _col = OFF
            else:
                _col = self._global_col
        else:
            _col = self._global_col

        self._np.fill(_col)

    def set_global_color(self, col=None):
        if col is not None:
            _col = [col]
        else:
            _col = [RED]
        self._col = _col * self._np.n

    def set_color(self, index, col=None):
        self._col[index] = col

    def __parse_color(self, index, col=None):
        if col is not None:
            if isinstance(col, tuple):
                if col != OFF:
                    self._col[index] = col
                return col
            elif col == 0:
                return OFF

        return self._col[index]
