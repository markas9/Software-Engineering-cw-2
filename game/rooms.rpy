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

    ## 1st Student
    show student_cs at left
    with dissolve
    s "Why does my Python code not work? I checked over and over but it looks right to me."
    menu:
        "Better ask a TA during a lab, I’m off-duty and heading home now.":
            $ ranking_meter -= five_points
            s "I am never going to finish this coursework.."
        "Ask Santa Claus to gift you working code LMAO":
            $ ranking_meter -= five_points
            s "But my dealine is before Christmas..."
        "I haven’t seen your code, but the chance that it is due to indentation is very high.
            Make sure everything is indented correctly.":
            $ ranking_meter += five_points
            s "You are probably right, I will go check it now!"
        "I’m afraid I cannot help you, as I cannot help you with coursework.":
            $ ranking_meter -= five_points
            s "Starting to feel hopeless.."
    hide student_math with dissolve

    ## 2nd Student
    show student_cs at right
    with dissolve
    s "My group for the coursework is having a bit of trouble keeping track of
        our workload, do you have any tips?"
    menu:
        "I do, but I won’t say because I won’t help you with coursework.":
            $ ranking_meter -= five_points
            s "Its not even work-related but you won't help..."
        "All I can tell you is that there may or may not be some agile process
            or processes that facilitate visualization of the workload.":
            $ ranking_meter -= five_points
            s "Could of been more specific.."
        "This is a common problem for Software Engineering teams, and a reason
            why many choose to implement Kanban.":
            $ ranking_meter += five_points
            s "Oh thats great thank you!"
        "One good solution to this would be to implement Kanban as it uses a Kanban
            board which allows you to have a visual representation of the workflow. It can be digital or physical.":
            $ ranking_meter += ten_points
            s "That's good advice thank you!"
    hide student_math with dissolve

    ## 3rd Student
    show student_cs at center
    with dissolve
    s "I want to be able to take the square root of an input, but the command doesn’t work. What could my issue be?"
    menu:
        "Not sure about the issue with the code, but the issue with me is that I’m in a hurry
            and have no time. It's the holidays!":
            $ ranking_meter -= five_points
            s "Yeah... wonderful."
        "Hmm I would need to see your code to be able to help you really, sorry.":
            $ ranking_meter -= five_points
            s "That's fair, but it doesn't help me.."
        "Well, if the command doesn’t work at all, have you imported the appropriate library?
            You need to import the math.h library to use sqrt()":
            $ ranking_meter += five_points
            s "I forgot to do that, thank you!"
    hide student_math with dissolve

    ## 4rth Student
    show student_cs at center
    with dissolve
    s "Mrs. Gadget, I was wondering about Java. In Java, do I need to- Okay now that everyone
        thinks we are talking about Computer Science, do you collect Pokemon cards?"
    menu:
        "Wait what? Are you 12? Show me your ID, I have to verify your age.":
            $ ranking_meter -= five_points
            s "Oops.. byyee!"
        "Not entirely sure how this is an appropriate thing to ask a Computer Science professor,
            so I will just pretend this interaction never happened.":
            $ ranking_meter -= five_points
            s "I just asked about your Pokemon cards.."
        "Very strange question, but no, I do not. My children love Pokemon though.":
            $ ranking_meter += five_points
            s "I am glad todays kids love pokemon as much as I do!"
        "I don’t, but I used to. I still have all my old cards, though I don’t remember where they are.":
            $ ranking_meter += five_points
            s "Thats a shame but its cool you used to collect card!"
        "Very strange question, but no, I do not. My children love Pokemon though.":
            $ ranking_meter += ten_points
            s "Okay this is unexpected, but yes, I love Pokemon. What’s your favorite generation?
                I personally love Scyther, it’s such a cool Pokemon. I also played the games. I remember
                in Pokemon Blue I completed the entire Pokedex. I was obsessed. I can’t believe they are
                still coming out with new games. I appreciate it though, as it is keeping the love for Pokemon alive."
    hide student_math with dissolve

    ## 5th Student
    show student_cs at center
    with dissolve
    s "Is it possible for me to put an if statement inside another if statement?"
    menu:
        "I do believe that there are plenty of online forums that have already answered this so
            I would appreciate it if you went there instead of slowing me down from getting home.":
            $ ranking_meter -= five_points
            s "Simple Yes or not would of suffice.."
        "Yes.":
            $ ranking_meter += five_points
            s "That's great thank you!"
        "Yes, you can do that, as long as you indent properly and use your brackets appropriately":
            $ ranking_meter += five_points
            s "I will make sure to check those!"
    hide student_math with dissolve

    jump expression next_room()

label parking_lot:
    "CONGRATULATIONS FINISHED"
    pause
    return
