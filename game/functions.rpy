label initialize:
    python:
        #Init ranking meter bar variables
        ranking_meter = 10
        ranking_meter_max = 100
        #init room list with dungeon length which is then randomized
        department_list = ["math_department", "languages_department", "cs_department"]
        #init music that plays at the START of the game
        renpy.music.play("audio/Funny 8-bit music(lower_volume).mp3", fadeout=1)


        #visited vairables (can change this to a proximity matrix later)
        math_dep_visited = False
        cs_dep_visited = False
        languages_dep_visited = False

    define five_points = 5
    define ten_points = 10

    jump begin

init python:
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
        return math_dep_visited and cs_dep_visited and languages_dep_visited