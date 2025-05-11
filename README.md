1. while keeping pressed the `boot` button, connect the board to the computer with usb cable
2. after a while a partition called `RPI-RP2` appears
3. Copy the file `adafruit-circuitpython-waveshare_rp2040_zero-en_US-9.2.7.uf2` in this partition and wait for operation to complete
4. a new partition is created, called `CIRCUITPY`
5. Go in the `lib` directory and there copy these items: 
   1. `pybox` *directory*
   2. neopixel.mpy
   3. adafruit_midi *directory*