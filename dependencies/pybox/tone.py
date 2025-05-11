import board
import simpleio


class TONE:
    def __init__(self):
        self._pin = board.GP8

    def play(self, note=440, duration=1):
        simpleio.tone(self._pin, note, duration)

    def mplay(self, midinote, duration=1):
        note = mtof(midinote)
        self.play(note, duration)


def mtof(m):
    return int(2**((m-69) / 12) * 440)
