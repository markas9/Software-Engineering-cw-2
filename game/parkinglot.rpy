label parking_lot:
    $renpy.hide_screen("ranking_stats")
    $check_ending_scene()

    scene school_gate 720p
    with dissolve

    if ranking_meter >= 80:
        jump good_end
    elif ranking_meter >= 40:
        jump medium_end
    else:
        jump bad_end


label bad_end:

    "Car not found!"

    jump finished


label medium_end:

    "Car found with grafiti!"

    jump finished


label good_end:

    "Car found!"

    jump finished



screen scoreboard:
    frame:
        background Frame("images/leaderboard/leaderboard_b.jpg")
        xmaximum 0.9
        ymaximum 0.9
        xalign 0.5
        yalign 0.1
        viewport:
            mousewheel True
            draggable True
            xpos 0.47
            ypos 0.1
            vbox:
                spacing 10

                for item in persistent.score_leaderboard:
                    text item color "#FF0000" xalign 0.5 yalign 0.2



screen add_to_leaderboard:
    button:
        text "Add to Leaderboard"

label finished:

    window hide

    show screen scoreboard
    show screen add_to_leaderboard
    pause
    return
