label math_department:
    python:
        math_dep_visited = True

        mathQuestions = ["math_question1", "math_question2", "math_question3", "math_question4", "math_question5"]
        renpy.random.shuffle(mathQuestions)

        mathStudent = Student("Math Student", "mathStudent.png")

    scene classroom_math_01
    show screen gameUI
    show math_student at right with dissolve

    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)
    call expression mathStudent.getQuestion(mathQuestions)

    hide math_student with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")
