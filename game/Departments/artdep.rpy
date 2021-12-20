label art_department:
    image artStudent = "characters/sm1_sensei_normal.png"
    image artStudent frown = "characters/sm1_sensei_angry.png"
    image artStudent smile = "characters/sm1_sensei_smile.png"

    python:
        art_dep_visited = True
        rankingBefore = ranking_meter    
        art_Student = Student()
    
    scene artdep #change to art dep scene
    show screen gameUI

    show artStudent at left with dissolve


    call expression art_Student.getQuestion(artQuestions) from _call_expression_7
    call expression art_Student.getQuestion(artQuestions) from _call_expression_8
    call expression art_Student.getQuestion(artQuestions) from _call_expression_9
    call expression art_Student.getQuestion(artQuestions) from _call_expression_10


    if ranking_meter < rankingBefore:
        show artStudent frown
        "You wern't very helpful.... I'll go ask someone else for help. :("
    else:
        show artStudent smile
        "Thanks so much for the help! Bye! :)"
    hide art_Student with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")