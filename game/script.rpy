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

label start:
    show screen ranking_stats
    ## Need to initialize when player loses and starts over
    jump initialize


label begin:
    scene University of Bath Campus
    with fade

    "<START OF THE GAME>"

    show Julia Padget
    with dissolve

    jp "<INSERT DIALOGUE FOR JULIA PADGET>"
    "[department_list]"
    menu:

        "Start Game?":
            # jump campus_map
            window hide
            $renpy.call_screen("MapScreen",_layer="screens")


        "Skip to end (testing).":
            jump parking_lot

        "Return":
            "Do nothing"
