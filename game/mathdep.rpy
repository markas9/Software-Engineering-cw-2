label math_department:
    python:
        math_dep_visited = True
        #init room list with dungeon length which is then randomized
        math_student_list = ["math_student_1", "math_student_2", 
            "math_student_3","math_student_4","math_student_5"]
        renpy.random.shuffle(math_student_list)
    
    scene classroom_math_01 720p
    
    jump expression next_scene(math_student_list, "math_end")

label math_end:
    # jump campus_map
    window hide
    $renpy.call_screen("MapScreen",_layer="screens")


label math_student_1:
    show math_student_1 at right
    with dissolve
    s "What is an obtuse angle?"
    menu:
        "Sorry, I am in a bit of a hurry!":
            $ ranking_meter -= five_points
            s "Guess I will never know.."
        "An obtuse angle is an angle over 90 degrees.":
            $ ranking_meter += ten_points
            s "Thank you so much!"
        "You’re in uni and don’t know that? Go google it.":
            $ ranking_meter -= ten_points
            s "Asking you was pointless..."
    hide math_student_1 with dissolve
    jump expression next_scene(math_student_list, "math_end")

label math_student_2:
    show math_student_2 at left
    with dissolve
    s "What is the value of pi?"
    menu:
        "Value is generally said to be 3.14.":
            $ ranking_meter += ten_points
            s "Thank you so much!"
        "A quick google search would answer that question...":
            $ ranking_meter -= ten_points
            s "Asking you was pointless..."
        "The value of pi is 3.14(add another 60 decimal places)
            (answer only available if certain item/stats acquired)":
            $ ranking_meter += ten_points
            s "Thats amazing, how did you know that do that?"
        "Well, it’s very tasty and fun to bake, you should try it!":
            $ ranking_meter -= five_points
            s "Guess I will never know.."
    hide math_student_2 with dissolve
    jump expression next_scene(math_student_list, "math_end")

label math_student_3:
    show math_student_3 at center
    with dissolve
    s "What is the volume of a sphere?"
    menu:
        "Sorry but I teach computer science, not maths.":
            $ ranking_meter += five_points
            s "Oh, I apologize I will go and ask someone else, thank you anyway!"
        "Hahaha what a dumb question, do I look like I teach Year 9?":
            $ ranking_meter -= ten_points
            s "You don't have to be so mean..."
        "You should already know this, but it’s four thirds of pi times the cube of the radius.":
            $ ranking_meter += five_points
            s "Thank you so much!"
        "Pretty sure it depends on its size, but I’d say it ranges from 0 to infinity.":
            $ ranking_meter -= five_points
            s "Guess I will never know.."
    hide math_student_3 with dissolve
    jump expression next_scene(math_student_list, "math_end")

label math_student_4:
    show math_student_4 at right
    with dissolve
    s "How does factorial work?"
    menu:
        "Fac-what? Is that what that exclamation point was called?
            No idea, I always thought people were just yelling their numbers when that came up.":
            $ ranking_meter -= five_points
            s "Why am I paying to come here?"
        "I’m not entirely sure I can explain it to you right now, I would need something to write on, sorry.":
            s "Thats unfortunate, I will go ask someone else."
        "If you have a number factorial, it means you take that number, and multiply it by the number
            one lower than it until you reach one, so 9! would be 9*8*7*6*5*4*3*2*1 for example.":
            $ ranking_meter += ten_points
            s "Thats incrediple, thank you!"
    hide math_student_4 with dissolve
    jump expression next_scene(math_student_list, "math_end")


label math_student_5:
    show math_student_5 at left
    with dissolve
    s "I know I am a bit late with this question, but why did they always use apples to
        teach us addition? I’m allergic to them and it always freaked me out!"
    menu:
        "Uhhh I think you need to seek a therapist to help you with this, I’m out.":
            $ ranking_meter -= five_points
            s "I am never asking anyone anything ever again!"
        "Oh that doesn’t sound very nice, I’m sorry you had to go through that.":
            $ ranking_meter += five_points
            s "Yes I was always freaked out by that, thank you for saying that!"
        "That sounds very unpleasant, but the apples were just to facilitate the
            learning and to be able to visualize it. They could have used bananas too.":
            $ ranking_meter += ten_points
            s "I have been getting freaked out for nothing.. Thank you for explaining that!"
    hide math_student_5 with dissolve
    jump expression next_scene(math_student_list, "math_end")
