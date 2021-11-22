define jp = Character('Julia Padget', color="c8ffc8")
define s = Character('Student', color="c8ffc8")

init python:
    room_list = ["library", "laboratory", "math_department", "physics_department",
        "chemistry_department", "biology_department", "cs_department", "staff_lounge"]
    dungeon_length = 3
    def next_room():
        if len(room_list) <= dungeon_length:
            room = renpy.jump("parking_lot")
        else:
            room = room_list.pop(0)
        return room

label start:
    play music "8-bit music.mp3" fadeout 1
    $renpy.random.shuffle(room_list)

    scene University of Bath Campus
    with fade

    "<START OF THE GAME>"

    show Julia Padget
    with dissolve

    jp "<INSERT DIALOGUE FOR JULIA PADGET>"
    "[room_list]"

menu:

    "Start Game?":
        jump expression next_room()

    "Return":
        "Do nothing"
