x = 0
def image():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        # # . # #
        # # . # #
        """)
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        """)
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    basic.clear_screen()

def on_forever():
    global x
    if TobbieII.rblock(900):
        image()
        x = 1 + randint(0, 2)
        basic.pause(2000)
        if x == 1:
            basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                # # . # #
                # # . # #
                """)
        if x == 2:
            basic.show_leds("""
                . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
                """)
        if x == 3:
            basic.show_leds("""
                # # # # #
                # . . . #
                # . . . #
                # . . . #
                # # # # #
                """)
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
        music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
            MelodyOptions.ONCE)
basic.forever(on_forever)
