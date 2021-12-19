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
    image julia angry = "characters/julia_outfit1_angry.png"

    scene University of Bath Campus
    with fade

    "The ranking of the University of Lath has sunk moderately over the years, 
        and with Christmas holidays starting, the time the university has to 
        improve their ranking for the year is steadily decreasing."
    "University staff is tasked with aiding in the improvement of the rank by 
        attempting to drive up average test scores and student satisfaction."
    show julia angry
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

    menu:

        "Start Game?":
            window hide
            $renpy.call_screen("MapScreen",_layer="screens")

