
label laboratory:
    scene laboratory
    show student_laboratory at right
    with dissolve
    s "<INSERT QUESTION BY LABORATORY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label library:
    scene library
    show student_library at right
    with dissolve
    s "<INSERT QUESTION BY LIBRARY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label math_department:
    scene math_department
    show student_math at right
    with dissolve
    s "What is an obtuse angle?"
    menu:
        "Sorry, I am in a bit of a hurry!":
            $ ranking_meter -= 5
            jump expression next_room()
        "An obtuse angle is an angle over 90 degrees.":
            $ ranking_meter += 10
            jump expression next_room()
        "You’re in uni and don’t know that? Go google it.":
            $ ranking_meter -= 10
            jump start


label english_department:
    scene english_department
    show student_english at right
    with dissolve
    s "<INSERT QUESTION BY ENGLISH STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label physics_department:
    scene physics_department
    show student_physics at right
    with dissolve
    s "<INSERT QUESTION BY PHYSICS STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label chemistry_department:
    scene chemistry_department
    show student_chemistry at right
    with dissolve
    s "<INSERT QUESTION BY CHEMISTRY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label biology_department:
    scene biology_department
    show student_biology at right
    with dissolve
    s "<INSERT QUESTION BY BIOLOGY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label cs_department:
    scene cs_department
    show student_cs at right
    with dissolve
    s "<INSERT QUESTION BY CS STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label staff_lounge:
    scene staff_lounge
    show boss_lounge at right
    with dissolve
    s "<INSERT QUESTION BY BOSS"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label parking_lot:
    "CONGRATULATIONS FINISHED"
    pause
    return
