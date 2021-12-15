label music_depmusicment:
    python:
        music_dep_visited = True
        
        musicStudent = Student("music Student", "musicStudent.png")
    
    scene classroom_math_01 #change to music dep scene
    show screen gameUI
    show music_Student at right with dissolve

    call expression mathStudent.getQuestion(musicQuestions)
    call expression mathStudent.getQuestion(musicQuestions)
    call expression mathStudent.getQuestion(musicQuestions)
    call expression mathStudent.getQuestion(musicQuestions)

    hide music_Student with dissolve

    window hide
    hide screen gameUI
    $renpy.call_screen("MapScreen",_layer="screens")