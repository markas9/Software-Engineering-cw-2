label languages_department:
    python:
        languages_dep_visited = True
        
        langStudent = Student("Lang Student", "langStudent.png")

    scene classroom_generic_01
    show screen gameUI
    show student_languages at right with dissolve

    call expression langStudent.getQuestion(langQuestions)
    call expression langStudent.getQuestion(langQuestions)
    # call expression langStudent.getQuestion(langQuestions)
    # call expression langStudent.getQuestion(langQuestions)
    # call expression langStudent.getQuestion(langQuestions)

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
