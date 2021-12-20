label languages_department:
    image soraW smile = "characters/Sora_WinterUni_Smile_Blush.png"
    image soraW = "characters/Sora_WinterUni_Smile.png"
    image soraW frown = "characters/Sora_WinterUni_Frown.png"


    python:
        languages_dep_visited = True
        rankingBefore = ranking_meter
        langStudent = Student()

    scene classroom_generic_01
    show screen gameUI
    show soraW at center with dissolve

    call expression langStudent.getQuestion(langQuestions) from _call_expression
    call expression langStudent.getQuestion(langQuestions) from _call_expression_1
    call expression langStudent.getQuestion(langQuestions)
    call expression langStudent.getQuestion(langQuestions)
    call expression langStudent.getQuestion(langQuestions)

    if ranking_meter < rankingBefore:
        show soraW frown
        "You wern't very helpful.... I'll go ask someone else for help. :("
    else:
        show soraW smile
        "Thanks so much for the help! Bye! :)"

    hide student_languages with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")
