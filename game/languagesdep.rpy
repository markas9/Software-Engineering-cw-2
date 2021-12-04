label languages_department:
    python:
        languages_dep_visited = True
        
        langQuestions = ["lang_question1", "lang_question2", "lang_question3", "lang_question4", "lang_question5"]
        renpy.random.shuffle(langQuestions)
        
        langStudent = Student("Lang Student", "langStudent.png")

    scene classroom_generic_01 720p

    show student_languages at right
    with dissolve

    call expression langStudent.getQuestion(langQuestions)
    call expression langStudent.getQuestion(langQuestions)
    call expression langStudent.getQuestion(langQuestions)
    call expression langStudent.getQuestion(langQuestions)
    call expression langStudent.getQuestion(langQuestions)

    hide student_languages with dissolve
    # jump campus_map
    window hide
    $renpy.call_screen("MapScreen",_layer="screens")
