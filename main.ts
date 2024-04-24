let magz = 0
let magy = 0
let magx = 0
serial.setBaudRate(BaudRate.BaudRate9600)
music.setVolume(255)
music.play(music.stringPlayable("D D A A B B A - ", 120), music.PlaybackMode.LoopingInBackground)
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.showLeds(`
        . # . # .
        # . # . #
        # . . . #
        . # . # .
        . . # . .
        `)
})
basic.forever(function () {
    magx = input.magneticForce(Dimension.X)
    magy = input.magneticForce(Dimension.Y)
    magz = input.magneticForce(Dimension.Z)
    serial.writeLine("MagX=" + magx + " MagY=" + magy + " MagZ=" + magz)
    for (let index = 0; index < 1000; index++) {
        control.waitMicros(1000)
    }
})
