define jg = Character("Julia Gadget")
define s = Character('Student', color="c8ffc8")
screen ranking_stats:
    frame:
        xalign 0.03 ypos 50
        vbox:
            text "Ranking Meter" size 22 xalign 0.5
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


    show Julia Padget
    with dissolve


    menu:

        "Start Game?":
            jump campus_map

        "Skip to end (testing).":
            jump parking_lot

        "Return":
            "Do nothing"
