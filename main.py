magz = 0
magy = 0
magx = 0
serial.set_tx_buffer_size(128)
serial.set_baud_rate(BaudRate.BAUD_RATE9600)
pins.analog_set_pitch_pin(AnalogPin.P1)
music.set_volume(255)
music.play(music.string_playable("D D A A B B A - ", 120),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.show_leds("""
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        """)
basic.forever(on_forever)

def on_forever2():
    global magx, magy, magz
    magx = input.magnetic_force(Dimension.X)
    magy = input.magnetic_force(Dimension.Y)
    magz = input.magnetic_force(Dimension.Z)
    serial.write_line("MagX=" + str(magx) + " MagY=" + str(magy) + " MagZ=" + str(magz))
    for index in range(1000):
        control.wait_micros(1000)
basic.forever(on_forever2)
