label math_department:
    python:
        math_dep_visited = True
        
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

