define jp = Character('Julia Padget', color="c8ffc8")
define s = Character('Student', color="c8ffc8")

screen ranking_stats:
    frame:
        xalign 0.03 ypos 50
        vbox:
            text "Ranking Meter" size 22 xalign 0.5
            null height 10
            bar:
                xmaximum 200
                value ranking_meter
                range ranking_meter_max
                left_gutter 0
                right_gutter 0
                thumb None
                thumb_shadow None

screen stat(name, amount):

    text name xalign 0.5
    bar value StaticValue(amount, 100) xalign 0.5 xsize 250


label start:

    show screen ranking_stats
    play music "8-bit music.mp3" fadeout 1
    $renpy.random.shuffle(room_list)

    scene University of Bath Campus
    with fade

    "<START OF THE GAME>"

    show Julia Padget
    with dissolve

    jp "<INSERT DIALOGUE FOR JULIA PADGET>"
    "[room_list]"

menu:

    "Start Game?":
        jump expression next_room()

    "Return":
        "Do nothing"
