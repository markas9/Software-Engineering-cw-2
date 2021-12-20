label cs_department:
    image soraC smile = "characters/Sora_Casual_Smile_Blush.png"
    image soraC = "characters/Sora_Casual_Smile.png"
    image soraC frown = "characters/Sora_Casual_Frown.png"


    python:
        cs_dep_visited = True
        rankingBefore = ranking_meter
        csStudent = Student()

    scene library
    show screen gameUI
    show soraC at left with dissolve

    call expression csStudent.getQuestion(csQuestions) from _call_expression_2
    call expression csStudent.getQuestion(csQuestions) from _call_expression_3
    call expression csStudent.getQuestion(csQuestions) from _call_expression_4
    call expression csStudent.getQuestion(csQuestions) from _call_expression_5
    call expression csStudent.getQuestion(csQuestions) from _call_expression_6

    if ranking_meter < rankingBefore:
        show soraC frown
        "You wern't very helpful.... I'll go ask someone else for help. :("
    else:
        show soraC smile
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
