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

    "Julia Gadget is a Computer Science professor at the University of Bath and has
        just finished her last lecture for the term."
    "As she exits her lecture hall to make her way to her car across campus to
        return to her family for the holidays, concerned students approach her to
        ask her questions regarding different matters."
    "Julia is faced with the decision of whether she wants to help the students
        and therefore increase the university ranking through average scores and
        satisfaction increasing, or turning down the students and
        returning home to her family faster."
>>>>>>> Stashed changes

    menu:

        "Start Game?":
            jump campus_map

        "Skip to end (testing).":
            jump parking_lot
<<<<<<< Updated upstream

        "Return":
            "Do nothing"
=======
>>>>>>> Stashed changes
