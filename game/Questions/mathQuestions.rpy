label initMathQuestions:
    $ mathQuestions = ["math_question1", "math_question2", "math_question3", "math_question4", "math_question5"]
    $ renpy.random.shuffle(mathQuestions)
    return

label math_question1:
    s "What is an obtuse angle?"
    menu:
        "Sorry, I am in a bit of a hurry!":
            s "Guess I will never know.."
        "An obtuse angle is an angle over 90 degrees.": #if {stats.math > x}
            $ ranking_meter += lower_increase
            s "Thank you so much!"
        "You’re in uni and don’t know that? Go google it.":
            $ ranking_meter -= lower_increase
            s "Asking you was pointless..."
    return

label math_question2:
    s "What is the value of pi?"
    menu:
        "Value is generally said to be 3.14.":
            $ ranking_meter += lower_increase
            s "Thank you so much!"
        "A quick google search would answer that question...":
            $ ranking_meter -= -lower_increase
            s "Asking you was pointless..."
        "Well, it’s very tasty and fun to bake, you should try it!":
            $ ranking_meter -= lower_increase
            s "Guess I will never know.."
        "The value of pi is 3.1415926535 8979323846 2643383279 5028841971 6939937510 5820974944 5923078164 0628620899 8628034825 3421170679 8214808651 3282306647 0938446095 5058223172 5359408128 4811174502 8410270193 8521105559 6446229489 5493038196 4428810975 6659334461 2847564823 3786783165 2712019091 4564856692 3460348610 4543266482 1339360726 0249141273 7245870066 0631558817 4881520920 9628292540.":
            if logic < 2:
                "You dont have enough logic"
                jump math_question2
            $ ranking_meter += higher_increase
            s "Thats amazing, how did you know that?"
    return

label math_question3:
    s "What is the volume of a sphere?"
    menu:
        "Sorry but I teach computer science, not maths.":
            $ ranking_meter += lower_increase
            s "Oh, I apologize I will go and ask someone else, thank you anyway!"
        "Hahaha what a dumb question, do I look like I teach Year 9?":
            $ ranking_meter -= higher_increase
            s "You don't have to be so mean..."
        "You should already know this, but it’s four thirds of pi times the cube of the radius.":
            $ ranking_meter += lower_increase
            s "Thank you so much!"
        "Pretty sure it depends on its size, but I’d say it ranges from 0 to infinity.":
            $ ranking_meter -= lower_increase
            s "Guess I will never know.."
    return
label math_question4:
    s "How does factorial work?"
    menu:
        "Fac-what? Is that what that exclamation point was called?
            No idea, I always thought people were just yelling their numbers when that came up.":
            $ ranking_meter -= lower_increase
            s "Why am I paying to come here?"
        "I’m not entirely sure I can explain it to you right now, I would need something to write on, sorry.":
            s "Thats unfortunate, I will go ask someone else."
        "If you have a number factorial, it means you take that number, and multiply it by the number
            one lower than it until you reach one, so 9! would be 9*8*7*6*5*4*3*2*1 for example.":
            $ ranking_meter += higher_increase
            s "Thats incrediple, thank you!"
    return


label math_question5:
    s "I know I am a bit late with this question, but why did they always use apples to
        teach us addition? I’m allergic to them and it always freaked me out!"
    menu:
        "Uhhh I think you need to seek a therapist to help you with this, I’m out.":
            $ ranking_meter -= lower_increase
            s "I am never asking anyone anything ever again!"
        "Oh that doesn’t sound very nice, I’m sorry you had to go through that.":
            $ ranking_meter += lower_increase
            s "Yes I was always freaked out by that, thank you for saying that!"
        "That sounds very unpleasant, but the apples were just to facilitate the
            learning and to be able to visualize it. They could have used bananas too.":
            $ ranking_meter += higher_increase
            s "I have been getting freaked out for nothing.. Thank you for explaining that!"
    return