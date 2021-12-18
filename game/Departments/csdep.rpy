label cs_department:
    image soraC smile blush = "characters/Sora_Casual_Smile_Blush.png"
    image soraC smile = "characters/Sora_Casual_Smile.png"
    image soraC frown = "characters/Sora_Casual_Frown.png"


    python:
        cs_dep_visited = True
        rankingBefore = ranking_meter
        csStudent = Student("CS Student", "csStudent.png")

    scene library
    show screen gameUI
    show soraC smile at left with dissolve

    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)

    if ranking_meter < rankingBefore:
        show soraC frown
        "You wern't very helpful.... I'll go ask someone else for help. :("
    else:
        show soraC smile blush
        "Thanks so much for the help! Bye! :)"
    hide soraC with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")
