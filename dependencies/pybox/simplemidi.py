import usb_midi
import adafruit_midi

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
from adafruit_midi.control_change import ControlChange

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)


class MIDI:
    """MIDI class.

    Args:
        out_channel (int, optional): value between 0 and 15, default = 0

    Examples:
        >>> midi = MIDI()
        >>> midi.note_on(60, 100)
        >>> midi.note_off(60)
    """

    def __init__(self, out_channel=0):
        self._midi = adafruit_midi.MIDI(
            midi_out=usb_midi.ports[1], out_channel=out_channel
        )

    def note_on(self, pitch=60, velocity=100):
        """Send Note On message"""
        self._midi.send(NoteOn(pitch, velocity))

    def note_off(self, pitch=60):
        """Send Note Off message"""
        self._midi.send(NoteOff(pitch, 0))

    def cc(self, ctrl_num, ctrl_val):
        """Send control change message

        Examples:
            >>> midi = MIDI()
            >>> midi.note_on(60, 100)  # Accende la nota DO3
            >>> midi.note_off(60)       # Spegne la nota
            >>> midi.cc(64, 127)        # Invia un Control Change (es. sustain pedal)
        """
        self._midi.send(ControlChange(ctrl_num, ctrl_val))

    @property
    def out_channel(self):
        """Set out channel"""
        return self._midi.out_channel

    @out_channel.setter
    def out_channel(self, channel=0):
        self._midi.out_channel(channel)
