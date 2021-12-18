label music_department:
    python:
        music_dep_visited = True
        
        musicStudent = Student("music Student", "musicStudent.png")
    
    scene classroom_math_01 #change to music dep scene
    show screen gameUI
    show music_Student at right with dissolve

    call expression musicStudent.getQuestion(musicQuestions)
    call expression musicStudent.getQuestion(musicQuestions)
    call expression musicStudent.getQuestion(musicQuestions)
    call expression musicStudent.getQuestion(musicQuestions)

    hide music_Student with dissolve

    window hide
    hide screen gameUI
    "Ring ring! You have a notification!"
    show screen phone
    with dissolve
    pause
    hide screen phone
    with dissolve
    $renpy.call_screen("MapScreen",_layer="screens")