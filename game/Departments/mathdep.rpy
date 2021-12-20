label math_department:
    image sora smile = "characters/Sora_SummerUni_Smile_Blush2.png"
    image sora = "characters/Sora_SummerUni_Smile.png"
    image sora frown = "characters/Sora_SummerUni_Frown.png"

    python:
        math_dep_visited = True
        rankingBefore = ranking_meter
        mathStudent = Student()

    scene classroom_math_01
    show screen gameUI
    show sora at right with dissolve

    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)

    if ranking_meter < rankingBefore:
        show sora frown
        "You wern't very helpful.... I'll go ask someone else for help. :("
    else:
        show sora smile
        "Thanks so much for the help! Bye! :)"
    hide sora with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")
