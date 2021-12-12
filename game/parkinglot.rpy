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
        background Frame("images/leaderboard/pngtree-cartoon-blackboard-doodle-background-image_151572.jpg")
        xmaximum 0.9
        ymaximum 0.9
        xalign 0.5
        yalign 0.1
        hbox:
            xalign 0.5
            yalign 0.1
            text "Leaderboard Scores"
        viewport:
            mousewheel True
            draggable True
            xalign 0.9
            xpos 0.5
            ypos 0.2
            vbox:
                spacing 10
                if persistent.score_leaderboard:
                    for username in persistent.score_leaderboard:
                        text username

screen add_to_leaderboard_button:
    button:
        imagebutton:
            idle "images/leaderboard/button1.png"
            hover "images/leaderboard/button2.png"
            action Jump("addingScore")
            xpos 0.1
            ypos 0.7
        vbox:
            xpos 0.14
            ypos 0.75
            text "Add to Leaderboard"

screen clear_scoreboard_button:
    button:
        imagebutton:
            idle "images/leaderboard/button1.png"
            hover "images/leaderboard/button2.png"
            action Jump("clear_data")
            xpos 0.38
            ypos 0.7
        vbox:
            xpos 0.43
            ypos 0.75
            text "Clear Leaderboard"

screen exit_game_button:
    button:
        imagebutton:
            idle "images/leaderboard/button1.png"
            hover "images/leaderboard/button2.png"
            action Jump("exit_game")
            xpos 0.66
            ypos 0.7
        vbox:
            xpos 0.74
            ypos 0.75
            text "Exit Game"

label addingScore:
    $addLeaderboardButton()
    jump finished

label clear_data:
    $persistent._clear()
    jump finished

label exit_game:
    return

label empty_scoreboard:
    "There are no scores in the leaderboard."
    jump finished

label finished:

    window hide

    show screen scoreboard
    show screen clear_scoreboard_button
    show screen add_to_leaderboard_button
    show screen exit_game_button
    pause
    jump finished
