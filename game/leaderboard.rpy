
screen scoreboard:
    frame:
        background Frame("images/leaderboard/blackboard_leaderboard.png")
        xmaximum 0.9
        ymaximum 0.9
        xalign 0.5
        yalign 0.1
        hbox:
            xalign 0.5
            yalign 0.1
            text "Leaderboard Scores" size 50
        vbox:
            ymaximum 0.8
            xalign 0.5
            yalign 0.4
            spacing 10
            if persistent.score_leaderboard:
                for username in persistent.score_leaderboard:
                    text username xalign 0.5

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

label empty_username:
    "Invalid username."
    jump finished

label low_score:
    "Ranking not high enough to make it to the leaderboard, better luck next time!"
    jump finished
