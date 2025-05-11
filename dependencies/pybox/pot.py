import board
import analogio
import time


class POT:
    def __init__(self):
        self._adc = analogio.AnalogIn(board.A0)

    @property
    def midivalue(self):
        return 127 - (self._adc.value >> 9)

    @property
    def value(self):
        return self.midivalue / 127

    @property
    def rawvalue(self):
        return (0XFFFF - self._adc.value) >> 4


if __name__ == '__main__':
    pot = POT()
    while True:
        print(f"{pot.value},\t{pot.midivalue}")
        time.sleep(0.1)
