label initialize:
    python:
        #Init ranking meter bar variables
        ranking_meter = 10
        ranking_meter_max = 100
        #init room list with dungeon length which is then randomized
        room_list = ["math_department", "languages_department", "cs_department"]
        renpy.random.shuffle(room_list)
        #init music that plays at the START of the game
        renpy.music.play("audio/Funny 8-bit music(lower_volume).mp3", fadeout=1)
    jump begin

init python:
    #using a stack of the room list to jump to next room
    def next_room():
        if len(room_list) == 0:
            room = renpy.jump("parking_lot")
        else:
            room = room_list.pop(0)
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
