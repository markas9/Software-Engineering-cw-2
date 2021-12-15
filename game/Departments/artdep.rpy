label art_department:
    python:
        art_dep_visited = True
        
        artStudent = Student("art Student", "artStudent.png")
    
    scene classroom_math_01 #change to art dep scene
    show screen gameUI
    show art_Student at right with dissolve

    call expression mathStudent.getQuestion(artQuestions)
    call expression mathStudent.getQuestion(artQuestions)
    call expression mathStudent.getQuestion(artQuestions)
    call expression mathStudent.getQuestion(artQuestions)

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