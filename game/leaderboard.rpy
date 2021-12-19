
image leaderboard_button = im.Scale("images/leaderboard/button1.png", 400,120)
image leaderboard_button2 = im.Scale("images/leaderboard/button2.png", 400,120)

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
            text "Leaderboard Scores" size 70 bold True
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
            idle "leaderboard_button"
            hover "leaderboard_button2"
            action Jump("addingScore")
            xpos 0.13
            ypos 0.73
        vbox:
            xpos 0.15
            ypos 0.765
            text "Add to Leaderboard"

screen clear_scoreboard_button:
    button:
        imagebutton:
            idle "leaderboard_button"
            hover "leaderboard_button2"
            action Jump("clear_data")
            xpos 0.4
            ypos 0.73
        vbox:
            xpos 0.43
            ypos 0.765
            text "Clear Leaderboard"

screen exit_game_button:
    button:
        imagebutton:
            idle "leaderboard_button"
            hover "leaderboard_button2"
            action Jump("exit_game")
            xpos 0.67
            ypos 0.73
        vbox:
            xpos 0.73
            ypos 0.765
            text "Exit Game"

label addingScore:
    python:
        if can_add_leaderboard == True:
            can_add_leaderboard = False
            addLeaderboardButton()
        else:
            narrator("Can only add score to leaderboard once per run!")
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
