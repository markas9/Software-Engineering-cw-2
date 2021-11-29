define five_points = 5
define ten_points = 10

label math_department:
    scene math_department
    ## 1st Student
    show student_math at right
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
    hide student_math with dissolve

    ## 2nd Student
    show student_math at left
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
    hide student_math with dissolve

    ## 3rd Student
    show student_math at center
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
    hide student_math with dissolve

    ## 4rth Student
    show student_math at right
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
    hide student_math with dissolve

    ## 5th Student
    show student_math at left
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
    hide student_math with dissolve

    jump expression next_room()

label languages_department:
    scene languages_department

    ## 1st Student
    show student_languages at right
    with dissolve
    s "I listened to this song and they said “voulez vous coucher avec moi, ce soir?” What does that mean?"
    menu:
        "I have no idea, is that spanish?":
            $ ranking_meter -= five_points
            s "Well that wasn't helpful at all!"
        "I am not sure that is an appropriate thing to ask.":
            s "Oh I am sorry if I said anything bad, I am going to go now.."
        "I believe it means “would you like to sleep with me tonight?”":
            $ ranking_meter += five_points
            s "That is so embarassing, I am so sorry!"
        "Brexit means Brexit, keep those languages away from me!":
            $ ranking_meter -= five_points
            s "You are the opposite of helpful..."
    hide student_math with dissolve

    ## 2nd Student
    show student_languages at left
    with dissolve
    s "I was reading something for my Italian homework, and
        noticed it looked similar to the writing I see on coins sometimes, why’s that?"
    menu:
        "I’m neither Italian nor a historian, so why do you ask me this? Leave me alone.":
            $ ranking_meter -= five_points
            s "True, I should of asked someone who speak Italian, but you could of been nicer about it."
        "Not entirely sure what they write on coins. Sorry but I’m afraid I can’t help.":
            $ ranking_meter += five_points
            s "That's fine I will go find someone else who might know!"
        "I believe you mean that Italian looks similar to Latin, and that would be because Italian stems from Latin.":
            $ ranking_meter += ten_points
            s "So thats why! Thank you!"
    hide student_math with dissolve

    ## 3rd Student
    show student_languages at center
    with dissolve
    s "I was listening to this cool song from ERA the other day called Ameno,
        but I didn’t recognize the language. Could you help me?"
    menu:
        "Sorry but I have absolutely no clue what you are talking about.":
            $ ranking_meter += five_points
            s "That's too bad, I will find someone else who does!"
        "I personally only listen to death metal, so I do not recognize the song,
            but I’m sure the Music department could help you.":
            $ ranking_meter -= five_points
            s "Why would the Music Department know what language it is..."
        "You are in luck, I am actually a big fan of that song. If I remember
            correctly, it is actually written in pseudo-latin, so it appears to be Latin,
            but actually does not mean anything.":
            $ ranking_meter += ten_points
            s "That's a shame but thank you any way!"
    hide student_math with dissolve

    ## 4rth Student
    show student_languages at right
    with dissolve
    s "My friends and I were discussing our German lecture today, and we were
        confused regarding the genders of nouns. Is the cat a feminine or masculin noun in german?"
    menu:
        "God, you Language students are by far the most annoying, walking through here is always painful.":
            $ ranking_meter -= ten_points
            s "Why are you so mean?"
        "I never learnt German, but all the members of the Pussycat Dolls were female,
            so if I had to guess, I’d say it’s feminine.":
            $ ranking_meter += five_points
            s "That makes sense!"
        "I believe it would be the same as in French, and in French the cat is masculin.":
            $ ranking_meter += five_points
            s "I didn't know that, thats so cool!"
        "Oh I remember my great-grandmother’s youngest sister’s boyfriend when she was
            in kindergarten had a German aunt, and according to them the cat was a feminine noun in german.":
            $ ranking_meter += five_points
            s "Weirdly specific but solves my question!"
    hide student_math with dissolve

    ## 5th Student
    show student_languages at left
    with dissolve
    s "Latin America is a name given to a big number of countries in the Americas,
        but they speak Spanish for the most part, does this mean Spanish came from Latin?"
    menu:
        "*music blasting from Airpods* SORRY I CAN’T HEAR YOU, AND I JUST CANNOT BRING MYSELF
            TO TURN BRITTNEY SPEARS DOWN!":
            $ ranking_meter -= five_points
            s "Who even listens to Brittney Spears in 2021?"
        "I’m not sure I should be the one you ask, but I believe that is the reason, yes.":
            $ ranking_meter += five_points
            s "Oh cool, Thank you!"
        "When I was but a small young girl, I was fascinated by the fireworks we would get to
            see on the 5th of November. Nowadays I blankly stare into them and feel myself fade
            away, little by little. Oh wait, that’s not what we were talking about. Yes, my wife’s
            friend is from Panama and she actually knows a lot of Latin because of this.":
            $ ranking_meter += ten_points
            s "... Thanks .. I think.."
    hide student_math with dissolve
    
    jump expression next_room()

label cs_department:
    scene cs_department
    show student_cs at right
    with dissolve
    s "<INSERT QUESTION BY CS STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label english_department:
    scene english_department
    show student_english at right
    with dissolve
    s "<INSERT QUESTION BY ENGLISH STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label physics_department:
    scene physics_department
    show student_physics at right
    with dissolve
    s "<INSERT QUESTION BY PHYSICS STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label chemistry_department:
    scene chemistry_department
    show student_chemistry at right
    with dissolve
    s "<INSERT QUESTION BY CHEMISTRY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label biology_department:
    scene biology_department
    show student_biology at right
    with dissolve
    s "<INSERT QUESTION BY BIOLOGY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label staff_lounge:
    scene staff_lounge
    show boss_lounge at right
    with dissolve
    s "<INSERT QUESTION BY BOSS"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start
label laboratory:
    scene laboratory
    show student_laboratory at right
    with dissolve
    s "<INSERT QUESTION BY LABORATORY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label library:
    scene library
    show student_library at right
    with dissolve
    s "<INSERT QUESTION BY LIBRARY STUDENT"
    menu:
        "<INSERT ANSWER A (CORRECT)":
            jump expression next_room()
        "<INSERT ANSWER B (WRONG)":
            jump start

label parking_lot:
    "CONGRATULATIONS FINISHED"
    pause
    return
