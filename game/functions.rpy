label initialize:
    python:
        #Init ranking meter bar variables
        ranking_meter = 10
        ranking_meter_max = 100
        #init room list with dungeon length which is then randomized
        room_list = ["library", "laboratory", "math_department", "physics_department",
        "chemistry_department", "biology_department", "cs_department", "staff_lounge"]
        dungeon_length = 3
        renpy.random.shuffle(room_list)
        #init music that plays at the START of the game
        renpy.music.play("audio/Funny 8-bit music(lower_volume).mp3", fadeout=1)
    jump begin

init python:
    #using a stack of the room list to jump to next room
    def next_room():
        if len(room_list) <= dungeon_length:
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
