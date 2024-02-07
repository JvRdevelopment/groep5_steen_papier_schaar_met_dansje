let x = 0
function image () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        `)
    music.playTone(523, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    music.playTone(523, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        `)
    music.playTone(523, music.beat(BeatFraction.Whole))
    basic.clearScreen()
}
basic.forever(function () {
    if (TobbieII.RBlock(900)) {
        image()
        x = 1 + randint(0, 2)
        basic.pause(2000)
        if (x == 1) {
            basic.showLeds(`
                # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
                `)
        }
        if (x == 2) {
            basic.showLeds(`
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                `)
        }
        if (x == 3) {
            basic.showLeds(`
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
                `)
        }
        TobbieII.forward()
        basic.pause(500)
        TobbieII.backward()
        basic.pause(500)
        TobbieII.stopwalk()
        TobbieII.leftward()
        basic.pause(500)
        TobbieII.rightward()
        basic.pause(500)
        TobbieII.stopturn()
        TobbieII.shake_head(2)
        music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
    }
})
