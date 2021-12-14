label cs_department:
    python:
        cs_dep_visited = True

        csQuestions = ["cs_question1", "cs_question2", "cs_question3", "cs_question4", "cs_question5"]
        renpy.random.shuffle(csQuestions)

        csStudent = Student("CS Student", "csStudent.png")

    scene library
    show screen gameUI
    show student_cs at left with dissolve

    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)
    call expression csStudent.getQuestion(csQuestions)

    hide student_cs with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")
