label music_department:

    image musicStudent = "characters/s1-normal.png"
    image musicStudent smile = "characters/s1-smile2.png"
    image musicStudent frown = "characters/s1-angry.png"

    python:
        music_dep_visited = True
        rankingBefore = ranking_meter    
        musicStudent = Student()
    
    scene musicdep #change to music dep scene
    show screen gameUI
    show musicStudent at right with dissolve

    call expression musicStudent.getQuestion(musicQuestions) from _call_expression_11
    call expression musicStudent.getQuestion(musicQuestions) from _call_expression_12
    call expression musicStudent.getQuestion(musicQuestions) from _call_expression_13
    call expression musicStudent.getQuestion(musicQuestions) from _call_expression_14

    if ranking_meter < rankingBefore:
        show musicStudent frown
        "You wern't very helpful.... I'll go ask someone else for help. :("
    else:
        show musicStudent smile
        "Thanks so much for the help! Bye! :)"
    hide music_Student with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")