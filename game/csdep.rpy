label cs_department:
    python:
        cs_dep_visited = True
        

    scene library 720p

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
    show student_cs at left
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
    show student_cs at left
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

    jump campus_map