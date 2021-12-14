label initialize:
    python:
        #Init ranking meter bar variables
        ranking_meter = 10
        ranking_meter_max = 100
        #init room list
        department_list = ["math_department", "languages_department", "cs_department"]
        #init music that plays at the START of the game
        renpy.music.play("audio/Funny 8-bit music(lower_volume).mp3", fadeout=1)

        #visited vairables (can change this to a proximity matrix later)
        math_dep_visited = False
        cs_dep_visited = False
        languages_dep_visited = False
        #player stats
        logic = 1
        creativity = 1
        debating = 1

    define five_points = 5
    define ten_points = 10

    call initializeStudent
    jump begin

init python:

    #button which is used to add score on leaderboard
    def addLeaderboardButton():
        user_name = renpy.input("What is your name?", length=32)
        if user_name == "":
            renpy.jump("empty_username")
        else:
            user_name = user_name.strip()
            addToLeaderboard(user_name)

    #adds user to persistent data
    def addToLeaderboard(username):
        if not persistent.score_leaderboard:
            persistent.score_leaderboard = []
        if not persistent.score_rankings:
            persistent.score_rankings = []

        if len(persistent.score_rankings) >= 10:
            if ranking_meter <= persistent.score_rankings[9]:
                renpy.jump("low_score")
            else:
                persistent.score_rankings.append(tuple((username + " - ",ranking_meter)))
                persistent.score_rankings.sort(key=lambda x:x[1], reverse=True)
                persistent.score_leaderboard = []
                for name,rank in persistent.score_rankings[:10]:
                    score = name + str(rank)
                    persistent.score_leaderboard.append(score)
        else:
            persistent.score_rankings.append(tuple((username + " - ",ranking_meter)))
            persistent.score_rankings.sort(key=lambda x:x[1], reverse=True)
            persistent.score_leaderboard = []
            for name,rank in persistent.score_rankings:
                score = name + str(rank)
                persistent.score_leaderboard.append(score)

    #using a stack of the room list to jump to next room
    def next_scene(label_list, default):
        if len(label_list) == 0:
            room = renpy.jump(default)
        else:
            room = label_list.pop(0)
        change_music()
        return room

    ##Changes music depending of University ranking meter
    def change_music():
        if(renpy.music.get_playing(channel=u'music') != "audio/Land_of_8_Bits(lower_volume).mp3"):
            if(ranking_meter >= 20):
                renpy.music.play("audio/Land_of_8_Bits(lower_volume).mp3", fadeout=1)

    def check_ending_scene():
        if(ranking_meter >= 80):
            renpy.scene()
            renpy.show("car_not_stolen")
        elif (ranking_meter >= 50):
            renpy.scene()
            renpy.show("car_damaged")
        else:
            renpy.scene()
            renpy.show("car_stolen")

    def all_visited():

        if math_dep_visited and cs_dep_visited and languages_dep_visited:
                ui.close()
                renpy.jump("parking_lot")
